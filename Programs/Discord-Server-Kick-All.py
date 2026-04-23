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

Title("Server Kick All")
Connection()

Scroll(GradientBanner(discord_banner))

try:
    token = ChoiceToken()

    server_id = input(f"{INPUT} Server Id {red}->{reset} ").strip()
    if not server_id:
        ErrorId()

    kick_reason = input(f"{INPUT} Reason {red}->{reset} ").strip()
    if not kick_reason:
        kick_reason = "Kicked by Buildware-Tools"

    try:
        delay = float(input(f"{INPUT} Delay {red}->{reset} ").strip())
        if delay < 0.1:
            delay = 0.1
    except:
        delay = 0.5

    headers = {"Authorization": token, "Content-Type": "application/json", "User-Agent": RandomUserAgents()}

    print(f"{LOADING} Fetching members..", reset)

    members = []
    limit   = 1000
    after   = 0

    while True:
        response = requests.get(f"https://discord.com/api/v9/guilds/{server_id}/members?limit={limit}&after={after}", headers=headers, timeout=10)
        if response.status_code != 200:
            break
        batch = response.json()
        if not batch:
            break
        members.extend(batch)
        after = int(batch[-1]["user"]["id"])
        if len(batch) < limit:
            break

    if not members:
        print(f"{ERROR} No members found!", reset)
        Continue()
        Reset()

    print(f"{SUCCESS} Found:{red} {len(members)}{white} member(s)", reset)
    print(f"{LOADING} Kicking..", reset)

    kicked_count = 0

    for member in members:
        user_id  = member.get("user", {}).get("id")
        username = member.get("user", {}).get("username", "Unknown")

        response = requests.delete(f"https://discord.com/api/v9/guilds/{server_id}/members/{user_id}", headers=headers, params={"reason": kick_reason}, timeout=10)

        if response.status_code in [200, 204]:
            kicked_count += 1
            print(f"{SUCCESS} Kicked:{red} {kicked_count:<6}{white} | User:{red} {username}", reset)
        elif response.status_code == 429:
            print(f"{ERROR} Status:{red} Limited {white}| User:{red} {username}", reset)
            time.sleep(2)
        else:
            print(f"{ERROR} Status:{red} Failed  {white}| User:{red} {username}", reset)

        time.sleep(delay)

    print(f"{INFO} Total kicked:{red} {kicked_count}/{len(members)}", reset)

    Continue()
    Reset()

except Exception as e:
    Error(e)