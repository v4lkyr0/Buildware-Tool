# Copyright (c) 2025-2026 v4lkyr0 — Buildware-Tools
# See the file 'LICENSE' for copying permission.
# --------------------------------------------------------
# EN: Non-commercial use only. Do not sell, remove credits
#     or redistribute without prior written permission.
# FR: Usage non-commercial uniquement. Ne pas vendre, supprimer
#     les crédits ou redistribuer sans autorisation écrite.

from Programs.Plugins.Utils import *
from Programs.Plugins.Config import *

try:
    import os
    import sys
    import time
except Exception as e:
    MissingModule(e)

config = LoadData()
if config.get("first_run", True):
    StartProgram("Setup-Configuration.py")
else:
    pass

def Connection():
    try:
        requests.get("https://www.google.com", timeout=5)
    except:
        print(f"{ERROR} An internet connection is required to use {name_tool}!", reset)
        Continue()
        sys.exit()

def ShowBanner():
    if os.environ.get("skip_banner") == "1":
        return
    Title("Banner")
    Clear()
    print("\n" * 6)
    Scroll(Gradient(buildware_banner))
    print("                                              - Coded by v4lkyr0 with <3 -")
    time.sleep(2)

def SavePage(page):
    try:
        data        = LoadData()
        data["page"] = page
        SaveData(data)
    except:
        pass

def LoadPage():
    try:
        data = LoadData()
        return int(data.get("page", 1))
    except:
        return 1

