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
    import threading
except Exception as e:
    MissingModule(e)

Title("Network Scanner")
Connection()

Scroll(GradientBanner(network_banner))

try:
    target = input(f"{INPUT} Host {red}->{reset} ").strip()

    if not target:
        ErrorInput()

    try:
        base = ".".join(socket.gethostbyname(target).split(".")[:3])
    except:
        print(f"{ERROR} Could not resolve host!", reset)
        Continue()
        Reset()

    print(f"{LOADING} Scanning..", reset)

    hosts  = []
    lock   = threading.Lock()
    semaphore = threading.Semaphore(50)

    def ScanHost(ip):
        with semaphore:
            try:
                result = ping(ip, count=1, timeout=1, privileged=False)
                if result.is_alive:
                    try:
                        hostname = socket.gethostbyaddr(ip)[0]
                    except:
                        hostname = "Unknown"
                    with lock:
                        hosts.append(ip)
                        print(f"{SUCCESS} Host:{red} {ip:<16}{white} | Hostname:{red} {hostname}", reset)
            except:
                pass

    threads = []
    for i in range(1, 255):
        ip = f"{base}.{i}"
        t  = threading.Thread(target=ScanHost, args=(ip,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    Continue()
    Reset()

except Exception as e:
    Error(e)