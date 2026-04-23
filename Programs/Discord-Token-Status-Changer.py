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

Title("Token Status Changer")
Connection()

Scroll(GradientBanner(discord_banner))

try:
    token      = ChoiceToken()
    new_status = input(f"{INPUT} Status {red}->{reset} ").strip()

    print(f"{LOADING} Changing..", reset)

    headers  = {"Authorization": token, "Content-Type": "application/json", "User-Agent": RandomUserAgents()}
    response = requests.patch("https://discord.com/api/v9/users/@me/settings", headers=headers, json={"custom_status": {"text": new_status}})

    if response.status_code == 200:
        print(f"{SUCCESS} Status changed!", reset)
    else:
        print(f"{ERROR} Could not change status!", reset)

    Continue()
    Reset()

except Exception as e:
    Error(e)