def Menu(page=1):
    update = Update()
    Title(f"Page {page}")

    if page == 1:
        nav     = f"{red}> {PREFIX}?{SUFFIX} {version_tool} Changelog            ░                       ░                                                  {white}Feedback {PREFIX}F{SUFFIX} {red}<\n{red}> {PREFIX}!{SUFFIX} Tool Information                                                                                Extras Files {PREFIX}E{SUFFIX} {red}<\n                                                                                                         Next Page {PREFIX}N{SUFFIX} {red}<"
        content = f"""
╓──────────────────────────────────────╖╓──────────────────────────────────────╖╓──────────────────────────────────────╖
                Network                                  Osint                                 Utilities               
╙┬─────────────────────────────────────╜╙┬─────────────────────────────────────╜╙┬─────────────────────────────────────╜
 ├─ {PREFIX1}01{SUFFIX1} Ip Port Scanner                 ├─ {PREFIX1}11{SUFFIX1} Ip Lookup                       ├─ {PREFIX1}21{SUFFIX1} Password Generator
 ├─ {PREFIX1}02{SUFFIX1} Ip Pinger                       ├─ {PREFIX1}12{SUFFIX1} Whois Lookup                    ├─ {PREFIX1}22{SUFFIX1} Temporary Mail
 ├─ {PREFIX1}03{SUFFIX1} Traceroute                      ├─ {PREFIX1}13{SUFFIX1} {StarRequired("Subdomain Finder")}                ├─ {PREFIX1}23{SUFFIX1} System Information
 ├─ {PREFIX1}04{SUFFIX1} Dns Lookup                      ├─ {PREFIX1}14{SUFFIX1} {StarRequired("Username Tracker")}                ├─ {PREFIX1}24{SUFFIX1} Hash Identifier
 ├─ {PREFIX1}05{SUFFIX1} Mac Lookup                      ├─ {PREFIX1}15{SUFFIX1} {StarRequired("Reverse Image Search")}            ├─ {PREFIX1}25{SUFFIX1} File Hasher
 ├─ {PREFIX1}06{SUFFIX1} {StarRequired("Ssl Checker")}                     ├─ {PREFIX1}16{SUFFIX1} {StarRequired("Email Breach Checker")}            ├─ {PREFIX1}26{SUFFIX1} Text Encoder/Decoder
 ├─ {PREFIX1}07{SUFFIX1} Proxy Checker                   ├─ {PREFIX1}17{SUFFIX1} {StarRequired("Phone Number Lookup")}             ├─ {PREFIX1}27{SUFFIX1} Regex Tester
 ├─ {PREFIX1}08{SUFFIX1} {StarRequired("Network Scanner")}                 ├─ {PREFIX1}18{SUFFIX1} {StarRequired("Ip Reputation Checker")}           ├─ {PREFIX1}28{SUFFIX1} {StarRequired("Jwt Decoder")}
 ├─ {PREFIX1}09{SUFFIX1} Bandwidth Tester                ├─ {PREFIX1}19{SUFFIX1} {StarRequired("Google Dork Builder")}             ├─ {PREFIX1}29{SUFFIX1} Qr Code Generator
 └─ {PREFIX1}10{SUFFIX1} {StarRequired("Http Headers")}                    └─ {PREFIX1}20{SUFFIX1} Domain Age Checker              └─ {PREFIX1}30{SUFFIX1} {StarRequired("Python Obfuscator")}"""

    elif page == 2:
        nav     = f"{red}> {PREFIX}?{SUFFIX} {version_tool} Changelog            ░                       ░                                                  {white}Feedback {PREFIX}F{SUFFIX} {red}<\n{red}> {PREFIX}!{SUFFIX} Tool Information                                                                                Extras Files {PREFIX}E{SUFFIX} {red}<\n{red}> {PREFIX}B{SUFFIX} Back Page                                                                                          Next Page {PREFIX}N{SUFFIX} {red}<"
        content = f"""
╓──────────────────────────────────────╖╓──────────────────────────────────────╖╓──────────────────────────────────────╖
            Stealer Builder                               Paid                                  Roblox                
╙┬─────────────────────────────────────╜╙┬─────────────────────────────────────╜╙┬─────────────────────────────────────╜
 └─ {PREFIX1}31{SUFFIX1} {StarRequired("Stealer Builder")}                 └─ {PREFIX1}41{SUFFIX1} {Prenium("Soon")}                            ├─ {PREFIX1}51{SUFFIX1} {StarRequired("Roblox Cookie Login")}
      ├─ {white}System Information                                                      ├─ {PREFIX1}52{SUFFIX1} Roblox Cookie Information
      ├─ {white}Wallets Sessions Files                                                  ├─ {PREFIX1}53{SUFFIX1} Roblox Id Information
      ├─ {white}Games/Telegram Sessions Files                                           ├─ {PREFIX1}54{SUFFIX1} Roblox Username Information
      ├─ {white}Discord Tokens                                                          ├─ {PREFIX1}55{SUFFIX1} {StarRequired("Roblox Group Information")}
      ├─ {white}Discord Injection                                                       └─ {PREFIX1}56{SUFFIX1} Roblox Game Information
      ├─ {white}Browsers Data
      ├─ {white}Interesting Files                                                   
      ├─ {white}Camera Capture
      └─ {white}Screenshots"""

    elif page == 3:
        nav     = f"{red}> {PREFIX}?{SUFFIX} {version_tool} Changelog            ░                       ░                                                  {white}Feedback {PREFIX}F{SUFFIX} {red}<\n{red}> {PREFIX}!{SUFFIX} Tool Information                                                                                Extras Files {PREFIX}E{SUFFIX} {red}<\n{red}> {PREFIX}B{SUFFIX} Back Page                                                                                          Next Page {PREFIX}N{SUFFIX} {red}<"
        content = f"""
╓──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╖
                                                         Discord                                                        
╙┬───────────────────────────────────────┬───────────────────────────────────────┬─────────────────────────────────────╜
 ├─ {PREFIX1}61{SUFFIX1} Discord Server Information      ├─ {PREFIX1}71{SUFFIX1} Discord Token Information       ├─ {PREFIX1}81{SUFFIX1} Discord Token Image Changer
 ├─ {PREFIX1}62{SUFFIX1} {StarRequired("Discord Server Editor")}           ├─ {PREFIX1}72{SUFFIX1} Discord Token Login             ├─ {PREFIX1}82{SUFFIX1} Discord Token Bio Changer
 ├─ {PREFIX1}63{SUFFIX1} {StarRequired("Discord Server Scraper")}          ├─ {PREFIX1}73{SUFFIX1} Discord Token Joiner            ├─ {PREFIX1}83{SUFFIX1} Discord Token Status Changer
 ├─ {PREFIX1}64{SUFFIX1} {StarRequired("Discord Server Cloner")}           ├─ {PREFIX1}74{SUFFIX1} Discord Token Leaver            ├─ {PREFIX1}84{SUFFIX1} Discord Token Generator
 ├─ {PREFIX1}65{SUFFIX1} {StarRequired("Discord Server Ban All")}          ├─ {PREFIX1}75{SUFFIX1} {StarRequired("Discord Token Mass Dm")}           ├─ {PREFIX1}85{SUFFIX1} Discord Embed Creator
 ├─ {PREFIX1}66{SUFFIX1} {StarRequired("Discord Server Kick All")}         ├─ {PREFIX1}76{SUFFIX1} {StarRequired("Discord Token Spammer")}           ├─ {PREFIX1}86{SUFFIX1} Discord Injection Cleaner
 ├─ {PREFIX1}67{SUFFIX1} Discord Server Unban All        ├─ {PREFIX1}77{SUFFIX1} {StarRequired("Discord Token Ghost Pinger")}      ├─ {PREFIX1}87{SUFFIX1} {StarRequired("Discord Webhook Spammer")}
 ├─ {PREFIX1}68{SUFFIX1} Discord Server Mute All         ├─ {PREFIX1}78{SUFFIX1} {StarRequired("Discord Token Nuker")}             ├─ {PREFIX1}88{SUFFIX1} Discord Webhook Information
 ├─ {PREFIX1}69{SUFFIX1} {StarRequired("Discord Bot Nuker")}               ├─ {PREFIX1}79{SUFFIX1} {StarRequired("Discord Token Disabler")}          ├─ {PREFIX1}89{SUFFIX1} {StarRequired("Discord Vanity Url Sniper")}
 └─ {PREFIX1}70{SUFFIX1} {StarRequired("Discord Bot Raider")}              └─ {PREFIX1}80{SUFFIX1} Discord Token Onliner           └─ {PREFIX1}90{SUFFIX1} Discord Snowflake Decoder"""

    return f"""{update}{buildware_banner}
{nav}
{content}"""

