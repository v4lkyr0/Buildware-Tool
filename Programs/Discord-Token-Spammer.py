# Copyright (c) 2025 v4lkyr0
# See LICENSE file for details

from Plugins.Utils import *
from Plugins.Config import *

try:
    import requests
    import threading    
except Exception as e:
    MissingModule(e)

Title("Discord Token Spammer")
Connection()

try:
    token          = ChoiceToken()
    channel_id     = input(f"{INPUT} Channel Id {red}->{reset} ")
    message        = input(f"{INPUT} Message {red}->{reset} ")
    threads_number = int(input(f"{INPUT} Threads {red}->{reset} "))
    if not channel_id or not message:
        ErrorInput()
    elif not threads_number or threads_number <= 0:
        ErrorNumber()

    print(f"{LOADING} Starting Token Spammer..", reset)

    def Spammer(token, channel_id, message):
        try:
            headers = {"Authorization": token, "Content-Type": "application/json", "User-Agent": RandomUserAgents()}
            payload = {"content": message}

            response = requests.post(f"https://discord.com/api/v9/channels/{channel_id}/messages", headers=headers, json=payload)
            if response.status_code in [200, 201]:
                print(f"{SUCCESS} Status:{red} Sent   {white}| Channel Id:{red} {channel_id}", reset)
            else:
                print(f"{ERROR} Status:{red} Failed {white}| Channel Id:{red} {channel_id}", reset)
        except:
            print(f"{ERROR} Status:{red} Error  {white}| Channel Id:{red} {channel_id}", reset)

    def Request():
        threads = []
        try:
            for _ in range(threads_number):
                t = threading.Thread(target=Spammer, args=(token, channel_id, message))
                t.start()
                threads.append(t)
        except:
            ErrorNumber()

        for thread in threads:
            thread.join()

    while True:
        Request()

except Exception as e:
    Error(e)