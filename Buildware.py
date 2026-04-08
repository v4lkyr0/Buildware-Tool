# Copyright (c) 2026 v4lkyr0
# See LICENSE file for details

from Programs.Plugins.Utils import *
from Programs.Plugins.Config import *

try:
    import os
    import sys
    import time
except Exception as e:
    MissingModule(e)

pages_path = os.path.join(tool_path, "Programs", "Extras", "Buildware.json")

def Connection():
    try:
        requests.get("https://www.google.com", timeout=5)
    except:
        print(f"{ERROR} An internet connection is required to use {name_tool}!", reset)
        Continue()
        sys.exit()

def SavePage(page):
    try:
        data = load_data()
        data["page"] = page
        save_data(data)
    except:
        pass

def LoadPage():
    try:
        data = load_data()
        return int(data.get("page", 1))
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
    Title(f"Page {page}")

    if page == 1:
        nav = f"{red}> {PREFIX}?{SUFFIX} {version_tool} Changelog            ░                       ░                                            {white}Exit {name_tool} {PREFIX}E{SUFFIX} {red}<\n{red}> {PREFIX}!{SUFFIX} Tool Information                                                                                Extras Files {PREFIX}F{SUFFIX} {red}<\n                                                                                                         Next Page {PREFIX}N{SUFFIX} {red}<"
        content = f"""   ├─ {PREFIX1}01{SUFFIX1} Discord Token Information      ├─ {PREFIX1}11{SUFFIX1} Discord Server Information     ├─ {PREFIX1}21{SUFFIX1} Discord Webhook Information
   ├─ {PREFIX1}02{SUFFIX1} Discord Token Login            ├─ {PREFIX1}12{SUFFIX1}{yellow} Discord Server Scraper         ├─ {PREFIX1}22{SUFFIX1} Discord Webhook Generator
   ├─ {PREFIX1}03{SUFFIX1} Discord Token Onliner          ├─ {PREFIX1}13{SUFFIX1}{yellow} Discord Server Cloner          ├─ {PREFIX1}23{SUFFIX1} Discord Webhook Spammer
   ├─ {PREFIX1}04{SUFFIX1} Discord Token Generator        ├─ {PREFIX1}14{SUFFIX1} Discord Server Editor          ├─ {PREFIX1}24{SUFFIX1} Discord Webhook Deleter
   ├─ {PREFIX1}05{SUFFIX1}{yellow} Discord Token Grabber Builder  ├─ {PREFIX1}15{SUFFIX1}{yellow} Discord Vanity Url Sniper      ├─ {PREFIX1}25{SUFFIX1} Discord Bot Information
   ├─ {PREFIX1}06{SUFFIX1} Discord Token Disabler         ├─ {PREFIX1}16{SUFFIX1} Discord Invite Generator       ├─ {PREFIX1}26{SUFFIX1}{yellow} Discord Bot Nuker
   ├─ {PREFIX1}07{SUFFIX1}{yellow} Discord Token Nuker            ├─ {PREFIX1}17{SUFFIX1} Discord Invite Tracker         ├─ {PREFIX1}27{SUFFIX1}{yellow} Discord Bot Raider
   ├─ {PREFIX1}08{SUFFIX1} Discord Token Joiner           ├─ {PREFIX1}18{SUFFIX1} Discord Embed Creator          ├─ {PREFIX1}28{SUFFIX1} Discord Bot Id To Invite
   ├─ {PREFIX1}09{SUFFIX1} Discord Token Leaver           ├─ {PREFIX1}19{SUFFIX1} Discord Snowflake Decoder      ├─ {PREFIX1}29{SUFFIX1} Discord Id To Token
   └─ {PREFIX1}10{SUFFIX1} Discord Token Spammer          └─ {PREFIX1}20{SUFFIX1}{yellow} Discord Mass Dm                └─ {PREFIX1}30{SUFFIX1} Discord Ghost Pinger"""

    elif page == 2:
        nav = f"{red}> {PREFIX}?{SUFFIX} {version_tool} Changelog            ░                       ░                                            {white}Exit {name_tool} {PREFIX}E{SUFFIX} {red}<\n{red}> {PREFIX}!{SUFFIX} Tool Information                                                                                Extras Files {PREFIX}F{SUFFIX} {red}<\n{red}> {PREFIX}B{SUFFIX} Back Page"
        content = f"""   ├─ {PREFIX1}31{SUFFIX1} Discord Token Pfp Changer      ├─ {PREFIX1}41{SUFFIX1}{yellow} Discord Server Ban All         ├─ {PREFIX1}51{SUFFIX1} Soon
   ├─ {PREFIX1}32{SUFFIX1} Discord Token Banner Changer   ├─ {PREFIX1}42{SUFFIX1} Discord Server Kick All        ├─ {PREFIX1}52{SUFFIX1} Soon
   ├─ {PREFIX1}33{SUFFIX1} Discord Token Bio Changer      ├─ {PREFIX1}43{SUFFIX1} Discord Server Unban All       ├─ {PREFIX1}53{SUFFIX1} Soon
   ├─ {PREFIX1}34{SUFFIX1} Discord Token Pronoun Changer  ├─ {PREFIX1}44{SUFFIX1} Discord Server Mute All        ├─ {PREFIX1}54{SUFFIX1} Soon
   ├─ {PREFIX1}35{SUFFIX1} Discord Token Theme Changer    ├─ {PREFIX1}45{SUFFIX1} Discord Delete Friends         ├─ {PREFIX1}55{SUFFIX1} Soon
   ├─ {PREFIX1}36{SUFFIX1} Discord Token Language Changer ├─ {PREFIX1}46{SUFFIX1} Discord Block Friends          ├─ {PREFIX1}56{SUFFIX1} Soon
   ├─ {PREFIX1}37{SUFFIX1} Discord Token Status Changer   ├─ {PREFIX1}47{SUFFIX1} Discord Unblock Users          ├─ {PREFIX1}57{SUFFIX1} Soon
   ├─ {PREFIX1}38{SUFFIX1} Discord Token House Changer    ├─ {PREFIX1}48{SUFFIX1} Discord Delete Dm              ├─ {PREFIX1}58{SUFFIX1} Soon
   ├─ {PREFIX1}39{SUFFIX1}{yellow} Discord Injection Builder      ├─ {PREFIX1}49{SUFFIX1} Soon                           ├─ {PREFIX1}59{SUFFIX1} Soon
   └─ {PREFIX1}40{SUFFIX1} Discord Injection Cleaner      └─ {PREFIX1}50{SUFFIX1} Soon                           └─ {PREFIX1}60{SUFFIX1} Soon"""

    return f"""{Banner}
{nav}

╓──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╖
                                        {github_url}
╙──┬──────────────────────────────────────┬──────────────────────────────────────┬─────────────────────────────────────╜
{content}"""

