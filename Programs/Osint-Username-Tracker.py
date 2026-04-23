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
    import threading
except Exception as e:
    MissingModule(e)

Title("Username Tracker")
Connection()

Scroll(GradientBanner(osint_banner))

try:
    username  = input(f"{INPUT} Username {red}->{reset} ").strip()

    if not username:
        ErrorInput()

    print(f"{LOADING} Tracking..", reset)

    sites = {
        "GitHub"        : f"https://github.com/{username}",
        "GitLab"        : f"https://gitlab.com/{username}",
        "X"             : f"https://x.com/{username}",
        "Instagram"     : f"https://www.instagram.com/{username}",
        "TikTok"        : f"https://www.tiktok.com/@{username}",
        "Reddit"        : f"https://www.reddit.com/user/{username}",
        "Pinterest"     : f"https://www.pinterest.com/{username}",
        "Twitch"        : f"https://www.twitch.tv/{username}",
        "YouTube"       : f"https://www.youtube.com/@{username}",
        "Soundcloud"    : f"https://soundcloud.com/{username}",
        "Steam"         : f"https://steamcommunity.com/id/{username}",
        "Patreon"       : f"https://www.patreon.com/{username}",
        "Keybase"       : f"https://keybase.io/{username}",
        "Dev.to"        : f"https://dev.to/{username}",
        "Medium"        : f"https://medium.com/@{username}",
        "Hackerrank"    : f"https://www.hackerrank.com/{username}",
        "Leetcode"      : f"https://leetcode.com/{username}",
        "Codecademy"    : f"https://www.codecademy.com/profiles/{username}",
        "Replit"        : f"https://replit.com/@{username}",
        "Producthunt"   : f"https://www.producthunt.com/@{username}",
        "Flickr"        : f"https://www.flickr.com/people/{username}",
        "Vimeo"         : f"https://vimeo.com/{username}",
        "Dailymotion"   : f"https://www.dailymotion.com/{username}",
        "Mixcloud"      : f"https://www.mixcloud.com/{username}",
        "Bandcamp"      : f"https://{username}.bandcamp.com",
        "Behance"       : f"https://www.behance.net/{username}",
        "Dribbble"      : f"https://dribbble.com/{username}",
        "Deviantart"    : f"https://www.deviantart.com/{username}",
        "500px"         : f"https://500px.com/p/{username}",
        "Unsplash"      : f"https://unsplash.com/@{username}",
    }

    found     = []
    lock      = threading.Lock()
    semaphore = threading.Semaphore(20)

    def CheckSite(site, url):
        with semaphore:
            try:
                response = requests.get(url, timeout=5, allow_redirects=True)
                if response.status_code == 200:
                    with lock:
                        found.append(url)
                        print(f"{SUCCESS} {site:<16} :{red} {url}", reset)
            except:
                pass

    threads = []
    for site, url in sites.items():
        t = threading.Thread(target=CheckSite, args=(site, url))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    if not found:
        print(f"{ERROR} No accounts found!", reset)

    Continue()
    Reset()

except Exception as e:
    Error(e)