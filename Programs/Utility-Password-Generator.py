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
    import random
    import string
except Exception as e:
    MissingModule(e)

Title("Password Generator")
Connection()

Scroll(GradientBanner(utilities_banner))

try:
    try:
        length = int(input(f"{INPUT} Length {red}->{reset} ").strip())
        if length < 1:
            ErrorNumber()
    except ValueError:
        ErrorNumber()

    Scroll(f"""
 {PREFIX}01{SUFFIX} Letters only
 {PREFIX}02{SUFFIX} Letters & Numbers
 {PREFIX}03{SUFFIX} Letters, Numbers & Symbols
""")

    choice = input(f"{INPUT} Choice {red}->{reset} ").strip().lstrip("0")

    if choice == "1":
        chars = string.ascii_letters
    elif choice == "2":
        chars = string.ascii_letters + string.digits
    elif choice == "3":
        chars = string.ascii_letters + string.digits + string.punctuation
    else:
        ErrorChoice()

    password = "".join(random.choices(chars, k=length))

    print(f"{SUCCESS} Password:{red} {password}", reset)

    Continue()
    Reset()

except Exception as e:
    Error(e)