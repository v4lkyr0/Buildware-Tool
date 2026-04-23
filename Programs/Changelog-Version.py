# Copyright (c) 2025-2026 v4lkyr0 — Buildware-Tools
# See the file 'LICENSE' for copying permission.
# --------------------------------------------------------
# EN: Non-commercial use only. Do not sell, remove credits
#     or redistribute without prior written permission.
# FR: Usage non-commercial uniquement. Ne pas vendre, supprimer
#     les crédits ou redistribuer sans autorisation écrite.

from Plugins.Utils import *
from Plugins.Config import *

Title(f"{version_tool} Changelog")

Scroll(GradientBanner(utilities_banner))

try:
    changelog = f"""
────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────

 {INFO} Creator Message
 {INFO}    - Hi {username_pc}, welcome to {name_tool} v{version_tool}!
 {INFO}    - I wanted to let you know that I read your comments, thank you for your messages
 {INFO}      it makes me very happy! <3

 {INFO} New Features
 {INFO}    - Added Dns Lookup
 {INFO}    - Added Network Scanner
 {INFO}    - Added Bandwidth Tester
 {INFO}    - Added Http Headers
 {INFO}    - Added Reverse Image Search
 {INFO}    - Added Phone Number Lookup
 {INFO}    - Added Ip Reputation Checker
 {INFO}    - Added Text Encoder/Decoder
 {INFO}    - Added Qr Code Generator
 {INFO}    - Added Uuid Generator
 {INFO}    - Added Google Dork Builder
 {INFO}    - Added Jwt Decoder
 {INFO}    - Added Regex Tester
 {INFO}    - Added First Run Configuration
 {INFO}    - Added Auto-Update
 {INFO}    - Added Paid Category - maybe soon!

 {INFO} Improvements
 {INFO}    - Updated text colors for better visual distinction
 {INFO}    - New icon created by me!
 {INFO}    - Improved performance and stability
 {INFO}    - Updated every feature for better user experience

 {INFO} Bug Fixes
 {INFO}    - 

 {INFO} Renamed
 {INFO}    - Temp Mail {red}->{white} Temporary Mail
 {INFO}    - Username Lookup {red}->{white} Username Tracker

 {INFO} Removed
 {INFO}    - Removed Caesar Cipher
 {INFO}    - Removed Url Analyzer
 {INFO}    - Removed Email Checker
 {INFO}    - Removed Phone Lookup
 {INFO}    - Removed Interface Information
 {INFO}    - Removed Website Status
 {INFO}    - Removed Text Converter
 {INFO}    - Removed Hash Generator
 {INFO}    - Removed Base64 Converter
 {INFO}    - Removed Attacks Category
 {INFO}    - Removed Reverse Dns
 {INFO}    - Removed Wifi Passwords
 {INFO}    - Removed Header Analyzer
 {INFO}    - Removed Website Detector
 {INFO}    - Removed Password Hash Cracker
 {INFO}    - Removed Password Zip Cracker
 {INFO}    - Removed DataBase Folder

────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────"""

    Scroll(Gradient(changelog))

    Continue()
    Reset()

except Exception as e:
    Error(e)