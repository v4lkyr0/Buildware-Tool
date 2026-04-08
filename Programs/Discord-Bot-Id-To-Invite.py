# Copyright (c) 2026 v4lkyr0
# See LICENSE file for details

from Plugins.Utils import *
from Plugins.Config import *

try:
    import requests
    import webbrowser
except Exception as e:
    MissingModule(e)

Title("Discord Bot Id To Invite")
Connection()

try:
    id_bot = input(f"{INPUT} Bot Id {red}->{reset} ")
    
    print(f"\n{INFO} Permission Options:")
    print(f"{PREFIX}01{SUFFIX} Administrator {red}(8)")
    print(f"{PREFIX}02{SUFFIX} Manage Server {red}(32)")
    print(f"{PREFIX}03{SUFFIX} Kick Members {red}(2)")
    print(f"{PREFIX}04{SUFFIX} Ban Members {red}(4)")
    print(f"{PREFIX}05{SUFFIX} Manage Channels {red}(16)")
    print(f"{PREFIX}06{SUFFIX} Manage Roles {red}(268435456)")
    print(f"{PREFIX}07{SUFFIX} Send Messages {red}(2048)")
    print(f"{PREFIX}08{SUFFIX} Custom Permissions\n")
    
    perm_choice = input(f"{INPUT} Permission {red}->{reset} ").strip().lstrip("0")
    
    permission_map = {
        "1": "8",
        "2": "32",
        "3": "2",
        "4": "4",
        "5": "16",
        "6": "268435456",
        "7": "2048"
    }
    
    if perm_choice == "8":
        permissions = input(f"{INPUT} Custom Permission Value {red}->{reset} ")
    elif perm_choice in permission_map:
        permissions = permission_map[perm_choice]
    else:
        permissions = "8"

    print(f"{LOADING} Generating Invite Link..", reset)

    response = requests.get(f"https://discord.com/oauth2/authorize?client_id={id_bot}&scope=bot&permissions={permissions}")
    if response.status_code == 200:
        print(f"{SUCCESS} Invite Link:{red} {response.url}", reset)
    else:
        ErrorUrl()

    browser = input(f"{INPUT} Open Browser? {YESORNO} {red}->{reset} ").lower()
    if browser in ['y', 'yes']:
        try:
            webbrowser.open_new_tab(response.url)
            print(f"{SUCCESS} Browser opened!", reset)
        except:
            print(f"{ERROR} Error while trying to open Browser!", reset)

    Continue()
    Reset()

except Exception as e:
    Error(e)