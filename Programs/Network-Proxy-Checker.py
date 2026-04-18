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

Title("Proxy Checker")
Connection()

Scroll(GradientBanner(network_banner))

try:
    proxies_list = []
    while True:
        proxy = input(f"{INPUT} Proxy {red}->{reset} ").strip()
        if not proxy:
            break
        proxies_list.append(proxy)

    if not proxies_list:
        ErrorInput()

    test_url = "http://httpbin.org/ip"

    print(f"{LOADING} Checking Proxies..", reset)

    working = 0
    output = ""

    for proxy in proxies_list:
        if "://" not in proxy:
            proxy_dict = {"http": f"http://{proxy}", "https": f"http://{proxy}"}
        else:
            proxy_dict = {"http": proxy, "https": proxy}

        try:
            start = time.time()
            response = requests.get(test_url, proxies=proxy_dict, timeout=10)
            elapsed = time.time() - start

            if response.status_code == 200:
                external_ip = response.json().get("origin", "Unknown")
                output += f"{SUCCESS} Status:{red} Working {white}| Ip:{red} {external_ip:15s}{white}| Speed:{red} {elapsed:.2f}s {white}| Proxy:{red} {proxy}{reset}\n"
                working += 1
            else:
                output += f"{ERROR} Status:{red} Failed  {white}| Proxy:{red} {proxy}{reset}\n"

        except requests.exceptions.ProxyError:
            output += f"{ERROR} Status:{red} Error   {white}| Proxy:{red} {proxy}{reset}\n"
        except requests.exceptions.Timeout:
            output += f"{ERROR} Status:{red} Timeout {white}| Proxy:{red} {proxy}{reset}\n"
        except Exception:
            output += f"{ERROR} Status:{red} Error   {white}| Proxy:{red} {proxy}{reset}\n"

    output += f"\n{INFO} Total working:{red} {working}/{len(proxies_list)}{reset}\n"

    Scroll(f"\n{output}")

    Continue()
    Reset()

except Exception as e:
    Error(e)
