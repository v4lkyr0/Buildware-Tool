# Copyright (c) 2025-2026 v4lkyr0 — Buildware-Tools
# See the file 'LICENSE' for copying permission.
# --------------------------------------------------------
# EN: Non-commercial use only. Do not sell, remove credits
#     or redistribute without prior written permission.
# FR: Usage non-commercial uniquement. Ne pas vendre, supprimer
#     les crédits ou redistribuer sans autorisation écrite.

from Plugins.Utils import *
from Plugins.Config import *

Title("Stealer Builder")

Scroll(GradientBanner(stealer_banner))

try:
    print(f"{INFO} I have temporarily disabled this feature because it was flagged as a virus.\n    I am currently working on resolving the issue.\n", reset)

    Continue()
    Reset()
except Exception as e:
    Error(e)
