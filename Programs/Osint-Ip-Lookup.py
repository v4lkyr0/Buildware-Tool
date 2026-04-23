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
    import socket
except Exception as e:
    MissingModule(e)

Title("Ip Lookup")
Connection()

Scroll(GradientBanner(osint_banner))

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

    print(f"{LOADING} Looking up..", reset)

    try:
        response = requests.get(
            f"http://ip-api.com/json/{resolved}?fields=status,message,country,countryCode,region,regionName,city,zip,lat,lon,timezone,isp,org,as,asname,reverse,mobile,proxy,hosting,query",
            timeout=10
        )
        data = response.json()

        if data.get("status") == "success":
            proxy_type = []
            if data.get("proxy"):
                proxy_type.append("Proxy")
            if data.get("hosting"):
                proxy_type.append("Hosting/VPN")
            if data.get("mobile"):
                proxy_type.append("Mobile")
            proxy_str = ", ".join(proxy_type) if proxy_type else "None"

            Scroll(f"""
 {SUCCESS} Ip          :{red} {data.get('query',      'None')}{white}
 {SUCCESS} Country     :{red} {data.get('country',    'None')} ({data.get('countryCode', 'None')}){white}
 {SUCCESS} Region      :{red} {data.get('regionName', 'None')}{white}
 {SUCCESS} City        :{red} {data.get('city',       'None')}{white}
 {SUCCESS} Zip         :{red} {data.get('zip',        'None')}{white}
 {SUCCESS} Latitude    :{red} {data.get('lat',        'None')}{white}
 {SUCCESS} Longitude   :{red} {data.get('lon',        'None')}{white}
 {SUCCESS} Timezone    :{red} {data.get('timezone',   'None')}{white}
 {SUCCESS} Isp         :{red} {data.get('isp',        'None')}{white}
 {SUCCESS} Org         :{red} {data.get('org',        'None')}{white}
 {SUCCESS} As          :{red} {data.get('as',         'None')}{white}
 {SUCCESS} As Name     :{red} {data.get('asname',     'None')}{white}
 {SUCCESS} Reverse Dns :{red} {data.get('reverse',    'None')}{white}
 {SUCCESS} Type        :{red} {proxy_str}{white}
""")
        else:
            print(f"{ERROR} Ip not found!", reset)

    except:
        print(f"{ERROR} Could not fetch Ip information!", reset)

    Continue()
    Reset()

except Exception as e:
    Error(e)