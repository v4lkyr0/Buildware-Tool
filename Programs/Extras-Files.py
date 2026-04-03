# Copyright (c) 2025 v4lkyr0
# See LICENSE file for details

from Plugins.Utils import *
from Plugins.Config import *

try:
    import os
    import subprocess
except Exception as e:
    MissingModule(e)

Title("Extras File")

try:
    extras_path = os.path.join(tool_path, "Programs", "Extras")
    
    print(f"\n{PREFIX}01{SUFFIX} Discord Tokens File", reset)
    print(f"{PREFIX}02{SUFFIX} Discord Webhooks File", reset)
    print(f"{PREFIX}03{SUFFIX} Extras Folder\n", reset)
    
    choice = input(f"{INPUT} Choice {red}->{reset} ").lstrip("0")
    
    if choice == "1":
        file_path = os.path.join(extras_path, "DiscordTokens.txt")
        file_name = "DiscordTokens.txt"
        print(f"{INFO} Each token must be on a separate line", reset)
    elif choice == "2":
        file_path = os.path.join(extras_path, "DiscordWebhooks.txt")
        file_name = "DiscordWebhooks.txt"
        print(f"{INFO} Each webhook URL must be on a separate line", reset)
    elif choice == "3":
        file_path = extras_path
        file_name = "Extras"
    else:
        ErrorChoice()
    
    print(f'{LOADING} Opening {red}"{white}{file_name}{red}"{white}..', reset)

    try:
        if platform_pc == "Windows":
            os.startfile(file_path)
        else:
            if choice == "3":
                subprocess.Popen(['xdg-open', file_path])
            else:
                subprocess.Popen(['xdg-open', file_path])
        print(f"{SUCCESS} {file_name} opened!", reset)
    except:
        print(f"{ERROR} Error while trying to open {file_name}!", reset)
        print(f"{INFO} Path:{red} {file_path}{reset}", reset)

    print()
    
    Continue()
    Reset()

except Exception as e:
    Error(e)