from Programs.Plugins.Utils import *
from Programs.Plugins.Config import *

try:
    import time
    import sys
    import os
except Exception as e:
    MissingModule(e)

pages_path = os.path.join(tool_path, "Programs", "Extras", "Pages.txt")

def Connection():
    try:
        requests.get("https://www.google.com", timeout=5)
    except:
        print(f"{ERROR} An internet connection is required to use {name_tool}!", reset)
        Continue()
        sys.exit()

def SavePage(page):
    try:
        with open(pages_path, "w") as f:
            f.write(str(page))
    except:
        pass

def LoadPage():
    try:
        with open(pages_path, "r") as f:
            return int(f.read().strip())
    except:
        return 1

Banner = """
                          ▄▄▄▄    █    ██  ██▓ ██▓    ▓█████▄  █     █░ ▄▄▄       ██▀███  ▓█████  
                         ▓█████▄  ██  ▓██▒▓██▒▓██▒    ▒██▀ ██▌▓█░ █ ░█░▒████▄    ▓██ ▒ ██▒▓█   ▀  
                         ▒██▒ ▄██▓██  ▒██░▒██▒▒██░    ░██   █▌▒█░ █ ░█ ▒██  ▀█▄  ▓██ ░▄█ ▒▒███   
                         ▒██░█▀  ▓▓█  ░██░░██░▒██░    ░▓█▄   ▌░█░ █ ░█ ░██▄▄▄▄██ ▒██▀▀█▄  ▒▓█  ▄  
                         ░▓█  ▀█▓▒▒█████▓ ░██░░██████▒░▒████▓ ░░██▒██▓  ▓█   ▓██▒░██▓ ▒██▒░▒████▒ 
                         ░▒▓███▀▒░▒▓▒ ▒ ▒ ░▓  ░ ▒░▓  ░ ▒▒▓  ▒ ░ ▓░▒ ▒   ▒▒   ▓▒█░░ ▒▓ ░▒▓░░░ ▒░ ░ 
                         ▒░▒   ░ ░░▒░ ░ ░  ▒ ░░ ░ ▒  ░ ░ ▒  ▒   ▒ ░ ░    ▒   ▒▒ ░  ░▒ ░ ▒░ ░ ░  ░ 
                          ░    ░  ░░░ ░ ░  ▒ ░  ░ ░    ░ ░  ░   ░   ░    ░   ▒     ░░   ░    ░    
                          ░         ░      ░      ░  ░   ░        ░          ░  ░   ░        ░  ░ """

