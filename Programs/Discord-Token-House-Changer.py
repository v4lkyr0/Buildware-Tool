# Copyright (c) 2026 v4lkyr0
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
 {PREFIX}04{SUFFIX} Leave HypeSquad House
""")
    choice = input(f"{INPUT} HypeSquad House {red}->{reset} ").strip().lstrip("0")
    
    headers = {
        "Authorization": token,
        "Content-Type": "application/json",
        "User-Agent": RandomUserAgents()
    }
    
    if choice == "4":
        print(f"{LOADING} Leaving HypeSquad House..", reset)
        try:
            response = requests.delete('https://discord.com/api/v9/hypesquad/online', headers=headers)
            if response.status_code == 204:
                print(f"{SUCCESS} Left HypeSquad House!", reset)
            else:
                print(f"{ERROR} Failed to leave HypeSquad House!", reset)
        except:
            print(f"{ERROR} Error while trying to leave HypeSquad House!", reset)
    elif choice == "1":
        house_id = "1"
    elif choice == "2":
        house_id = "2"
    elif choice == "3":
        house_id = "3"
    else:
        ErrorNumber()
    
    if choice in ["1", "2", "3"]:
        print(f"{LOADING} Changing HypeSquad House..", reset)
        data = {"house_id": house_id}
        try:
            response = requests.post('https://discord.com/api/v9/hypesquad/online', headers=headers, json=data)
            if response.status_code == 204:
                print(f"{SUCCESS} HypeSquad House changed!", reset)
            else:
                print(f"{ERROR} Failed to change HypeSquad House!", reset)
        except:
            print(f"{ERROR} Error while trying to change HypeSquad House!", reset)

    Continue()
    Reset()

except Exception as e:
    Error(e)