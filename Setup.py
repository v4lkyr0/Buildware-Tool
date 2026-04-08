# Copyright (c) 2026 v4lkyr0
# See LICENSE file for details

from Programs.Plugins.Config import *
from Programs.Plugins.Utils import Title

import os
import sys

Title("Setup")

def OpenLinks():
    try:
        import webbrowser
        webbrowser.open(github_url)
        webbrowser.open(gunslol_url)
    except:
        pass

if sys.platform.startswith("win"):
    os.system("cls")
    print(f"Installing required modules for {name_tool}:")
    os.system("python -m pip install --upgrade pip")
    os.system("pip install -r requirements.txt")
    OpenLinks()
    os.system("python Buildware.py")
elif sys.platform.startswith("linux"):
    os.system("clear")
    print(f"Installing required modules for {name_tool}:")
    os.system("python3 -m pip install --upgrade pip")
    os.system("pip3 install -r requirements.txt")
    OpenLinks()
    os.system("python3 Buildware.py")