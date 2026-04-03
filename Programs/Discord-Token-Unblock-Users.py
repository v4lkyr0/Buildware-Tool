# Copyright (c) 2025 v4lkyr0
# See LICENSE file for details

from Plugins.Utils import *
from Plugins.Config import *

try:
    import requests
    import threading
except Exception as e:
    MissingModule(e)

Title("Discord Token Unblock Users")
Connection()

try:
    token = ChoiceToken()

    print(f"{LOADING} Unblocking Users..", reset)

    def UnblockUsers(token, blocked_users):
        for user in blocked_users:
            try:
                response = requests.delete(f'https://discord.com/api/v9/users/@me/relationships/'+user['id'], 
                                      headers={'Authorization': token, 'Content-Type': 'application/json'})
                if response.status_code == 204 or response.status_code == 200:
                    print(f"{SUCCESS} Status:{red} Unblocked {white}| User:{red} {user['user']['username']}", reset)
                else:
                    print(f"{ERROR} Status:{red} Failed    {white}| User:{red} {user['user']['username']}", reset)
            except:
                print(f"{ERROR} Status:{red} Error     {white}| User:{red} {user['user']['username']}", reset)

    processes = []
    blocked_id = requests.get("https://discord.com/api/v9/users/@me/relationships", headers={'Authorization': token, 'Content-Type': 'application/json'}).json()
    
    blocked_users = [user for user in blocked_id if user.get('type') == 2]
    
    if not blocked_users:
        print(f"{ERROR} No Blocked Users found!", reset)

    for users in [blocked_users[i:i+3] for i in range(0, len(blocked_users), 3)]:
        t = threading.Thread(target=UnblockUsers, args=(token, users))
        t.start()
        processes.append(t)
    for process in processes:
        process.join()

    Continue()
    Reset()

except Exception as e:
    Error(e)