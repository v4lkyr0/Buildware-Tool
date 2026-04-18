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
    import socket
except Exception as e:
    MissingModule(e)

Title("Reverse Dns")
Connection()

Scroll(GradientBanner(network_banner))

try:
    ip = input(f"{INPUT} Ip Address {red}->{reset} ").strip()
    if not ip:
        ErrorInput()

    print(f"{LOADING} Performing Reverse Dns Lookup..", reset)

    try:
        hostname, aliases, addresses = socket.gethostbyaddr(ip)

        Scroll(f"""
 {INFO} Ip Address               :{red} {ip}
 {INFO} Hostname                 :{red} {hostname}
 {INFO} Aliases                  :{red} {', '.join(aliases) if aliases else 'None'}
 {INFO} Addresses                :{red} {', '.join(addresses) if addresses else 'None'}
""")

    except socket.herror:
        print(f" {ERROR} No Reverse Dns Record found!", reset)
    except socket.gaierror:
        print(f" {ERROR} Invalid Ip Address format!", reset)

    Continue()
    Reset()

except Exception as e:
    Error(e)
