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
except Exception as e:
    MissingModule(e)

Title("Token Spammer")
Connection()

Scroll(GradientBanner(discord_banner))

try:
    token      = ChoiceToken()
    channel_id = input(f"{INPUT} Channel Id {red}->{reset} ").strip()
    message    = input(f"{INPUT} Message {red}->{reset} ").strip()

    if not channel_id or not message:
        ErrorInput()

    try:
        message_limit = int(input(f"{INPUT} Total Messages {red}->{reset} ").strip())
        if message_limit < 0:
            message_limit = 0
    except:
        message_limit = 0

    try:
        threads_number = int(input(f"{INPUT} Threads {red}->{reset} ").strip())
        if threads_number <= 0:
            ErrorNumber()
    except:
        ErrorNumber()

    print(f"{LOADING} Starting..", reset)

    message_count = 0

    def Spammer():
        global message_count

        if message_limit > 0 and message_count >= message_limit:
            return

        headers  = {"Authorization": token, "Content-Type": "application/json", "User-Agent": RandomUserAgents()}
        response = requests.post(f"https://discord.com/api/v9/channels/{channel_id}/messages", headers=headers, json={"content": message})

        if response.status_code in [200, 201]:
            message_count += 1
            print(f"{SUCCESS} Status:{red} Sent    {white}| Messages:{red} {message_count:<6}{white} | Channel:{red} {channel_id}", reset)
        else:
            print(f"{ERROR} Status:{red} Failed  {white}| Channel:{red} {channel_id}", reset)

    def Request():
        threads = []
        for _ in range(threads_number):
            if message_limit > 0 and message_count >= message_limit:
                break
            t = threading.Thread(target=Spammer)
            t.start()
            threads.append(t)
        for thread in threads:
            thread.join()

    while True:
        if message_limit > 0 and message_count >= message_limit:
            print(f"{INFO} Total messages sent:{red} {message_count}", reset)
            break
        Request()

    Continue()
    Reset()

except Exception as e:
    Error(e)