# Copyright (c) 2026 v4lkyr0
# See LICENSE file for details

from Plugins.Utils import *
from Plugins.Config import *

try:
    import requests
except Exception as e:
    MissingModule(e)

Title("Discord Token Theme Changer")
Connection()

try:
    token = ChoiceToken()

    Scroll(f"""
 {PREFIX}01{SUFFIX} Light Theme
 {PREFIX}02{SUFFIX} Dark Theme
 {PREFIX}03{SUFFIX} Darker Theme
 {PREFIX}04{SUFFIX} Midnight Theme
""")
    choice = input(f"{INPUT} Choice {red}->{reset} ").strip().lstrip("0")

    themes = {
        "1": "light",
        "2": "dark",
        "3": "darker",
        "4": "midnight"
    }
    if choice in themes:
        theme = themes[choice]

        print(f"{LOADING} Changing Theme..", reset)

        headers = {"Authorization": token, "Content-Type": "application/json"}
        data = {"theme": theme}

        try:
            response = requests.patch("https://discord.com/api/v9/users/@me/settings", json=data, headers=headers)
            if response.status_code == 200:
                print(f"{SUCCESS} Theme changed!", reset)
            else:
                print(f"{ERROR} Failed to change Theme!", reset)
        except:
            print(f"{ERROR} Error while trying to change Theme!", reset)
    else:
        ErrorNumber()

    Continue()
    Reset()

except Exception as e:
    Error(e)