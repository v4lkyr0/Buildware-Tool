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

Title("Mac Lookup")
Connection()

Scroll(GradientBanner(network_banner))

try:
    mac = input(f"{INPUT} Mac Address {red}->{reset} ").strip()

    if not mac:
        ErrorInput()

    print(f"{LOADING} Looking up..", reset)

    try:
        response = requests.get(f"https://api.macvendors.com/{mac}", timeout=5)
        if response.status_code == 200:
            print(f"{SUCCESS} Vendor:{red} {response.text}", reset)
        else:
            print(f"{ERROR} Mac Address not found!", reset)
    except:
        print(f"{ERROR} Mac Address not found!", reset)

    Continue()
    Reset()

except Exception as e:
    Error(e)