def Menu(page=1):
    update = Update()
    Title(f"Page {page}")

    if page == 1:
        nav     = f"{red}> {PREFIX}?{SUFFIX} {version_tool} Changelog            ░                       ░                                            {white}Exit {name_tool} {PREFIX}E{SUFFIX} {red}<\n{red}> {PREFIX}!{SUFFIX} Tool Information                                                                                Extras Files {PREFIX}F{SUFFIX} {red}<\n                                                                                                         Next Page {PREFIX}N{SUFFIX} {red}<"
        content = f"""   ├─ {PREFIX1}01{SUFFIX1} Discord Token Information      ├─ {PREFIX1}11{SUFFIX1} Discord Server Information     ├─ {PREFIX1}21{SUFFIX1} Discord Snowflake Decoder
   ├─ {PREFIX1}02{SUFFIX1} Discord Token Login            ├─ {PREFIX1}12{SUFFIX1} Discord Token Joiner           ├─ {PREFIX1}22{SUFFIX1} Discord Id To Token
   ├─ {PREFIX1}03{SUFFIX1} Discord Token Onliner          ├─ {PREFIX1}13{SUFFIX1} Discord Token Leaver           ├─ {PREFIX1}23{SUFFIX1} Discord Bot Id To Invite
   ├─ {PREFIX1}04{SUFFIX1} Discord Token Bio Changer      ├─ {PREFIX1}14{SUFFIX1} Discord Token Delete Friends   ├─ {PREFIX1}24{SUFFIX1} Discord Webhook Information
   ├─ {PREFIX1}05{SUFFIX1} Discord Token Alias Changer    ├─ {PREFIX1}15{SUFFIX1} Discord Token Block Friends    ├─ {PREFIX1}25{SUFFIX1} Discord Webhook Generator
   ├─ {PREFIX1}06{SUFFIX1} Discord Token Pfp Changer      ├─ {PREFIX1}16{SUFFIX1} Discord Token Unblock Users    ├─ {PREFIX1}26{SUFFIX1} Discord Webhook Spammer
   ├─ {PREFIX1}07{SUFFIX1} Discord Token CStatus Changer  ├─ {PREFIX1}17{SUFFIX1} Discord Token Spammer          ├─ {PREFIX1}27{SUFFIX1} Discord Webhook Deleter
   ├─ {PREFIX1}08{SUFFIX1} Discord Token Theme Changer    ├─ {PREFIX1}18{SUFFIX1} Discord Token Mass Dm          ├─ {PREFIX1}28{SUFFIX1} Discord Token Generator
   ├─ {PREFIX1}09{SUFFIX1} Discord Token Language Changer ├─ {PREFIX1}19{SUFFIX1} Discord Token Delete Dm        ├─ {PREFIX1}29{SUFFIX1} Discord Token Disabler
   └─ {PREFIX1}10{SUFFIX1} Discord Token House Changer    └─ {PREFIX1}20{SUFFIX1} Discord Token Ghost Pinger     └─ {PREFIX1}30{SUFFIX1} Discord Token Nuker"""

    elif page == 2:
        nav     = f"{red}> {PREFIX}?{SUFFIX} {version_tool} Changelog            ░                       ░                                            {white}Exit {name_tool} {PREFIX}E{SUFFIX} {red}<\n{red}> {PREFIX}!{SUFFIX} Tool Information                                                                                Extras Files {PREFIX}F{SUFFIX} {red}<\n{red}> {PREFIX}B{SUFFIX} Back Page"
        content = f"""   ├─ {PREFIX1}31{SUFFIX1} Feature 31                     ├─ {PREFIX1}41{SUFFIX1} Feature 41                     ├─ {PREFIX1}51{SUFFIX1} Feature 51
   ├─ {PREFIX1}32{SUFFIX1} Feature 32                     ├─ {PREFIX1}42{SUFFIX1} Feature 42                     ├─ {PREFIX1}52{SUFFIX1} Feature 52
   ├─ {PREFIX1}33{SUFFIX1} Feature 33                     ├─ {PREFIX1}43{SUFFIX1} Feature 43                     ├─ {PREFIX1}53{SUFFIX1} Feature 53
   ├─ {PREFIX1}34{SUFFIX1} Feature 34                     ├─ {PREFIX1}44{SUFFIX1} Feature 44                     ├─ {PREFIX1}54{SUFFIX1} Feature 54
   ├─ {PREFIX1}35{SUFFIX1} Feature 35                     ├─ {PREFIX1}45{SUFFIX1} Feature 45                     ├─ {PREFIX1}55{SUFFIX1} Feature 55
   ├─ {PREFIX1}36{SUFFIX1} Feature 36                     ├─ {PREFIX1}46{SUFFIX1} Feature 46                     ├─ {PREFIX1}56{SUFFIX1} Feature 56
   ├─ {PREFIX1}37{SUFFIX1} Feature 37                     ├─ {PREFIX1}47{SUFFIX1} Feature 47                     ├─ {PREFIX1}57{SUFFIX1} Feature 57
   ├─ {PREFIX1}38{SUFFIX1} Feature 38                     ├─ {PREFIX1}48{SUFFIX1} Feature 48                     ├─ {PREFIX1}58{SUFFIX1} Feature 58
   ├─ {PREFIX1}39{SUFFIX1} Feature 39                     ├─ {PREFIX1}49{SUFFIX1} Feature 49                     ├─ {PREFIX1}59{SUFFIX1} Feature 59
   └─ {PREFIX1}40{SUFFIX1} Feature 40                     └─ {PREFIX1}50{SUFFIX1} Feature 50                     └─ {PREFIX1}60{SUFFIX1} Feature 60"""

    return f"""{update}{Banner}
{nav}

╓──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╖
                                        {github_url}
╙──┬──────────────────────────────────────┬──────────────────────────────────────┬─────────────────────────────────────╜
{content}"""

