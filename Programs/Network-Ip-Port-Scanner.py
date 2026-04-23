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
    import threading
except Exception as e:
    MissingModule(e)

Title("Ip Port Scanner")
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

    Scroll(f"""
 {PREFIX}01{SUFFIX} Common Ports
 {PREFIX}02{SUFFIX} Full Scan
 {PREFIX}03{SUFFIX} Custom Range
""")

    choice = input(f"{INPUT} Choice {red}->{reset} ").strip().lstrip("0")

    common_ports = [21, 22, 23, 25, 53, 80, 110, 135, 139, 143, 443, 445, 3306, 3389, 5900, 8080, 8443, 8888, 9090, 27017]

    if choice == "1":
        ports = common_ports
    elif choice == "2":
        ports = range(1, 65536)
    elif choice == "3":
        try:
            start = int(input(f"{INPUT} Start Port {red}->{reset} ").strip())
            end   = int(input(f"{INPUT} End Port {red}->{reset} ").strip())
            if start < 1 or end > 65535 or start > end:
                ErrorNumber()
            ports = range(start, end + 1)
        except ValueError:
            ErrorNumber()
    else:
        ErrorChoice()

    print(f"{LOADING} Scanning..", reset)

    open_ports = []
    lock       = threading.Lock()
    semaphore  = threading.Semaphore(200)

    def ScanPort(port):
        with semaphore:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(0.5)
                result = sock.connect_ex((resolved, port))
                sock.close()
                if result == 0:
                    try:
                        service = socket.getservbyport(port)
                    except:
                        service = "Unknown"
                    with lock:
                        open_ports.append((port, service))
                        print(f"{SUCCESS} Port:{red} {port}{white} | Service:{red} {service}", reset)
            except:
                pass

    threads = []
    for port in ports:
        t = threading.Thread(target=ScanPort, args=(port,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    Continue()
    Reset()

except Exception as e:
    Error(e)