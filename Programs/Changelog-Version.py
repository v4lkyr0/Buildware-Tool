# Copyright (c) 2026 v4lkyr0
# See LICENSE file for details

from Plugins.Utils import *
from Plugins.Config import *

Title(f"{version_tool} Changelog")

try:
    changelog = f"""
────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────

 {INFO}{red} Creator Message:
 {INFO}    - Hello {username_pc}! Hope you're enjoying all the features in this tool. If you like it
          and want to support the project, feel free to leave a star on the repository!
 
 {INFO} {red}New Features:
 {INFO}    - Discord Token Grabber Builder [Star Required]
 {INFO}    - Discord Injection Builder     [Star Required]
 {INFO}    - Discord Injection Cleaner
 {INFO}    - Discord Server Scraper        [Star Required]
 {INFO}    - Discord Server Cloner         [Star Required]
 {INFO}    - Discord Server Editor
 {INFO}    - Discord Vanity Url Sniper     [Star Required]
 {INFO}    - Discord Invite Generator
 {INFO}    - Discord Invite Tracker
 {INFO}    - Discord Embed Creator
 {INFO}    - Discord Bot Information
 {INFO}    - Discord Bot Nuker             [Star Required]
 {INFO}    - Discord Bot Raider            [Star Required]
 {INFO}    - Discord Token Banner Changer
 {INFO}    - Discord Server Ban All        [Star Required]
 {INFO}    - Discord Server Kick All
 {INFO}    - Discord Server Unban All
 {INFO}    - Discord Server Mute All

 {INFO} {red}Improvements:
 {INFO}    - All scripts are now more stable and less likely to encounter errors or get rate limited.

 {INFO} {red}Bug Fixes:
 {INFO}    - All known bugs have been fixed.

 {INFO} {red}Renamed Features:
 {INFO}    - Discord Token Alias Changer {red}->{white} Discord Token Pronoun Changer

 {INFO} {red}Removed Features:
 {INFO}    - Nothing has been removed.

────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────"""
    Scroll(Gradient(changelog))

    Continue()
    Reset()

except Exception as e:
    Error(e)