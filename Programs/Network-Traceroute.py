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
    from icmplib import traceroute
    import socket
except Exception as e:
    MissingModule(e)

Title("Traceroute")
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

    print(f"{LOADING} Tracerouting..", reset)

    try:
        hops = traceroute(resolved, max_hops=30, timeout=2, privileged=False)
        for hop in hops:
            if hop.is_alive:
                print(f"{SUCCESS} Hop:{red} {hop.distance:<3}{white} | IP:{red} {hop.address:<16}{white} | Time:{red} {hop.avg_rtt}ms", reset)
            else:
                print(f"{ERROR} Hop:{red} {hop.distance:<3}{white} | {red}* * * Request timed out.", reset)
    except:
        print(f"{ERROR} Traceroute failed!", reset)

    Continue()
    Reset()

except Exception as e:
    Error(e)