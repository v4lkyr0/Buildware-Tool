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

Title("Bandwidth Tester")
Connection()

Scroll(GradientBanner(network_banner))

try:
    print(f"{LOADING} Testing..", reset)

    servers = [
        ("Tele2",      "http://speedtest.tele2.net/10MB.zip"),
        ("Bouygues",   "http://speedtest.bouyguestelecom.fr/files/10M.bin"),
        ("Scaleway",   "http://ping.online.net/10Mo.dat"),
    ]

    download  = None
    size      = None
    elapsed   = None
    used      = None

    for name, url in servers:
        try:
            start    = time.time()
            response = requests.get(url, stream=True, timeout=20)
            total    = 0

            for chunk in response.iter_content(chunk_size=8192):
                total += len(chunk)

            elapsed  = time.time() - start
            download = round((total * 8) / (elapsed * 1_000_000), 2)
            size     = total
            used     = name
            break
        except:
            continue

    if download is not None:
        Scroll(f"""
 {SUCCESS} Download :{red} {download} Mbps{white}
 {SUCCESS} Size     :{red} {round(size / 1_000_000, 2)} MB{white}
 {SUCCESS} Time     :{red} {round(elapsed, 2)} s{white}
 {SUCCESS} Server   :{red} {used}{white}
""")
    else:
        print(f"{ERROR} All servers failed!", reset)

    Continue()
    Reset()

except Exception as e:
    Error(e)