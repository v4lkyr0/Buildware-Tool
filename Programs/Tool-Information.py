# Copyright (c) 2025-2026 v4lkyr0 — Buildware-Tools
# See the file 'LICENSE' for copying permission.
# --------------------------------------------------------
# EN: Non-commercial use only. Do not sell, remove credits
#     or redistribute without prior written permission.
# FR: Usage non-commercial uniquement. Ne pas vendre, supprimer
#     les crédits ou redistribuer sans autorisation écrite.

from Plugins.Utils import *
from Plugins.Config import *

Title("Tool Information")

Scroll(GradientBanner(information_banner))

try:
    Scroll(f"""
 {INFO} Tool Name :{red} {name_tool}
 {INFO} Version   :{red} {version_tool}
 {INFO} Type      :{red} {type_tool}
 {INFO} Author    :{red} {author_tool}
 {INFO} GitHub    :{red} {github_url}
 {INFO} Guns.lol  :{red} {gunslol_url}
 {INFO} License   :{red} {license} ({license_url})
""")
    Continue()
    Reset()

except Exception as e:
    Error(e)