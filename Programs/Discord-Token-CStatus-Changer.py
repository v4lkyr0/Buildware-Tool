# Copyright (c) 2025 v4lkyr0
# See LICENSE file for details

from Plugins.Utils import *
from Plugins.Config import *

try:
    import requests
except Exception as e:
    MissingModule(e)

Title("Discord Token Custom Status Changer")
Connection()

try:
    token = ChoiceToken()

    new_status = input(f"{INPUT} Custom Status {red}->{reset} ")
    custom     = {"custom_status": {"text": new_status}}
    headers    = {'Authorization': token, 'Content-Type': 'application/json'}

    print(f"{LOADING} Changing Status..", reset)

    try:
        response = requests.patch("https://discord.com/api/v9/users/@me/settings", headers=headers, json=custom)
        if response.status_code == 200:
            print(f"{SUCCESS} Status changed!", reset)
        else:
            print(f"{ERROR} Failed to change Status!", reset)
    except:
        print(f"{ERROR} Error while trying to change Status!", reset)

    Continue()
    Reset()

except Exception as e:
    Error(e)