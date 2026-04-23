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
    from datetime import datetime
except Exception as e:
    MissingModule(e)

Title("Cookie Information")
Connection()

Scroll(GradientBanner(roblox_banner))

try:
    cookie  = ChoiceCookie()
    session = requests.Session()
    session.cookies[".ROBLOSECURITY"] = cookie

    print(f"{LOADING} Fetching..", reset)

    auth = session.get("https://users.roblox.com/v1/users/authenticated", timeout=10)

    if auth.status_code != 200:
        print(f"{ERROR} Invalid or expired cookie!", reset)
        Continue()
        Reset()

    auth_data = auth.json()
    user_id   = auth_data.get("id")
    username  = auth_data.get("name", "None")
    user      = requests.get(f"https://users.roblox.com/v1/users/{user_id}", timeout=10).json()

    robux = "None"
    try:
        eco   = session.get(f"https://economy.roblox.com/v1/users/{user_id}/currency", timeout=10).json()
        robux = eco.get("robux", "None")
    except:
        pass

    friends_count = "None"
    try:
        fc            = requests.get(f"https://friends.roblox.com/v1/users/{user_id}/friends/count", timeout=10).json()
        friends_count = fc.get("count", "None")
    except:
        pass

    followers_count = "None"
    try:
        fl              = requests.get(f"https://friends.roblox.com/v1/users/{user_id}/followers/count", timeout=10).json()
        followers_count = fl.get("count", "None")
    except:
        pass

    following_count = "None"
    try:
        fw              = requests.get(f"https://friends.roblox.com/v1/users/{user_id}/followings/count", timeout=10).json()
        following_count = fw.get("count", "None")
    except:
        pass

    groups_count = "None"
    groups_list  = []
    try:
        gr           = requests.get(f"https://groups.roblox.com/v1/users/{user_id}/groups/roles", timeout=10).json()
        groups_data  = gr.get("data", [])
        groups_count = len(groups_data)
        groups_list  = [(g.get("group", {}).get("name", "None"), g.get("role", {}).get("name", "None")) for g in groups_data[:10]]
    except:
        pass

    collectibles_count = "None"
    try:
        inv                = requests.get(f"https://inventory.roblox.com/v1/users/{user_id}/assets/collectibles?limit=10&sortOrder=Desc", timeout=10).json()
        collectibles_count = len(inv.get("data", []))
    except:
        pass

    avatar_url = "None"
    try:
        th         = requests.get(f"https://thumbnails.roblox.com/v1/users/avatar-headshot?userIds={user_id}&size=420x420&format=Png&isCircular=false", timeout=10).json()
        avatar_url = th.get("data", [{}])[0].get("imageUrl", "None")
    except:
        pass

    email_status = "None"
    try:
        settings       = session.get("https://accountsettings.roblox.com/v1/email", timeout=10).json()
        email_verified = settings.get("verified", False)
        email_addr     = settings.get("emailAddress", "None")
        email_status   = f"{email_addr} (Verified: {email_verified})"
    except:
        pass

    pin_status = "None"
    try:
        pin        = session.get("https://auth.roblox.com/v1/account/pin", timeout=10).json()
        pin_status = "Enabled" if pin.get("isEnabled", False) else "Disabled"
    except:
        pass

    presence = "None"
    try:
        pr             = requests.post("https://presence.roblox.com/v1/presence/users", json={"userIds": [user_id]}, timeout=10).json()
        presence_data  = pr.get("userPresences", [{}])[0]
        presence_types = {0: "Offline", 1: "Online", 2: "In-Game", 3: "In Studio"}
        presence       = presence_types.get(presence_data.get("userPresenceType", 0), "Unknown")
        last_location  = presence_data.get("lastLocation", "")
        if last_location:
            presence += f" ({last_location})"
    except:
        pass

    prev_names = []
    try:
        pn         = requests.get(f"https://users.roblox.com/v1/users/{user_id}/username-history?limit=10&sortOrder=Desc", timeout=10).json()
        prev_names = [n.get("name", "") for n in pn.get("data", []) if n.get("name")]
    except:
        pass

    created = user.get("created", "None")
    if created and created != "None":
        try:
            dt      = datetime.fromisoformat(created.replace("Z", "+00:00"))
            created = dt.strftime("%Y-%m-%d %H:%M:%S UTC")
        except:
            created = created[:10]

    Scroll(f"""
 {SUCCESS} Status             :{red} Valid{white}
 {SUCCESS} Cookie             :{red} {cookie[:30]}..{white}
 {SUCCESS} User Id            :{red} {user_id}{white}
 {SUCCESS} Username           :{red} {username}{white}
 {SUCCESS} Display Name       :{red} {user.get('displayName', 'None')}{white}
 {SUCCESS} Bio                :{red} {(user.get('description', 'None') or 'None')[:100]}{white}
 {SUCCESS} Created            :{red} {created}{white}
 {SUCCESS} Banned             :{red} {user.get('isBanned', False)}{white}
 {SUCCESS} Verified Badge     :{red} {user.get('hasVerifiedBadge', False)}{white}
 {SUCCESS} Email              :{red} {email_status}{white}
 {SUCCESS} Pin                :{red} {pin_status}{white}
 {SUCCESS} Presence           :{red} {presence}{white}
 {SUCCESS} Robux              :{red} {robux}{white}
 {SUCCESS} Friends            :{red} {friends_count}{white}
 {SUCCESS} Followers          :{red} {followers_count}{white}
 {SUCCESS} Following          :{red} {following_count}{white}
 {SUCCESS} Groups             :{red} {groups_count}{white}
 {SUCCESS} Collectibles       :{red} {collectibles_count}{white}
 {SUCCESS} Previous Usernames :{red} {', '.join(prev_names) if prev_names else 'None'}{white}
 {SUCCESS} Avatar             :{red} {avatar_url}{white}
 {SUCCESS} Profile            :{red} https://www.roblox.com/users/{user_id}/profile{white}
""")

    if groups_list:
        print(f"{INFO} Top Groups:", reset)
        for name, role in groups_list:
            print(f"{SUCCESS} {red}{name}{white} | Role:{red} {role}", reset)

    Continue()
    Reset()

except Exception as e:
    Error(e)