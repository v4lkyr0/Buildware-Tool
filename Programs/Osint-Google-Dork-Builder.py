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
    import webbrowser
except Exception as e:
    MissingModule(e)

Title("Google Dork Builder")
Connection()

Scroll(GradientBanner(osint_banner))

try:
    Scroll(f"""
 {PREFIX}01{SUFFIX} Site Search
 {PREFIX}02{SUFFIX} File Type Search
 {PREFIX}03{SUFFIX} Intitle Search
 {PREFIX}04{SUFFIX} Inurl Search
 {PREFIX}05{SUFFIX} Intext Search
 {PREFIX}06{SUFFIX} Cache Search
 {PREFIX}07{SUFFIX} Related Search
 {PREFIX}08{SUFFIX} Custom Dork
""")

    choice = input(f"{INPUT} Choice {red}->{reset} ").strip().lstrip("0")

    if choice == "1":
        site    = input(f"{INPUT} Site {red}->{reset} ").strip()
        keyword = input(f"{INPUT} Keyword {red}->{reset} ").strip()
        dork    = f"site:{site} {keyword}"
    elif choice == "2":
        site     = input(f"{INPUT} Site {red}->{reset} ").strip()
        filetype = input(f"{INPUT} File Type {red}->{reset} ").strip()
        keyword  = input(f"{INPUT} Keyword {red}->{reset} ").strip()
        dork     = f"site:{site} filetype:{filetype} {keyword}"
    elif choice == "3":
        keyword = input(f"{INPUT} Keyword {red}->{reset} ").strip()
        dork    = f"intitle:{keyword}"
    elif choice == "4":
        keyword = input(f"{INPUT} Keyword {red}->{reset} ").strip()
        dork    = f"inurl:{keyword}"
    elif choice == "5":
        keyword = input(f"{INPUT} Keyword {red}->{reset} ").strip()
        dork    = f"intext:{keyword}"
    elif choice == "6":
        site = input(f"{INPUT} Site {red}->{reset} ").strip()
        dork = f"cache:{site}"
    elif choice == "7":
        site = input(f"{INPUT} Site {red}->{reset} ").strip()
        dork = f"related:{site}"
    elif choice == "8":
        dork = input(f"{INPUT} Dork {red}->{reset} ").strip()
        if not dork:
            ErrorInput()
    else:
        ErrorChoice()

    if not dork:
        ErrorInput()

    print(f"{LOADING} Opening..", reset)

    url = f"https://www.google.com/search?q={dork.replace(' ', '+')}"
    webbrowser.open(url)

    print(f"{SUCCESS} Dork:{red} {dork}", reset)

    Continue()
    Reset()

except Exception as e:
    Error(e)