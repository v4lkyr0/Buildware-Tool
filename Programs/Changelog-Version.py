# Copyright (c) 2025-2026 v4lkyr0 — Buildware-Tools
# See the file 'LICENSE' for copying permission.
# --------------------------------------------------------
# EN: Non-commercial use only. Do not sell, remove credits
#     or redistribute without prior written permission.
# FR: Usage non-commercial uniquement. Ne pas vendre, supprimer
#     les crédits ou redistribuer sans autorisation écrite.

from Core.Utils import *
from Core.Config import *

Title(f"{version_tool} Changelog")

Scroll(GradientBanner(utilities_banner)) 

try:
    changelog = f"""
────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
 
 {INFO} Creator Message
 {INFO}    - Hey {username_pc}! Welcome to {name_tool} v{version_tool}!
 {INFO}      This update introduces the Plugin System, install community plugins directly from Plugin Manager.
 {INFO}      Want to create your own? Everything you need is in Programs/Plugins/Example-Plugin ({white}read main.py{red}). Good luck!
 
 {INFO} New Features
 {INFO}    - Added Plugins Category
 {INFO}    - Added Example Plugin to the Plugins category, you can hide or uninstall it if you wish
 {INFO}    - Added a ASCII animation on startup, you can remove it on Programs/Extras/Config.json
 
 {INFO} Improvements
 {INFO}    - Added a youtube tutorial for github token
 {INFO}    - MacOS supported
 {INFO}    - Improved Setup.py with Python version check and missing dependencies detection
 {INFO}    - Added a GitHub wiki for {name_tool}
 {INFO}    - Added Osint links on Phone Number Lookup
 {INFO}    - Network-Proxy-Scraper : No more duplicate proxies, slow proxies filtered out, results sorted by speed,
 {INFO}      separate file per protocol.
 {INFO}    - Network-Network-Scanner : Now shows the subnet before scanning, and each host displays its first open port.
 {INFO}    - Network-Ip-Port-Scanner : Added resolved IP display, banner grabbing on open ports, results sorted.
 {INFO}    - Network-Ssl-Checker : More specific error messages for each failure type.
 {INFO}    - Network-Proxy-Checker : Auto-strips protocol prefix, errors split for clearer feedback.
 {INFO}    - Network-Traceroute : Missing hops now shown explicitly, final summary added.
 {INFO}    - Network-Ip-Pinger : Summary always displays even if all pings fail.
 {INFO}    - Network-Dns-Lookup : Added resolved IP display, specific exception handling, final summary.
 {INFO}    - Network-Http-Headers : Added security score summary, TooManyRedirects caught separately.
 {INFO}    - Network-Mac-Lookup : Added 422 status for invalid format, ConnectionError caught separately.
 {INFO}    - Osint-Subdomain-Finder : Fallback wordlist now shows entry count, gaierror caught specifically.
 {INFO}    - Osint-Ip-Reputation-Checker : Added resolved IP display, gaierror caught in CheckBlacklist.
 {INFO}    - Osint-Username-Tracker : Fixed duplicate Twitch entry, added final summary.
 {INFO}    - Osint-Email-Breach-Checker : Added 429 handling per source, better summary.
 {INFO}    - Osint-Ip-Lookup : Added Google Maps URL, 429 handling, ConnectionError caught separately.
 {INFO}    - Osint-Whois-Lookup : PywhoisError and ConnectionResetError caught specifically.
 {INFO}    - Osint-Phone-Number-Lookup : NumberParseException caught with error detail shown.
 {INFO}    - Osint-Exif-Data-Extractor : UnidentifiedImageError caught, KeyError handled in GetGps.
 {INFO}    - Osint-Google-Dork-Builder : Added Login Pages and Exposed Files search options.
 
 {INFO} Bug Fixes
 {INFO}    - No bug found
 
 {INFO} Renamed/Changed
 {INFO}    - Changed Feedback to Plugin Manager
 
 {INFO} Removed
 {INFO}    - Removed Paid Category
 
────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────"""

    Scroll(Gradient(changelog))

    Continue()
    Reset()

except Exception as e:
    Error(e)