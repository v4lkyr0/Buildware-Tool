# Copyright (c) 2025 v4lkyr0
# See LICENSE file for details

from Plugins.Utils import *
from Plugins.Config import *

try:
    import requests
except Exception as e:
    MissingModule(e)

Title("Discord Token Joiner")
Connection()

try:
    token = ChoiceToken()
    invite_code = input(f"{INPUT} Server Invitation {red}->{reset} ").split("/")[-1]

    print(f"{LOADING} Joining the Server..", reset)

    try:
        response = requests.post(f"https://discord.com/api/v9/invites/{invite_code}", headers={'Authorization': token})

        if response.status_code == 200:
            print(f"{SUCCESS} Token joined the Server!", reset)
        else:
            print(f"{ERROR} Failed to join the Server!", reset)
    except:
        print(f"{ERROR} Error while trying to join the Server!", reset)

    Continue()
    Reset()

except Exception as e:
    Error(e)