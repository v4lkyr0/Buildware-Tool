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

    print(f"{LOADING} Looking Up Mac Address..", reset)

    response = requests.get(f"https://api.macvendors.com/{mac}", timeout=10)

    if response.status_code == 200:
        vendor = response.text.strip()
        mac_clean = mac.upper().replace("-", ":").replace(".", ":")
        oui = ":".join(mac_clean.split(":")[:3]) if ":" in mac_clean else mac_clean[:8]

        Scroll(f"""
 {INFO} Mac Address              :{red} {mac}
 {INFO} Normalized               :{red} {mac_clean}
 {INFO} Oui Prefix               :{red} {oui}
 {INFO} Vendor / Manufacturer    :{red} {vendor}
""")
    elif response.status_code == 404:
        print(f" {ERROR} Mac Address not found in Vendor Database!", reset)
        print(f" {INFO} This could be a randomized or private Mac Address", reset)
    else:
        print(f" {ERROR} Lookup failed!", reset)

    Continue()
    Reset()

except Exception as e:
    Error(e)
