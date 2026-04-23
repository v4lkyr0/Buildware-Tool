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
    import platform
    import psutil
    import socket
except Exception as e:
    MissingModule(e)

Title("System Information")
Connection()

Scroll(GradientBanner(utilities_banner))

try:
    print(f"{LOADING} Fetching..", reset)

    cpu_count   = psutil.cpu_count(logical=True)
    cpu_freq    = psutil.cpu_freq()
    cpu_usage   = psutil.cpu_percent(interval=1)
    ram         = psutil.virtual_memory()
    disk        = psutil.disk_usage("/")
    hostname    = socket.gethostname()
    local_ip    = socket.gethostbyname(hostname)

    Scroll(f"""
 {SUCCESS} Os         :{red} {platform.system()} {platform.release()}{white}
 {SUCCESS} Machine    :{red} {platform.machine()}{white}
 {SUCCESS} Processor  :{red} {platform.processor()}{white}
 {SUCCESS} Hostname   :{red} {hostname}{white}
 {SUCCESS} Local Ip   :{red} {local_ip}{white}
 {SUCCESS} Username   :{red} {username_pc}{white}
 {SUCCESS} Cpu Cores  :{red} {cpu_count}{white}
 {SUCCESS} Cpu Freq   :{red} {round(cpu_freq.current, 2)} Mhz{white}
 {SUCCESS} Cpu Usage  :{red} {cpu_usage}%{white}
 {SUCCESS} Ram Total  :{red} {round(ram.total / 1_073_741_824, 2)} Gb{white}
 {SUCCESS} Ram Used   :{red} {round(ram.used / 1_073_741_824, 2)} Gb{white}
 {SUCCESS} Ram Free   :{red} {round(ram.available / 1_073_741_824, 2)} Gb{white}
 {SUCCESS} Disk Total :{red} {round(disk.total / 1_073_741_824, 2)} Gb{white}
 {SUCCESS} Disk Used  :{red} {round(disk.used / 1_073_741_824, 2)} Gb{white}
 {SUCCESS} Disk Free  :{red} {round(disk.free / 1_073_741_824, 2)} Gb{white}
""")

    Continue()
    Reset()

except Exception as e:
    Error(e)