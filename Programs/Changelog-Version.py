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

 {INFO} Creator message:
 {INFO}    - Hi {username_pc}, welcome to {name_tool} v{version_tool}!

 {INFO} New features:
 {INFO}    - Added Stealer Builder feature & category
 {INFO}    - Added 'Attacks' category
 {INFO}    - Added Email Bomber
 {INFO}    - Added SMS Bomber
 {INFO}    - Added Phishing Attack
 {INFO}    - Added Password Zip Cracker
 {INFO}    - Added Password Hash Cracker
 {INFO}    - Added small DataBase with common passwords

 {INFO} Improvements:
 {INFO}    - Swapped the 'Osint' & 'Network' columns
 {INFO}    - Added new banners for all categories
 {INFO}    - LICENSE rewritten

 {INFO} Bug fixes:
 {INFO}    - Assorted fixes & small stability improvements

 {INFO} Renamed:
 {INFO}    - Nothing renamed in this release

 {INFO} Removed:
 {INFO}    - Nothing removed in this release

────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────"""
    Scroll(Gradient(changelog))

    Continue()
    Reset()

except Exception as e:
    Error(e)