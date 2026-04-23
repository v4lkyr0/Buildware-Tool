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

Title("Http Headers")
Connection()

Scroll(GradientBanner(network_banner))

security_headers = {
    "Strict-Transport-Security" : "HSTS",
    "Content-Security-Policy"   : "CSP",
    "X-Frame-Options"           : "Clickjacking",
    "X-Content-Type-Options"    : "MIME Sniffing",
    "Referrer-Policy"           : "Referrer",
    "Permissions-Policy"        : "Permissions",
    "X-XSS-Protection"          : "XSS Protection",
    "Cross-Origin-Opener-Policy": "COOP",
    "Cross-Origin-Embedder-Policy": "COEP",
}

try:
    target = input(f"{INPUT} Url {red}->{reset} ").strip()

    if not target:
        ErrorInput()

    if not target.startswith("http://") and not target.startswith("https://"):
        target = "https://" + target

    print(f"{LOADING} Fetching..", reset)

    try:
        response = requests.get(target, timeout=10, allow_redirects=True)
        headers  = response.headers

        for key, value in headers.items():
            print(f"{SUCCESS} {key:<40}{red}:{white} {value}", reset)
    except:
        print(f"{ERROR} Could not fetch headers!", reset)

    Continue()
    Reset()

except Exception as e:
    Error(e)