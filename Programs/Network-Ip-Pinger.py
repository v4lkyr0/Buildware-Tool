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
    from icmplib import ping
    import socket
except Exception as e:
    MissingModule(e)

Title("Ip Pinger")
Connection()

Scroll(GradientBanner(network_banner))

try:
    target = input(f"{INPUT} Host {red}->{reset} ").strip()

    if not target:
        ErrorInput()

    try:
        resolved = socket.gethostbyname(target)
    except:
        print(f"{ERROR} Could not resolve host!", reset)
        Continue()
        Reset()

    try:
        count = int(input(f"{INPUT} Number of Ping {red}->{reset} ").strip())
        if count < 1:
            ErrorNumber()
    except ValueError:
        ErrorNumber()

    print(f"{LOADING} Pinging..", reset)

    for i in range(count):
        try:
            result = ping(resolved, count=1, timeout=2, privileged=False)
            if result.is_alive:
                print(f"{SUCCESS} Reply from:{red} {resolved}{white} | Time:{red} {result.avg_rtt}ms", reset)
            else:
                print(f"{ERROR} Request timed out!", reset)
        except:
            print(f"{ERROR} Request timed out!", reset)

    Continue()
    Reset()

except Exception as e:
    Error(e)