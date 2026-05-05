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
 {INFO}    - 

 {INFO} New Features
 {INFO}    - Exif Data Extractor
 {INFO}    - Proxy Scraper
 {INFO}    - Zip Cracker
 {INFO}    - Hash Cracker
 {INFO}    - Nitro Generator
 {INFO}    - Dox Creator

 {INFO} Improvements
 {INFO}    - All scripts have been fixed, improved and made more stable
 {INFO}    - Add more sites for Username Tracker
 {INFO}    - Added automatic installation dependencies for Stealer Builder
 {INFO}    - Improved Advanced Python Obfuscator with new obfuscation techniques and better performance

 {INFO} Bug Fixes
 {INFO}    - All known bugs have been fixed

 {INFO} Renamed
 {INFO}    - The prefixes Discord and Roblox have been removed from all options that included them
 {INFO}    - Python Obfuscator {red}->{white} Advanced Python Obfuscator

 {INFO} Removed
 {INFO}    - Reverse Image Search
 {INFO}    - Bandwidth Tester
 {INFO}    - System Information
 {INFO}    - Regex Tester
 {INFO}    - Snowflake Decoder
 {INFO}    - Domain Age Checker

────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────"""

    Scroll(Gradient(changelog))

    Continue()
    Reset()

except Exception as e:
    Error(e)