options = {
    "01": "Network-Ip-Port-Scanner",             "11": "Osint-Ip-Lookup",                          "21": "Utility-Password-Generator",
    "02": "Network-Ip-Pinger",                   "12": "Osint-Whois-Lookup",                       "22": "Utility-Temporary-Mail",
    "03": "Network-Traceroute",                  "13": "Osint-Subdomain-Finder",                   "23": "Utility-System-Information",
    "04": "Network-Dns-Lookup",                  "14": "Osint-Username-Tracker",                   "24": "Utility-Hash-Identifier",
    "05": "Network-Mac-Lookup",                  "15": "Osint-Reverse-Image-Search",               "25": "Utility-File-Hasher",
    "06": "Network-Ssl-Checker",                 "16": "Osint-Email-Breach-Checker",               "26": "Utility-Text-Encoder-Decoder",
    "07": "Network-Proxy-Checker",               "17": "Osint-Phone-Number-Lookup",                "27": "Utility-Regex-Tester",
    "08": "Network-Network-Scanner",             "18": "Osint-Ip-Reputation-Checker",              "28": "Utility-Jwt-Decoder",
    "09": "Network-Bandwidth-Tester",            "19": "Osint-Google-Dork-Builder",                "29": "Utility-Qr-Code-Generator",
    "10": "Network-Http-Headers",                "20": "Osint-Domain-Age-Checker",                 "30": "Utility-Python-Obfuscator",

    "31": "Stealer-Builder",                     "41": "Soon",                                     "51": "Roblox-Cookie-Login",
                                                                                                   "52": "Roblox-Cookie-Information",
                                                                                                   "53": "Roblox-Id-Information",
                                                                                                   "54": "Roblox-Username-Information",
                                                                                                   "55": "Roblox-Group-Information",
                                                                                                   "56": "Roblox-Game-Information",

    "61": "Discord-Server-Information",          "71": "Discord-Token-Information",                "81": "Discord-Token-Image-Changer",
    "62": "Discord-Server-Editor",               "72": "Discord-Token-Login",                      "82": "Discord-Token-Bio-Changer",
    "63": "Discord-Server-Scraper",              "73": "Discord-Token-Joiner",                     "83": "Discord-Token-Status-Changer",
    "64": "Discord-Server-Cloner",               "74": "Discord-Token-Leaver",                     "84": "Discord-Token-Generator",
    "65": "Discord-Server-Ban-All",              "75": "Discord-Token-Mass-Dm",                    "85": "Discord-Embed-Creator",
    "66": "Discord-Server-Kick-All",             "76": "Discord-Token-Spammer",                    "86": "Discord-Injection-Cleaner",
    "67": "Discord-Server-Unban-All",            "77": "Discord-Token-Ghost-Pinger",               "87": "Discord-Webhook-Spammer",
    "68": "Discord-Server-Mute-All",             "78": "Discord-Token-Nuker",                      "88": "Discord-Webhook-Information",
    "69": "Discord-Bot-Nuker",                   "79": "Discord-Token-Disabler",                   "89": "Discord-Vanity-Url-Sniper",
    "70": "Discord-Bot-Raider",                  "80": "Discord-Token-Onliner",                    "90": "Discord-Snowflake-Decoder",
}

star_required = {"06", "08", "10", "13", "14", "15", "16", "17", "18", "19", "28", "30", "31", "51", "55", "62", "63", "64", "65", "66", "69", "70", "75", "76", "77", "78", "79", "87", "89"}

Connection()
page = LoadPage()
ShowBanner()

while True:
    try:
        Clear()
        Scroll(Gradient(Menu(page)))

        choice = input(f"{PREFIX}{username_pc}@Buildware{SUFFIX} {red}->{reset} ").strip().lower()

        if choice in ['f', 'feedback']:
            StartProgram('Feedback.py')
        elif choice in ['n', 'next']:
            page = 1 if page == 3 else page + 1
        elif choice in ['b', 'back']:
            page = 3 if page == 1 else page - 1
        elif choice in ['?', 'changelog']:
            StartProgram('Changelog-Version.py')
        elif choice in ['!', 'tool', 'info']:
            StartProgram('Tool-Information.py')
        elif choice in ['e', 'extras']:
            StartProgram('Extras-Files.py')
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
            ErrorFeature()

        SavePage(page)

    except Exception as e:
        Error(e)