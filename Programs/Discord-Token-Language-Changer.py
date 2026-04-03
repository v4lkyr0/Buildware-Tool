# Copyright (c) 2025 v4lkyr0
# See LICENSE file for details

from Plugins.Utils import *
from Plugins.Config import *

try:
    import requests
except Exception as e:
    MissingModule(e)

Title("Discord Token Language Changer")
Connection()

try:
    token = ChoiceToken()
    print()

    languages = {
        '01': ('bg', 'Bulgarian'),
        '02': ('zh-CN', 'Chinese {red}({white}China{red}){white}'),
        '03': ('zh-TW', 'Chinese {red}({white}Taiwan{red}){white}'),
        '04': ('hr', 'Croatian'),
        '05': ('cs', 'Czech'),
        '06': ('da', 'Danish'),
        '07': ('nl', 'Dutch'),
        '08': ('en-US', f'English {red}({white}US{red}){white}'),
        '09': ('en-GB', f'English {red}({white}UK{red}){white}'),
        '10': ('fi', 'Finnish'),
        '11': ('fr', 'French'),
        '12': ('de', 'German'),
        '13': ('el', 'Greek'),
        '14': ('hi', 'Hindi'),
        '15': ('hu', 'Hungarian'),
        '16': ('it', 'Italian'),
        '17': ('ja', 'Japanese'),
        '18': ('ko', 'Korean'),
        '19': ('lt', 'Lithuanian'),
        '20': ('no', 'Norwegian'),
        '21': ('pl', 'Polish'),
        '22': ('pt-BR', f'Portuguese {red}({white}Brazil{red}){white}'),
        '23': ('ro', 'Romanian'),
        '24': ('ru', 'Russian'),
        '25': ('es-ES', f'Spanish {red}({white}Spain{red}){white}'),
        '26': ('sv-SE', 'Swedish'),
        '27': ('th', 'Thai'),
        '28': ('tr', 'Turkish'),
        '29': ('uk', 'Ukrainian'),
        '30': ('vi', 'Vietnamese')
    }
    for key, (code, name) in languages.items():
        Scroll(f"{PREFIX}{key}{SUFFIX} {name}")

    choice = input(f"\n {INPUT} Language {red}->{reset} ").strip().lstrip("0")
    if choice in languages:
        language_code, language_name = languages[choice]

        print(f"{INFO} Changing Language..", reset)

        headers  = {'Authorization': token, 'Content-Type': 'application/json', 'User-Agent': RandomUserAgents()}
        data     = {'locale': language_code}
        response = requests.patch('https://discord.com/api/v9/users/@me/settings', headers=headers, json=data)

        try:
            if response.status_code == 200:
                print(f"{SUCCESS} Language changed!", reset)
            else:
                print(f"{ERROR} Failed to change Language!", reset)
        except:
            print(f"{ERROR} Error while trying to change Language!", reset)
    else:
        ErrorNumber()

    Continue()
    Reset()

except Exception as e:
    Error(e) 