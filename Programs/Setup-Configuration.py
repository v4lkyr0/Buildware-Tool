# Copyright (c) 2025-2026 v4lkyr0 — Buildware-Tools
# See the file 'LICENSE' for copying permission.
# --------------------------------------------------------
# EN: Non-commercial use only. Do not sell, remove credits
#     or redistribute without prior written permission.
# FR: Usage non-commercial uniquement. Ne pas vendre, supprimer
#     les crédits ou redistribuer sans autorisation écrite.

from Plugins.Utils import *
from Plugins.Config import *

Title("Setup Configuration")

Clear()

try:
    config = LoadData()

    Scroll(Gradient(f"""{buildware_banner}

╓──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╖
                                                  Setup Configuration                                                  
╙──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╜"""))

    TypeWriter(f"{INFO} Welcome {username_pc}! Let's quickly set things up so you can start using {name_tool}. It'll only take a moment.{reset}", 0.025)

    auto_update = input(f"\n{INPUT} Auto-updates {YESORNO} {red}->{reset} ").strip().lower()

    config["auto_update"] = auto_update in ["yes", "y"]
    config["first_run"]   = False

    SaveData(config)

    print(f"\n{SUCCESS} Configuration saved!", reset)

    Continue()
    Reset()

except Exception as e:
    Error(e)