# Copyright (c) 2025 v4lkyr0
# See LICENSE file for details

from Plugins.Utils import *
from Plugins.Config import *

Title(f"{version_tool} Changelog")

try:
    changelog = f"""
────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────

 {INFO} {red} Creator Message:
 {INFO}    - Sorry for the slower progress lately. I've had a heavy teaching workload and other commitments, which
          limited the time I could dedicate to development. Things should be moving forward more consistently soon.
          Thanks for your patience.
 
 {INFO} {red}New Features:
 {INFO}    - Discord Token Ghost Pinger

 {INFO} {red}Improvements:
 {INFO}    - README file updated.
 {INFO}    - Extras Files updated.
 {INFO}    - Added a second page to the main menu.

 {INFO} {red}Bug Fixes:
 {INFO}    - Update Checker now displays the correct version number.
 {INFO}    - Discord Token Delete Dm now works properly.
 {INFO}    - Discord Token Mass Dm now works properly.
 {INFO}    - Discord Id To Token now works properly.
 {INFO}    - Discord Token Delete Friends now works properly.
 {INFO}    - Discord Token Block Friends now works properly.
 {INFO}    - Discord Token Leaver now works properly.
 {INFO}    - Discord Token Generator now works properly.
 {INFO}    - Discord Token Login now works properly.

 {INFO} {red}Renamed Features:
 {INFO}    - Tokens File {red}->{white} Extras Files

 {INFO} {red}Removed Features:
 {INFO}    - Discord Nitro Generator

────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────"""
    Scroll(Gradient(changelog))

    Continue()
    Reset()

except Exception as e:
    Error(e)