options = {
    "01": "Discord-Token-Information",      "21": "Discord-Webhook-Information",   "41": "Discord-Server-Ban-All",
    "02": "Discord-Token-Login",            "22": "Discord-Webhook-Generator",     "42": "Discord-Server-Kick-All",
    "03": "Discord-Token-Onliner",          "23": "Discord-Webhook-Spammer",       "43": "Discord-Server-Unban-All",
    "04": "Discord-Token-Generator",        "24": "Discord-Webhook-Deleter",       "44": "Discord-Server-Mute-All",
    "05": "Discord-Token-Grabber-Builder",  "25": "Discord-Bot-Information",       "45": "Discord-Token-Delete-Friends",
    "06": "Discord-Token-Disabler",         "26": "Discord-Bot-Nuker",             "46": "Discord-Token-Block-Friends",
    "07": "Discord-Token-Nuker",            "27": "Discord-Bot-Raider",            "47": "Discord-Token-Unblock-Users",
    "08": "Discord-Token-Joiner",           "28": "Discord-Bot-Id-To-Invite",      "48": "Discord-Token-Delete-Dm",
    "09": "Discord-Token-Leaver",           "29": "Discord-Id-To-Token",           "49": "Soon",
    "10": "Discord-Token-Spammer",          "30": "Discord-Token-Ghost-Pinger",    "50": "Soon",
    "11": "Discord-Server-Information",     "31": "Discord-Token-Pfp-Changer",     "51": "Soon",
    "12": "Discord-Server-Scraper",         "32": "Discord-Token-Banner-Changer",  "52": "Soon",
    "13": "Discord-Server-Cloner",          "33": "Discord-Token-Bio-Changer",     "53": "Soon",
    "14": "Discord-Server-Editor",          "34": "Discord-Token-Pronoun-Changer", "54": "Soon",
    "15": "Discord-Vanity-Url-Sniper",      "35": "Discord-Token-Theme-Changer",   "55": "Soon",
    "16": "Discord-Invite-Generator",       "36": "Discord-Token-Language-Changer","56": "Soon",
    "17": "Discord-Invite-Tracker",         "37": "Discord-Token-CStatus-Changer", "57": "Soon",
    "18": "Discord-Embed-Creator",          "38": "Discord-Token-House-Changer",   "58": "Soon",
    "19": "Discord-Snowflake-Decoder",      "39": "Discord-Injection-Builder",     "59": "Soon",
    "20": "Discord-Token-Mass-Dm",          "40": "Discord-Injection-Cleaner",     "60": "Soon",
}

star_required = {"05", "07", "12", "13", "15", "20", "26", "27", "39", "41"}

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
        elif choice in ['?', 'changelog']:
            StartProgram('Changelog-Version.py')
        elif choice in ['!', 'tool', 'info']:
            StartProgram('Tool-Information.py')
        elif choice in ['f', 'files', 'extras']:
            StartProgram('Extras-Files.py')
        elif choice in ['p', 'parrot']:
            Clear()
            Title("Parrot Live")
            os.system("curl parrot.live")
        elif choice in options:
            if choice in star_required and not CheckGithubStar():
                continue
            StartProgram(options[choice] + '.py')
        elif choice.zfill(2) in options:
            padded = choice.zfill(2)
            if padded in star_required and not CheckGithubStar():
                continue
            StartProgram(options[padded] + '.py')
        else:
            ErrorChoice()

        SavePage(page)

    except Exception as e:
        Error(e)