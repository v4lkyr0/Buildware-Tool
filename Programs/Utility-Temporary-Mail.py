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
    import random
    import string
    import time
except Exception as e:
    MissingModule(e)

Title("Temporary Mail")
Connection()

Scroll(GradientBanner(utilities_banner))

api_base = "https://api.mail.tm"

def GetDomain():
    response = requests.get(f"{api_base}/domains", timeout=10)
    domains  = response.json().get("hydra:member", [])
    if not domains:
        return None
    return domains[0]["domain"]

def CreateAccount(domain):
    user     = "".join(random.choices(string.ascii_lowercase + string.digits, k=10))
    address  = f"{user}@{domain}"
    password = "".join(random.choices(string.ascii_letters + string.digits, k=16))
    response = requests.post(f"{api_base}/accounts", json={"address": address, "password": password}, timeout=10)
    if response.status_code != 201:
        return None, None
    return address, password

def GetToken(address, password):
    response = requests.post(f"{api_base}/token", json={"address": address, "password": password}, timeout=10)
    if response.status_code != 200:
        return None
    return response.json().get("token")

def GetMessages(token):
    headers  = {"Authorization": f"Bearer {token}"}
    response = requests.get(f"{api_base}/messages", headers=headers, timeout=10)
    if response.status_code != 200:
        return []
    return response.json().get("hydra:member", [])

def GetMessage(token, msg_id):
    headers  = {"Authorization": f"Bearer {token}"}
    response = requests.get(f"{api_base}/messages/{msg_id}", headers=headers, timeout=10)
    if response.status_code != 200:
        return None
    return response.json()

def DisplayMessages(token):
    messages = GetMessages(token)
    if not messages:
        return 0
    for msg in messages:
        detail = GetMessage(token, msg.get("id"))
        if not detail:
            continue
        sender = detail.get("from", {})
        sender = sender.get("address", "None") if isinstance(sender, dict) else str(sender)
        body   = detail.get("text", detail.get("intro", "None")) or "None"
        if len(body) > 500:
            body = body[:500] + "..."
        Scroll(f"""
 {SUCCESS} From    :{red} {sender}{white}
 {SUCCESS} Subject :{red} {detail.get('subject', 'None')}{white}
 {SUCCESS} Date    :{red} {detail.get('createdAt', 'None')[:19].replace('T', ' ')}{white}
 {SUCCESS} Body    :{red} {body}{white}
""")
    return len(messages)

try:
    Scroll(f"""
 {PREFIX}01{SUFFIX} New Email
 {PREFIX}02{SUFFIX} Check Messages
""")

    choice = input(f"{INPUT} Choice {red}->{reset} ").strip().lstrip("0")

    if choice == "1":
        print(f"{LOADING} Generating..", reset)

        domain = GetDomain()
        if not domain:
            print(f"{ERROR} Could not fetch domain!", reset)
            Continue()
            Reset()

        address, password = CreateAccount(domain)
        if not address:
            print(f"{ERROR} Could not create email!", reset)
            Continue()
            Reset()

        token = GetToken(address, password)

        Scroll(f"""
 {SUCCESS} Email    :{red} {address}{white}
 {SUCCESS} Password :{red} {password}{white}
""")

        print(f"{INFO} Waiting for messages.. Press{red} Ctrl+C{white} to stop.", reset)

        seen     = set()
        interval = 10

        try:
            while True:
                messages = GetMessages(token)
                for msg in messages:
                    msg_id = msg.get("id")
                    if msg_id not in seen:
                        seen.add(msg_id)
                        detail = GetMessage(token, msg_id)
                        if not detail:
                            continue
                        sender = detail.get("from", {})
                        sender = sender.get("address", "None") if isinstance(sender, dict) else str(sender)
                        body   = detail.get("text", detail.get("intro", "None")) or "None"
                        if len(body) > 500:
                            body = body[:500] + "..."
                        print(f"\n{SUCCESS} New message!", reset)
                        Scroll(f"""
 {SUCCESS} From    :{red} {sender}{white}
 {SUCCESS} Subject :{red} {detail.get('subject', 'None')}{white}
 {SUCCESS} Date    :{red} {detail.get('createdAt', 'None')[:19].replace('T', ' ')}{white}
 {SUCCESS} Body    :{red} {body}{white}
""")
                time.sleep(interval)
        except KeyboardInterrupt:
            print(f"\n{INFO} Stopped.", reset)

    elif choice == "2":
        address  = input(f"{INPUT} Email {red}->{reset} ").strip()
        if not address or "@" not in address:
            ErrorInput()

        password = input(f"{INPUT} Password {red}->{reset} ").strip()
        if not password:
            ErrorInput()

        print(f"{LOADING} Authenticating..", reset)

        token = GetToken(address, password)
        if not token:
            print(f"{ERROR} Authentication failed!", reset)
            Continue()
            Reset()

        print(f"{INFO} Checking messages.. {red}({white}Ctrl+C to Stop{red})", reset)

        seen     = set()
        interval = 10

        try:
            while True:
                messages = GetMessages(token)
                new      = [m for m in messages if m.get("id") not in seen]
                if new:
                    for msg in new:
                        msg_id = msg.get("id")
                        seen.add(msg_id)
                        detail = GetMessage(token, msg_id)
                        if not detail:
                            continue
                        sender = detail.get("from", {})
                        sender = sender.get("address", "None") if isinstance(sender, dict) else str(sender)
                        body   = detail.get("text", detail.get("intro", "None")) or "None"
                        if len(body) > 500:
                            body = body[:500] + "..."
                        Scroll(f"""
 {SUCCESS} From    :{red} {sender}{white}
 {SUCCESS} Subject :{red} {detail.get('subject', 'None')}{white}
 {SUCCESS} Date    :{red} {detail.get('createdAt', 'None')[:19].replace('T', ' ')}{white}
 {SUCCESS} Body    :{red} {body}{white}
""")
                elif not seen:
                    print(f"{INFO} No messages yet..", reset)
                time.sleep(interval)
        except KeyboardInterrupt:
            print(f"\n{INFO} Stopped.", reset)

    else:
        ErrorChoice()

    Continue()
    Reset()

except Exception as e:
    Error(e)