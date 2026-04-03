# Copyright (c) 2025 v4lkyr0
# See LICENSE file for details

from Plugins.Utils import *
from Plugins.Config import *

try:
    import requests
    import threading
except Exception as e:
    MissingModule(e)

Title("Discord Token Delete Dm")
Connection()

try:
    token = ChoiceToken()

    print(f"{LOADING} Deleting Dm..", reset)

    def DeleteDm(token, channels):
        for channel in channels:
            try:
                response = requests.delete(f"https://discord.com/api/v9/channels/{channel['id']}", headers={'Authorization': token})
                if response.status_code in [200, 204]:
                    print(f"{SUCCESS} Status:{red} Deleted {white}| Channel Id:{red} {channel['id']}", reset)
                else:
                    print(f"{ERROR} Status:{red} Failed  {white}| Channel Id:{red} {channel['id']}", reset)
            except:
                print(f"{ERROR} Status:{red} Error   {white}| Channel Id:{red} {channel['id']}", reset)

    processes  = []
    channel_id = requests.get("https://discord.com/api/v9/users/@me/channels", headers={'Authorization': token}).json()

    if not channel_id:
        print(f"{ERROR} No Dm found!", reset)
        Continue()
        Reset()

    for channel in [channel_id[i:i+3] for i in range(0, len(channel_id), 3)]:
        t = threading.Thread(target=DeleteDm, args=(token, channel))
        t.start()
        processes.append(t)
    for process in processes:
        process.join()

    Continue()
    Reset()

except Exception as e:
    Error(e)