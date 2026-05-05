# Copyright (c) 2025-2026 v4lkyr0 — Buildware-Tools
# See the file 'LICENSE' for copying permission.
# --------------------------------------------------------
# EN: Non-commercial use only. Do not sell, remove credits
#     or redistribute without prior written permission.
# FR: Usage non-commercial uniquement. Ne pas vendre, supprimer
#     les crédits ou redistribuer sans autorisation écrite.

from Programs.Plugins.Config import *

import os
import sys
import subprocess
import webbrowser

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def OpenLinks():
    try:
        webbrowser.open(github_url)
        webbrowser.open(gunslol_url)
    except Exception:
        pass

if sys.platform.startswith("win"):
    os.system("cls")
elif sys.platform.startswith("linux"):
    os.system("clear")

print(f"Installing required modules for {name_tool}..")

subprocess.run([sys.executable, "-m", "pip", "install", "--upgrade", "pip"])
subprocess.run([sys.executable, "-m", "pip", "install", "-r", os.path.join(os.path.dirname(os.path.abspath(__file__)), "requirements.txt")])

OpenLinks()

subprocess.run([sys.executable, os.path.join(os.path.dirname(os.path.abspath(__file__)), "Buildware.py")])