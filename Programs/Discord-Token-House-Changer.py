# Copyright (c) 2025 v4lkyr0
# See LICENSE file for details

from Plugins.Utils import *
from Plugins.Config import *

try:
    import requests
except Exception as e:
    MissingModule(e)

Title("Discord Token House Changer")
Connection()

try:
    token = ChoiceToken()

    Scroll(f"""
 {PREFIX}01{SUFFIX} HypeSquad Bravery
 {PREFIX}02{SUFFIX} HypeSquad Brilliance
 {PREFIX}03{SUFFIX} HypeSquad Balance
""")
    choice = input(f"{INPUT} HypeSquad House {red}->{reset} ").strip().lstrip("0")
    if choice == "1":
        house_id = "1"
    elif choice == "2":
        house_id = "2"
    elif choice == "3":
        house_id = "3"
    else:
        ErrorNumber()

    print(f"{LOADING} Changing HypeSquad House..", reset)

    headers = {'Authorization': token, 'Content-Type': 'application/json', 'User-Agent': RandomUserAgents()}
    data    = {'house_id': house_id}

    try:
        response = requests.post('https://discord.com/api/v9/hypesquad/online', headers=headers, json=data)
        if response.status_code == 204:
            print(f"{SUCCESS} HypeSquad House changed!", reset)
        else:
            print(f"{ERROR} Failed to change HypeSquad House!", reset)
    except:
        print(f"{ERROR} Error while trying to change the HypeSquad House!", reset)

    Continue()
    Reset()

except Exception as e:
    Error(e)