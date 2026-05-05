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

Scroll(GradientBanner(network_banner))

try:
    target = input(f"{INPUT} Host {red}->{reset} ").strip()

    if not target:
        ErrorInput()

    target = target.removeprefix("https://").removeprefix("http://").rstrip("/")

    try:
        resolved = socket.gethostbyname(target)
    except Exception:
        print(f"{ERROR} Could not resolve host!", reset)
        Continue()
        Reset()

    try:
        count = int(input(f"{INPUT} Number of Pings {red}->{reset} ").strip())
        if count < 1:
            ErrorNumber()
    except Exception:
        ErrorNumber()

    print(f"{LOADING} Pinging..", reset)

    success_count = 0
    failed_count  = 0
    rtt_list      = []

    for i in range(count):
        try:
            result = ping(resolved, count=1, timeout=2, privileged=False)
            if result.is_alive:
                success_count += 1
                rtt_list.append(result.avg_rtt)
                print(f"{SUCCESS} Reply from:{red} {resolved}{white} | Time:{red} {round(result.avg_rtt, 2)}ms", reset)
            else:
                failed_count += 1
                print(f"{ERROR} Request timed out!", reset)
        except Exception:
            failed_count += 1
            print(f"{ERROR} Request timed out!", reset)

    if rtt_list:
        Scroll(f"""
 {SUCCESS} Host    :{red} {resolved}{white}
 {SUCCESS} Sent    :{red} {count}{white}
 {SUCCESS} Success :{red} {success_count}{white}
 {SUCCESS} Failed  :{red} {failed_count}{white}
 {SUCCESS} Min     :{red} {round(min(rtt_list), 2)}ms{white}
 {SUCCESS} Max     :{red} {round(max(rtt_list), 2)}ms{white}
 {SUCCESS} Avg     :{red} {round(sum(rtt_list) / len(rtt_list), 2)}ms{white}
""")

    Continue()
    Reset()

except Exception as e:
    Error(e)