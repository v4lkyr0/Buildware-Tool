# Copyright (c) 2025-2026 v4lkyr0 — Buildware-Tools
# See the file 'LICENSE' for copying permission.
# --------------------------------------------------------
# EN: Non-commercial use only. Do not sell, remove credits
#     or redistribute without prior written permission.
# FR: Usage non-commercial uniquement. Ne pas vendre, supprimer
#     les crédits ou redistribuer sans autorisation écrite.

from Plugins.Utils import *
from Plugins.Config import *

Title("Premium")

try:
    print(f"{INFO} This feature requires a premium license!", reset)
    print(f"{INFO} Purchase at:{red} {website_url}", reset)

    Continue()
    Reset()

except Exception as e:
    Error(e)