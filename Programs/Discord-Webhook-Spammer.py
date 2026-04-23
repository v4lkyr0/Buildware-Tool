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
    import requests
    import threading
    import time
except Exception as e:
    MissingModule(e)

Title("Webhook Spammer")
Connection()

Scroll(GradientBanner(discord_banner))

try:
    webhook = ChoiceWebhook()

    message = input(f"{INPUT} Message {red}->{reset} ").strip()
    if not message:
        ErrorInput()

    try:
        amount = int(input(f"{INPUT} Amount {red}->{reset} ").strip())
        if amount <= 0:
            ErrorNumber()
    except:
        ErrorNumber()

    try:
        threads_number = int(input(f"{INPUT} Threads {red}->{reset} ").strip())
        if threads_number <= 0:
            ErrorNumber()
    except:
        ErrorNumber()

    print(f"{LOADING} Starting..", reset)

    success_count = 0
    lock          = threading.Lock()

    def Spam():
        global success_count

        while success_count < amount:
            time.sleep(0.1)

            headers  = {"Content-Type": "application/json", "User-Agent": RandomUserAgents()}
            response = requests.post(webhook, json={"content": message}, headers=headers)

            if response.status_code == 204:
                with lock:
                    success_count += 1
                print(f"{SUCCESS} Status:{red} Sent         {white}| Messages:{red} {success_count}", reset)
            elif response.status_code == 429:
                retry_after = response.json().get("retry_after", 1)
                print(f"{ERROR} Status:{red} Rate Limited {white}| Waiting:{red} {retry_after}s", reset)
                time.sleep(retry_after)
            else:
                print(f"{ERROR} Status:{red} Failed       {white}| Code:{red} {response.status_code}", reset)

    thread_list = []
    for _ in range(threads_number):
        t = threading.Thread(target=Spam)
        thread_list.append(t)
        t.start()

    for t in thread_list:
        t.join()

    Continue()
    Reset()

except Exception as e:
    Error(e)