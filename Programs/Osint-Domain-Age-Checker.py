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
    from datetime import datetime, timezone
except Exception as e:
    MissingModule(e)

Title("Domain Age Checker")
Connection()

Scroll(GradientBanner(osint_banner))

def WhoisQuery(domain, server="whois.iana.org"):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(10)
        sock.connect((server, 43))
        sock.send((domain + "\r\n").encode())
        response = b""
        while True:
            data = sock.recv(4096)
            if not data:
                break
            response += data
        sock.close()
        return response.decode(errors="ignore")
    except:
        return ""

def GetWhoisServer(domain):
    response = WhoisQuery(domain)
    for line in response.splitlines():
        if "whois:" in line.lower():
            return line.split(":")[-1].strip()
    return None

def ParseDate(response, keys):
    for key in keys:
        for line in response.splitlines():
            if key.lower() in line.lower():
                date_str = line.split(":", 1)[-1].strip()[:19]
                for fmt in ["%Y-%m-%dT%H:%M:%S", "%Y-%m-%d %H:%M:%S", "%Y-%m-%d", "%d/%m/%Y"]:
                    try:
                        return datetime.strptime(date_str, fmt)
                    except:
                        pass
    return None

def ParseField(response, keys):
    for key in keys:
        for line in response.splitlines():
            if key.lower() in line.lower():
                value = line.split(":", 1)[-1].strip()
                if value:
                    return value
    return "None"

def RdapLookup(domain):
    try:
        r = requests.get(f"https://rdap.org/domain/{domain}", timeout=10)
        if r.status_code != 200:
            return None
        data    = r.json()
        events  = {e["eventAction"]: e["eventDate"][:10] for e in data.get("events", [])}
        notices = data.get("entities", [{}])[0]
        return {
            "created"  : events.get("registration", "None"),
            "expires"  : events.get("expiration",   "None"),
            "updated"  : events.get("last changed", "None"),
            "registrar": notices.get("vcardArray", [[]])[1][1][3] if notices.get("vcardArray") else "None",
            "status"   : ", ".join(data.get("status", [])) or "None",
        }
    except:
        return None

try:
    target = input(f"{INPUT} Domain {red}->{reset} ").strip()

    if not target:
        ErrorInput()

    print(f"{LOADING} Checking..", reset)

    created   = None
    expires   = None
    updated   = None
    registrar = "None"
    status    = "None"

    whois_server = GetWhoisServer(target)

    if whois_server:
        response  = WhoisQuery(target, whois_server)
        created   = ParseDate(response,  ["Creation Date", "Created On", "created:", "Registration Date"])
        expires   = ParseDate(response,  ["Registry Expiry Date", "Expiry Date", "Expiration Date", "expires:"])
        updated   = ParseDate(response,  ["Updated Date", "Last Modified", "last-modified:"])
        registrar = ParseField(response, ["Registrar:"])
        status    = ParseField(response, ["Domain Status:"])

    if not created:
        print(f"{LOADING} Trying RDAP..", reset)
        rdap = RdapLookup(target)
        if rdap:
            try:
                created   = datetime.strptime(rdap["created"], "%Y-%m-%d") if rdap["created"] != "None" else None
                expires   = datetime.strptime(rdap["expires"], "%Y-%m-%d") if rdap["expires"] != "None" else None
                updated   = datetime.strptime(rdap["updated"], "%Y-%m-%d") if rdap["updated"] != "None" else None
                registrar = rdap["registrar"]
                status    = rdap["status"]
            except:
                pass

    if not created:
        print(f"{ERROR} Could not fetch domain information!", reset)
        Continue()
        Reset()

    age_days  = (datetime.now() - created).days
    age_years = round(age_days / 365, 1)

    Scroll(f"""
 {SUCCESS} Domain    :{red} {target}{white}
 {SUCCESS} Created   :{red} {created.strftime('%Y-%m-%d') if created else 'None'}{white}
 {SUCCESS} Expires   :{red} {expires.strftime('%Y-%m-%d') if expires else 'None'}{white}
 {SUCCESS} Updated   :{red} {updated.strftime('%Y-%m-%d') if updated else 'None'}{white}
 {SUCCESS} Age       :{red} {age_years} years ({age_days} days){white}
 {SUCCESS} Registrar :{red} {registrar}{white}
 {SUCCESS} Status    :{red} {status}{white}
""")

    Continue()
    Reset()

except Exception as e:
    Error(e)