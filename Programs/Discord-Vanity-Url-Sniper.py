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

Title("Vanity Url Sniper")
Connection()

Scroll(GradientBanner(discord_banner))

try:
    token = ChoiceToken()

    server_id = input(f"{INPUT} Server Id {red}->{reset} ").strip()
    if not server_id:
        ErrorId()

    vanity_code = input(f"{INPUT} Vanity Code {red}->{reset} ").strip()
    if not vanity_code:
        ErrorInput()

    try:
        delay = float(input(f"{INPUT} Delay {red}->{reset} ").strip())
        if delay < 0.1:
            delay = 0.1
    except:
        delay = 0.5

    headers = {"Authorization": token, "Content-Type": "application/json", "User-Agent": RandomUserAgents()}

    print(f"{LOADING} Fetching server..", reset)

    guild_response = requests.get(f"https://discord.com/api/v9/guilds/{server_id}", headers=headers)

    if guild_response.status_code != 200:
        print(f"{ERROR} Could not access server!", reset)
        Continue()
        Reset()

    guild_name = guild_response.json().get("name", "Unknown")

    print(f"{SUCCESS} Server:{red} {guild_name}", reset)
    print(f"{SUCCESS} Vanity:{red} {vanity_code}", reset)
    print(f"{LOADING} Sniping..", reset)

    attempt = 0

    while True:
        attempt      += 1
        check_response = requests.get(f"https://discord.com/api/v9/invites/{vanity_code}", headers=headers)

        if check_response.status_code == 404:
            print(f"{LOADING} Attempt:{red} {attempt:<6}{white} | Status:{red} Available {white}| Claiming..", reset)

            claim_response = requests.patch(
                f"https://discord.com/api/v9/guilds/{server_id}/vanity-url",
                headers=headers,
                json={"code": vanity_code}
            )

            if claim_response.status_code == 200:
                print(f"{SUCCESS} Vanity url claimed!", reset)
                break
            else:
                print(f"{ERROR} Could not claim vanity url!", reset)
        else:
            print(f"{LOADING} Attempt:{red} {attempt:<6}{white} | Status:{red} Taken", reset)

        time.sleep(delay)

    Continue()
    Reset()

except Exception as e:
    Error(e)