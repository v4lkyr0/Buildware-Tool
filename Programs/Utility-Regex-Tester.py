# Copyright (c) 2025-2026 v4lkyr0 — Buildware-Tools
# See the file 'LICENSE' for copying permission.
# --------------------------------------------------------
# EN: Non-commercial use only. Do not sell, remove credits
#     or redistribute without prior written permission.
# FR: Usage non-commercial uniquement. Ne pas vendre, supprimer
#     les crédits ou redistribuer sans autorisation écrite.

from Plugins.Utils import *
from Plugins.Config import *

try:
    import re
except Exception as e:
    MissingModule(e)

Title("Regex Tester")
Connection()

Scroll(GradientBanner(utilities_banner))

try:
    pattern = input(f"{INPUT} Pattern {red}->{reset} ").strip()

    if not pattern:
        ErrorInput()

    text = input(f"{INPUT} Text {red}->{reset} ").strip()

    if not text:
        ErrorInput()

    print(f"{LOADING} Testing..", reset)

    try:
        matches = re.findall(pattern, text)

        if matches:
            print(f"{SUCCESS} Found:{red} {len(matches)}{white} match(es)!", reset)
            for i, match in enumerate(matches, 1):
                print(f"{SUCCESS} Match {i:<4} :{red} {match}", reset)
        else:
            print(f"{ERROR} No matches found!", reset)
    except re.error as err:
        print(f"{ERROR} Invalid pattern:{red} {err}", reset)

    Continue()
    Reset()

except Exception as e:
    Error(e)