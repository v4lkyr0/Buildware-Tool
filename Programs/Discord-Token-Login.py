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
    from selenium import webdriver
    import time
except Exception as e:
    MissingModule(e)

Title("Token Login")
Connection()

Scroll(GradientBanner(discord_banner))

try:
    token = ChoiceToken()

    Scroll(f"""
 {PREFIX}01{SUFFIX} Google Chrome
 {PREFIX}02{SUFFIX} Microsoft Edge
 {PREFIX}03{SUFFIX} Mozilla Firefox
""")

    browser_choice = input(f"{INPUT} Browser {red}->{reset} ").strip().lstrip("0")

    browsers = {
        "1": ("Google Chrome",   webdriver.Chrome),
        "2": ("Microsoft Edge",  webdriver.Edge),
        "3": ("Mozilla Firefox", webdriver.Firefox),
    }

    if browser_choice not in browsers:
        ErrorChoice()

    browser_name, driver_class = browsers[browser_choice]

    print(f"{LOADING} Starting {browser_name}..", reset)

    try:
        driver = driver_class()
    except:
        print(f"{ERROR} {browser_name} not installed or driver not updated!", reset)
        Continue()
        Reset()

    js_code = """
function login(token) {
    setInterval(() => {
        document.body.appendChild(document.createElement('iframe')).contentWindow.localStorage.token = `"${token}"`;
    }, 50);
    setTimeout(() => {
        location.reload();
    }, 2500);
}
"""

    driver.get("https://discord.com/login")

    print(f"{LOADING} Injecting..", reset)

    driver.execute_script(js_code + f'login("{token}");')

    time.sleep(5)

    print(f"{SUCCESS} Token injected!", reset)
    print(f"{INFO} If you leave the tool, {browser_name} will close.", reset)

    Continue()
    Reset()

except Exception as e:
    Error(e)