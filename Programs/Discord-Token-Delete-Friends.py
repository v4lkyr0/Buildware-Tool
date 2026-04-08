# Copyright (c) 2026 v4lkyr0
# See LICENSE file for details

from Plugins.Utils import *
from Plugins.Config import *

try:
    import requests
    import threading
except Exception as e:
    MissingModule(e)

Title("Discord Token Delete Friends")
Connection()

try:
    token = ChoiceToken()

    print(f"{LOADING} Deleting Friends..", reset)

    def DeleteFriends(token, friends):
        for friend in friends:
            try:
                username = friend.get('user', {}).get('username', 'Unknown')
                response = requests.delete(f"https://discord.com/api/v9/users/@me/relationships/{friend['id']}", headers={'Authorization': token})
                if response.status_code in [200, 204]:
                    print(f"{SUCCESS} Status:{red} Deleted {white}| Username:{red} {username}", reset)
                else:
                    print(f"{ERROR} Status:{red} Failed  {white}| Username:{red} {username}", reset)
            except:
                print(f"{ERROR} Status:{red} Error   {white}| Username:{red} Unknown", reset)

    CHUNK_SIZE = 3
    
    processes = []
    friend_id = requests.get("https://discord.com/api/v9/users/@me/relationships", headers={'Authorization': token, 'Content-Type': 'application/json'}).json()

    if not friend_id:
        print(f"{ERROR} No Friends found!", reset)
        Continue()
        Reset()

    for friends in [friend_id[i:i+CHUNK_SIZE] for i in range(0, len(friend_id), CHUNK_SIZE)]:
        t = threading.Thread(target=DeleteFriends, args=(token, friends))
        t.start()
        processes.append(t)
    for process in processes:
        process.join()

    Continue()
    Reset()

except Exception as e:
    Error(e)