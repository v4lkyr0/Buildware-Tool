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

Title("Token Joiner")
Connection()

Scroll(GradientBanner(discord_banner))

try:
    token = ChoiceToken()

    invite = input(f"{INPUT} Invite {red}->{reset} ").strip()
    if not invite:
        ErrorInput()

    invite_code = invite.split("/")[-1]

    print(f"{LOADING} Joining..", reset)

    headers  = {"Authorization": token, "User-Agent": RandomUserAgents()}
    response = requests.post(f"https://discord.com/api/v9/invites/{invite_code}", headers=headers)

    if response.status_code == 200:
        print(f"{SUCCESS} Joined!", reset)
    else:
        print(f"{ERROR} Could not join server!", reset)

    Continue()
    Reset()

except Exception as e:
    Error(e)