# Copyright (c) 2025 v4lkyr0
# See LICENSE file for details

from Plugins.Utils import *
from Plugins.Config import *

try:
    import time
    from selenium import webdriver
except Exception as e:
    MissingModule(e)

Title("Discord Token Login")
Connection()

try:
    token = ChoiceToken()

    Scroll(f"""
 {PREFIX}01{SUFFIX} Google Chrome
 {PREFIX}02{SUFFIX} Microsoft Edge
 {PREFIX}03{SUFFIX} Mozilla Firefox
""")
    browser_choice = input(f"{INPUT} Browser {red}->{reset} ").strip().lstrip("0")

    BROWSERS = {
        "1": ("Google Chrome",   webdriver.Chrome),
        "2": ("Microsoft Edge",  webdriver.Edge),
        "3": ("Mozilla Firefox", webdriver.Firefox)
    }

    if browser_choice not in BROWSERS:
        ErrorNumber()

    browser_name, driver_class = BROWSERS[browser_choice]

    try:
        print(f"{LOADING} Starting {browser_name}..", reset)
        driver = driver_class()
    except:
        print(f"{ERROR} {browser_name} not installed or driver not updated!", reset)
        Continue()
        Reset()

    try:
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
        print(f"{LOADING} Injecting Token into Discord..", reset)
        driver.execute_script(js_code + f'login("{token}");')
        time.sleep(5)
        print(f"{SUCCESS} Token injected!", reset)
        print(f"{INFO} If you leave the tool, {browser_name} will close.", reset)
        Continue()
        Reset()
    except:
        print(f"{ERROR} Failed to inject Token into Discord!", reset)
        Continue()
        Reset()

except Exception as e:
    Error(e)