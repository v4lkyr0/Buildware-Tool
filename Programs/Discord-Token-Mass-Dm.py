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

Title("Token Mass Dm")
Connection()

Scroll(GradientBanner(discord_banner))

try:
    token = ChoiceToken()

    message = input(f"{INPUT} Message {red}->{reset} ").strip()
    if not message:
        ErrorInput()

    try:
        repetitions = int(input(f"{INPUT} Repetitions {red}->{reset} ").strip())
        if repetitions <= 0:
            ErrorNumber()
    except:
        ErrorNumber()

    headers  = {"Authorization": token, "Content-Type": "application/json", "User-Agent": RandomUserAgents()}
    channels = requests.get("https://discord.com/api/v9/users/@me/channels", headers=headers).json()

    if not channels:
        print(f"{ERROR} No dms found!", reset)
        Continue()
        Reset()

    print(f"{LOADING} Sending..", reset)

    sent_count   = 0
    failed_count = 0

    def MassDm(token, chunk, message):
        global sent_count, failed_count
        for channel in chunk:
            for user in [x["username"] for x in channel.get("recipients", [])]:
                response = requests.post(
                    f"https://discord.com/api/v9/channels/{channel['id']}/messages",
                    headers={"Authorization": token, "Content-Type": "application/json", "User-Agent": RandomUserAgents()},
                    json={"content": message}
                )
                if response.status_code in [200, 201]:
                    sent_count += 1
                    print(f"{SUCCESS} Status:{red} Sent    {white}| User:{red} {user}{white} | Total:{red} {sent_count}", reset)
                else:
                    failed_count += 1
                    print(f"{ERROR} Status:{red} Failed  {white}| User:{red} {user}", reset)
                time.sleep(0.1)

    threads    = []
    chunk_size = 3

    for _ in range(repetitions):
        for chunk in [channels[j:j + chunk_size] for j in range(0, len(channels), chunk_size)]:
            t = threading.Thread(target=MassDm, args=(token, chunk, message))
            t.start()
            threads.append(t)
            time.sleep(0.1)

    for thread in threads:
        thread.join()

    print(f"{SUCCESS} Sent:{red} {sent_count}{white} | Failed:{red} {failed_count}", reset)

    Continue()
    Reset()

except Exception as e:
    Error(e)