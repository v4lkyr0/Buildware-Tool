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
    from icmplib import ping as icmp_ping
except Exception as e:
    MissingModule(e)

Title("Ip Pinger")
Connection()

Scroll(GradientBanner(network_banner))

try:
    target = input(f"{INPUT} Target {red}->{reset} ").strip()
    if not target:
        ErrorInput()

    target = target.replace("http://", "").replace("https://", "").split("/")[0]

    count_input = input(f"{INPUT} Number of Pings {red}->{reset} ").strip()
    try:
        count = int(count_input) if count_input else 4
    except ValueError:
        count = 4

    if count < 1 or count > 100:
        ErrorNumber()

    print(f"{LOADING} Pinging Target..", reset)

    try:
        result = icmp_ping(target, count=count, timeout=2, privileged=False)

        Scroll(f"""
 {INFO} Target                   :{red} {result.address}
 {INFO} Packets Sent             :{red} {result.packets_sent}
 {INFO} Packets Received         :{red} {result.packets_received}
 {INFO} Packet Loss              :{red} {result.packet_loss * 100:.1f}%
 {INFO} Min RTT                  :{red} {result.min_rtt:.2f} ms
 {INFO} Avg RTT                  :{red} {result.avg_rtt:.2f} ms
 {INFO} Max RTT                  :{red} {result.max_rtt:.2f} ms
 {INFO} Jitter                   :{red} {result.jitter:.2f} ms
""")

        if result.is_alive:
            print(f"{SUCCESS} Host is reachable!", reset)
        else:
            print(f"{ERROR} Host is unreachable!", reset)

    except Exception as e:
        print(f"{ERROR} Ping failed:{red} {e}", reset)

    Continue()
    Reset()

except Exception as e:
    Error(e)
