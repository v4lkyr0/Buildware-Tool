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

Title("Token Leaver")
Connection()

Scroll(GradientBanner(discord_banner))

try:
    token   = ChoiceToken()
    headers = {"Authorization": token, "Content-Type": "application/json", "User-Agent": RandomUserAgents()}
    guilds  = requests.get("https://discord.com/api/v9/users/@me/guilds", headers=headers).json()

    if not guilds:
        print(f"{ERROR} No servers found!", reset)
        Continue()
        Reset()

    print(f"{LOADING} Leaving..", reset)

    for guild in guilds:
        guild_name = guild['name']
        response   = requests.delete(f"https://discord.com/api/v9/users/@me/guilds/{guild['id']}", headers=headers)

        if response.status_code in [200, 204]:
            print(f"{SUCCESS} Status:{red} Left    {white}| Server:{red} {guild_name}", reset)
        elif response.status_code == 400:
            response = requests.delete(f"https://discord.com/api/v9/guilds/{guild['id']}", headers=headers)
            if response.status_code in [200, 204]:
                print(f"{SUCCESS} Status:{red} Left    {white}| Server:{red} {guild_name}", reset)
            else:
                print(f"{ERROR} Status:{red} Failed  {white}| Server:{red} {guild_name}", reset)
        else:
            print(f"{ERROR} Status:{red} Failed  {white}| Server:{red} {guild_name}", reset)

    Continue()
    Reset()

except Exception as e:
    Error(e)