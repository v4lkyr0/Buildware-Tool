# Copyright (c) 2026 v4lkyr0
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
        '12': ('fr-CA', f'French {red}({white}Canada{red}){white}'),
        '13': ('de', 'German'),
        '14': ('el', 'Greek'),
        '15': ('hi', 'Hindi'),
        '16': ('hu', 'Hungarian'),
        '17': ('id', 'Indonesian'),
        '18': ('it', 'Italian'),
        '19': ('ja', 'Japanese'),
        '20': ('ko', 'Korean'),
        '21': ('lt', 'Lithuanian'),
        '22': ('no', 'Norwegian'),
        '23': ('pl', 'Polish'),
        '24': ('pt-BR', f'Portuguese {red}({white}Brazil{red}){white}'),
        '25': ('pt-PT', f'Portuguese {red}({white}Portugal{red}){white}'),
        '26': ('ro', 'Romanian'),
        '27': ('ru', 'Russian'),
        '28': ('es-ES', f'Spanish {red}({white}Spain{red}){white}'),
        '29': ('es-419', f'Spanish {red}({white}Latin America{red}){white}'),
        '30': ('sv-SE', 'Swedish'),
        '31': ('th', 'Thai'),
        '32': ('tr', 'Turkish'),
        '33': ('uk', 'Ukrainian'),
        '34': ('vi', 'Vietnamese')
    }
    for key, (code, name) in languages.items():
        Scroll(f"{PREFIX}{key}{SUFFIX} {name}")

    choice = input(f"\n {INPUT} Language {red}->{reset} ").strip().lstrip("0")
    if choice in languages:
        language_code, language_name = languages[choice]

        print(f"{LOADING} Changing Language..", reset)

        headers = {
            "Authorization": token,
            "Content-Type": "application/json",
            "User-Agent": RandomUserAgents()
        }
        data = {"locale": language_code}
        response = requests.patch("https://discord.com/api/v9/users/@me/settings", headers=headers, json=data)

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