options = {
    '01': "Discord-Token-Information",      '21': "Discord-Snowflake-Decoder",      '41': "Feature-41",                     '?':  "Changelog-Version",
    '02': "Discord-Token-Login",            '22': "Discord-Id-To-Token",            '42': "Feature-42",                     '!':  "Tool-Information",
    '03': "Discord-Token-Onliner",          '23': "Discord-Bot-Id-To-Invite",       '43': "Feature-43",                     'f':  "Extras-Files",
    '04': "Discord-Token-Bio-Changer",      '24': "Discord-Webhook-Information",    '44': "Feature-44",
    '05': "Discord-Token-Alias-Changer",    '25': "Discord-Webhook-Generator",      '45': "Feature-45",
    '06': "Discord-Token-Pfp-Changer",      '26': "Discord-Webhook-Spammer",        '46': "Feature-46",
    '07': "Discord-Token-CStatus-Changer",  '27': "Discord-Webhook-Deleter",        '47': "Feature-47",
    '08': "Discord-Token-Theme-Changer",    '28': "Discord-Token-Generator",        '48': "Feature-48",
    '09': "Discord-Token-Language-Changer", '29': "Discord-Token-Disabler",         '49': "Feature-49",
    '10': "Discord-Token-House-Changer",    '30': "Discord-Token-Nuker",            '50': "Feature-50",
    '11': "Discord-Server-Information",     '31': "Feature-31",                     '51': "Feature-51",
    '12': "Discord-Token-Joiner",           '32': "Feature-32",                     '52': "Feature-52",
    '13': "Discord-Token-Leaver",           '33': "Feature-33",                     '53': "Feature-53",
    '14': "Discord-Token-Delete-Friends",   '34': "Feature-34",                     '54': "Feature-54",
    '15': "Discord-Token-Block-Friends",    '35': "Feature-35",                     '55': "Feature-55",
    '16': "Discord-Token-Unblock-Users",    '36': "Feature-36",                     '56': "Feature-56",
    '17': "Discord-Token-Spammer",          '37': "Feature-37",                     '57': "Feature-57",
    '18': "Discord-Token-Mass-Dm",          '38': "Feature-38",                     '58': "Feature-58",
    '19': "Discord-Token-Delete-Dm",        '39': "Feature-39",                     '59': "Feature-59",
    '20': "Discord-Token-Ghost-Pinger",     '40': "Feature-40",                     '60': "Feature-60",
}

Connection()
page = LoadPage()

while True:
    try:
        Clear()
        Scroll(Gradient(Menu(page)))

        choice = input(f"{PREFIX}{username_pc}@{name_tool}{SUFFIX} {red}->{reset} ").strip().lower()

        if choice in ['e', 'exit', 'q', 'quit']:
            SavePage(page)
            print(f"{LOADING} Exiting {name_tool}..")
            time.sleep(0.5)
            break
        elif choice in ['n', 'next']:
            page = 2
        elif choice in ['b', 'back']:
            page = 1
        elif choice in ['p', 'parrot']:
            Clear()
            Title("Parrot Live")
            os.system("curl parrot.live")
        elif choice in options:
            StartProgram(options[choice] + '.py')
        elif choice.zfill(2) in options:
            StartProgram(options[choice.zfill(2)] + '.py')
        else:
            ErrorChoice()

        SavePage(page)

    except Exception as e:
        Error(e)