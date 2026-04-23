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
    import hashlib
except Exception as e:
    MissingModule(e)

Title("Email Breach Checker")
Connection()

Scroll(GradientBanner(osint_banner))

try:
    email = input(f"{INPUT} Email {red}->{reset} ").strip()

    if not email or "@" not in email or "." not in email:
        print(f"{ERROR} Invalid email!", reset)
        Continue()
        Reset()

    print(f"{LOADING} Checking..", reset)

    found    = False
    sources  = []

    try:
        headers  = {"User-Agent": RandomUserAgents()}
        response = requests.get(
            f"https://leakcheck.io/api/public?check={email}",
            headers=headers,
            timeout=10
        )
        if response.status_code == 200:
            data = response.json()
            if data.get("success") and data.get("found", 0) > 0:
                found = True
                sources.append({
                    "source" : "LeakCheck.io",
                    "found"  : data.get("found", 0),
                    "fields" : ", ".join(data.get("fields", [])) or "Unknown",
                    "sources": ", ".join(data.get("sources", [])) or "Unknown",
                })
    except:
        pass

    try:
        headers  = {"User-Agent": RandomUserAgents()}
        response = requests.get(
            f"https://intelx.io/phonebook/search?term={email}&k=&maxresults=1&media=0&terminate=[]&timeout=20",
            headers=headers,
            timeout=10
        )
        if response.status_code == 200:
            data = response.json()
            if data.get("selectors") and len(data["selectors"]) > 0:
                found = True
                sources.append({
                    "source" : "IntelX",
                    "found"  : len(data["selectors"]),
                    "fields" : "Email",
                    "sources": "IntelX Database",
                })
    except:
        pass

    try:
        headers  = {
            "User-Agent"   : RandomUserAgents(),
            "X-RapidAPI-Host": "breachdirectory.p.rapidapi.com",
        }
        response = requests.get(
            f"https://breachdirectory.org/api?func=auto&term={email}",
            headers=headers,
            timeout=10
        )
        if response.status_code == 200:
            data = response.json()
            if data.get("success") and data.get("result"):
                found = True
                sources.append({
                    "source" : "BreachDirectory",
                    "found"  : len(data["result"]),
                    "fields" : "Password hash",
                    "sources": "BreachDirectory Database",
                })
    except:
        pass

    if found:
        total = sum(s["found"] for s in sources)
        print(f"{ERROR} Found in{red} {total}{white} breach(es) across{red} {len(sources)}{white} source(s)!\n", reset)
        for s in sources:
            Scroll(f"""
 {SUCCESS} Source  :{red} {s['source']}{white}
 {SUCCESS} Found   :{red} {s['found']}{white}
 {SUCCESS} Fields  :{red} {s['fields']}{white}
 {SUCCESS} Sources :{red} {s['sources']}{white}""")
    else:
        print(f"{SUCCESS} No breaches found!", reset)

    Continue()
    Reset()

except Exception as e:
    Error(e)