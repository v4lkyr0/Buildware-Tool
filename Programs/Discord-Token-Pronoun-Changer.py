# Copyright (c) 2026 v4lkyr0
# See LICENSE file for details

from Plugins.Utils import *
from Plugins.Config import *

try:
    import requests
except Exception as e:
    MissingModule(e)

Title("Discord Token Pronoun Changer")
Connection()

try:
    token = ChoiceToken()
    
    print(f"\n{INFO} Pronoun Options:")
    print(f"{PREFIX}01{SUFFIX} he/him")
    print(f"{PREFIX}02{SUFFIX} she/her")
    print(f"{PREFIX}03{SUFFIX} they/them")
    print(f"{PREFIX}04{SUFFIX} Custom Pronouns\n")
    
    choice = input(f"{INPUT} Choice {red}->{reset} ").strip().lstrip("0")
    
    pronoun_map = {
        "1": "he/him",
        "2": "she/her",
        "3": "they/them"
    }
    
    if choice == "4":
        new_pronoun = input(f"{INPUT} Custom Pronoun {red}->{reset} ")
    elif choice in pronoun_map:
        new_pronoun = pronoun_map[choice]
    else:
        ErrorChoice()

    print(f"{LOADING} Changing Pronoun..", reset)

    headers = {
        "Authorization": token,
        "Content-Type": "application/json",
        "User-Agent": RandomUserAgents()
    }

    data = {"pronouns": new_pronoun}

    try:
        response = requests.patch("https://discord.com/api/v9/users/@me/profile", json=data, headers=headers)
        if response.status_code == 200:
            print(f"{SUCCESS} Pronoun changed!", reset)
        else:
            print(f"{ERROR} Failed to change Pronoun!", reset)
    except:
        print(f"{ERROR} Error while trying to change Pronoun!", reset)

    Continue()
    Reset()

except Exception as e:
    Error(e)