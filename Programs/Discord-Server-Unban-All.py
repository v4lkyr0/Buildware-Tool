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
    import time
except Exception as e:
    MissingModule(e)

Title("Server Unban All")
Connection()

Scroll(GradientBanner(discord_banner))

try:
    token = ChoiceToken()

    server_id = input(f"{INPUT} Server Id {red}->{reset} ").strip()
    if not server_id:
        ErrorId()

    try:
        delay = float(input(f"{INPUT} Delay {red}->{reset} ").strip())
        if delay < 0.1:
            delay = 0.1
    except:
        delay = 0.5

    headers = {"Authorization": token, "Content-Type": "application/json", "User-Agent": RandomUserAgents()}

    print(f"{LOADING} Fetching bans..", reset)

    bans_response = requests.get(f"https://discord.com/api/v9/guilds/{server_id}/bans", headers=headers)

    if bans_response.status_code != 200:
        print(f"{ERROR} Could not fetch bans!", reset)
        Continue()
        Reset()

    bans = bans_response.json()

    if not bans:
        print(f"{INFO} No banned users found!", reset)
        Continue()
        Reset()

    print(f"{SUCCESS} Found:{red} {len(bans)}{white} banned user(s)", reset)
    print(f"{LOADING} Unbanning..", reset)

    unbanned_count = 0

    for ban in bans:
        user_id  = ban.get("user", {}).get("id")
        username = ban.get("user", {}).get("username", "Unknown")

        response = requests.delete(f"https://discord.com/api/v9/guilds/{server_id}/bans/{user_id}", headers=headers)

        if response.status_code in [200, 204]:
            unbanned_count += 1
            print(f"{SUCCESS} Unbanned:{red} {unbanned_count:<6}{white} | User:{red} {username}", reset)
        else:
            print(f"{ERROR} Status:{red} Failed  {white}| User:{red} {username}", reset)

        time.sleep(delay)

    print(f"{INFO} Total unbanned:{red} {unbanned_count}/{len(bans)}", reset)

    Continue()
    Reset()

except Exception as e:
    Error(e)