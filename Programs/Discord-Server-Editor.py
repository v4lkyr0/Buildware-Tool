# Copyright (c) 2025-2026 v4lkyr0 — Buildware-Tools
# See the file 'LICENSE' for copying permission.
# --------------------------------------------------------
# EN: Non-commercial use only. Do not sell, remove credits
#     or redistribute without prior written permission.
# FR: Usage non-commercial uniquement. Ne pas vendre, supprimer
#     les crédits ou redistribuer sans autorisation écrite.

from Plugins.Utils import *
from Plugins.Config import *

try:
    import requests
except Exception as e:
    MissingModule(e)

Title("Server Editor")
Connection()

Scroll(GradientBanner(discord_banner))

try:
    token = ChoiceToken()

    server_id = input(f"{INPUT} Server Id {red}->{reset} ").strip()
    if not server_id:
        ErrorId()

    headers = {"Authorization": token, "Content-Type": "application/json", "User-Agent": RandomUserAgents()}

    print(f"{LOADING} Fetching server..", reset)

    guild_response = requests.get(f"https://discord.com/api/v9/guilds/{server_id}", headers=headers)

    if guild_response.status_code != 200:
        print(f"{ERROR} Could not access server!", reset)
        Continue()
        Reset()

    current_name = guild_response.json().get("name", "Unknown")

    Scroll(f"""
 {INFO} Current Name :{red} {current_name}{white}

 {PREFIX}01{SUFFIX} Change Name
 {PREFIX}02{SUFFIX} Change Description
 {PREFIX}03{SUFFIX} Change Afk Channel
 {PREFIX}04{SUFFIX} Change Afk Timeout
 {PREFIX}05{SUFFIX} Change Verification Level
 {PREFIX}06{SUFFIX} Change System Channel
""")

    choice = input(f"{INPUT} Choice {red}->{reset} ").strip().lstrip("0")

    if choice == "1":
        new_name = input(f"{INPUT} New Name {red}->{reset} ").strip()
        if not new_name:
            ErrorInput()
        print(f"{LOADING} Changing..", reset)
        response = requests.patch(f"https://discord.com/api/v9/guilds/{server_id}", headers=headers, json={"name": new_name})
        if response.status_code == 200:
            print(f"{SUCCESS} Name changed!", reset)
        else:
            print(f"{ERROR} Could not change name!", reset)

    elif choice == "2":
        new_description = input(f"{INPUT} New Description {red}->{reset} ").strip()
        print(f"{LOADING} Changing..", reset)
        response = requests.patch(f"https://discord.com/api/v9/guilds/{server_id}", headers=headers, json={"description": new_description})
        if response.status_code == 200:
            print(f"{SUCCESS} Description changed!", reset)
        else:
            print(f"{ERROR} Could not change description!", reset)

    elif choice == "3":
        channel_id = input(f"{INPUT} Afk Channel Id {red}->{reset} ").strip()
        if not channel_id:
            ErrorId()
        print(f"{LOADING} Changing..", reset)
        response = requests.patch(f"https://discord.com/api/v9/guilds/{server_id}", headers=headers, json={"afk_channel_id": channel_id})
        if response.status_code == 200:
            print(f"{SUCCESS} Afk channel changed!", reset)
        else:
            print(f"{ERROR} Could not change afk channel!", reset)

    elif choice == "4":
        print(f"{INFO} Values:{red} 60, 300, 900, 1800, 3600", reset)
        try:
            timeout = int(input(f"{INPUT} Afk Timeout {red}->{reset} ").strip())
            if timeout not in [60, 300, 900, 1800, 3600]:
                ErrorInput()
        except:
            ErrorInput()
        print(f"{LOADING} Changing..", reset)
        response = requests.patch(f"https://discord.com/api/v9/guilds/{server_id}", headers=headers, json={"afk_timeout": timeout})
        if response.status_code == 200:
            print(f"{SUCCESS} Afk timeout changed!", reset)
        else:
            print(f"{ERROR} Could not change afk timeout!", reset)

    elif choice == "5":
        print(f"{INFO} Levels:{red} 0=None, 1=Low, 2=Medium, 3=High, 4=Highest", reset)
        try:
            level = int(input(f"{INPUT} Verification Level {red}->{reset} ").strip())
            if level not in [0, 1, 2, 3, 4]:
                ErrorInput()
        except:
            ErrorInput()
        print(f"{LOADING} Changing..", reset)
        response = requests.patch(f"https://discord.com/api/v9/guilds/{server_id}", headers=headers, json={"verification_level": level})
        if response.status_code == 200:
            print(f"{SUCCESS} Verification level changed!", reset)
        else:
            print(f"{ERROR} Could not change verification level!", reset)

    elif choice == "6":
        channel_id = input(f"{INPUT} System Channel Id {red}->{reset} ").strip()
        if not channel_id:
            ErrorId()
        print(f"{LOADING} Changing..", reset)
        response = requests.patch(f"https://discord.com/api/v9/guilds/{server_id}", headers=headers, json={"system_channel_id": channel_id})
        if response.status_code == 200:
            print(f"{SUCCESS} System channel changed!", reset)
        else:
            print(f"{ERROR} Could not change system channel!", reset)

    else:
        ErrorChoice()

    Continue()
    Reset()

except Exception as e:
    Error(e)