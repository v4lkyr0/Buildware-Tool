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
    time.sleep(3)

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

def Menu(page=1):
    update = Update()
    Title(f"Page {page}")

    if page == 1:
        nav = f"{red}> {PREFIX}?{SUFFIX} {version_tool} Changelog            ░                       ░                                                  {white}Feedback {PREFIX}F{SUFFIX} {red}<\n{red}> {PREFIX}!{SUFFIX} Tool Information                                                                                Extras Files {PREFIX}E{SUFFIX} {red}<\n                                                                                                         Next Page {PREFIX}N{SUFFIX} {red}<"
        content = f"""
╓──────────────────────────────────────╖╓──────────────────────────────────────╖╓──────────────────────────────────────╖
                Network                                  Osint                                 Utilities               
╙┬─────────────────────────────────────╜╙┬─────────────────────────────────────╜╙┬─────────────────────────────────────╜
 ├─ {PREFIX1}01{SUFFIXP} Ip Port Scanner                 ├─ {PREFIX1}11{SUFFIX1} Ip Lookup                       ├─ {PREFIX1}21{SUFFIX1} Password Generator
 ├─ {PREFIX1}02{SUFFIX1} Ip Pinger                       ├─ {PREFIX1}12{SUFFIX1} Dns Lookup                      ├─ {PREFIX1}22{SUFFIXP} Temp Mail
 ├─ {PREFIX1}03{SUFFIX1} Traceroute                      ├─ {PREFIX1}13{SUFFIX1} Whois Lookup                    ├─ {PREFIX1}23{SUFFIX1} System Information
 ├─ {PREFIX1}04{SUFFIX1} Reverse Dns                     ├─ {PREFIX1}14{SUFFIXP} Subdomain Finder                ├─ {PREFIX1}24{SUFFIX1} Hash Generator
 ├─ {PREFIX1}05{SUFFIX1} Mac Lookup                      ├─ {PREFIX1}15{SUFFIX1} Header Analyzer                 ├─ {PREFIX1}25{SUFFIX1} Hash Identifier
 ├─ {PREFIX1}06{SUFFIX1} Interface Information           ├─ {PREFIX1}16{SUFFIX1} Website Detector                ├─ {PREFIX1}26{SUFFIX1} File Hasher
 ├─ {PREFIX1}07{SUFFIX1} Website Status                  ├─ {PREFIX1}17{SUFFIXP} Username Lookup                 ├─ {PREFIX1}27{SUFFIX1} Base64 Converter
 ├─ {PREFIX1}08{SUFFIX1} Ssl Checker                     ├─ {PREFIX1}18{SUFFIX1} Email Checker                   ├─ {PREFIX1}28{SUFFIX1} Caesar Cipher
 ├─ {PREFIX1}09{SUFFIX1} Proxy Checker                   ├─ {PREFIX1}19{SUFFIXP} Email Breach Checker            ├─ {PREFIX1}29{SUFFIX1} Text Converter
 └─ {PREFIX1}10{SUFFIXP} Wifi Passwords                  └─ {PREFIX1}20{SUFFIX1} Phone Lookup                    └─ {PREFIX1}30{SUFFIX1} Url Analyzer"""

    elif page == 2:
        nav = f"{red}> {PREFIX}?{SUFFIX} {version_tool} Changelog            ░                       ░                                                  {white}Feedback {PREFIX}F{SUFFIX} {red}<\n{red}> {PREFIX}!{SUFFIX} Tool Information                                                                                Extras Files {PREFIX}E{SUFFIX} {red}<\n{red}> {PREFIX}B{SUFFIX} Back Page                                                                                          Next Page {PREFIX}N{SUFFIX} {red}<"
        content = f"""
╓──────────────────────────────────────╖╓──────────────────────────────────────╖╓──────────────────────────────────────╖
            Stealer Builder                             Attacks                                  Roblox                
╙┬─────────────────────────────────────╜╙┬─────────────────────────────────────╜╙┬─────────────────────────────────────╜
 └─ {PREFIX1}31{SUFFIXP} Stealer Builder                 ├─ {PREFIX1}41{SUFFIXT} Email Bomber                    ├─ {PREFIX1}51{SUFFIXP} Roblox Cookie Login
      ├─ {white}System Information              ├─ {PREFIX1}42{SUFFIXT} Sms Bomber                      ├─ {PREFIX1}52{SUFFIXP} Roblox Cookie Information
      ├─ {white}Wallets Sessions Files          ├─ {PREFIX1}43{SUFFIXT} Phishing Attack                 ├─ {PREFIX1}53{SUFFIX1} Roblox Id Information
      ├─ {white}Games/Telegram Sessions Files   ├─ {PREFIX1}44{SUFFIXT} Password Zip Cracker            ├─ {PREFIX1}54{SUFFIX1} Roblox Username Information
      ├─ {white}Discord Tokens                  └─ {PREFIX1}45{SUFFIXT} Password Hash Cracker           ├─ {PREFIX1}55{SUFFIX1} Roblox Group Information
      ├─ {white}Discord Injection                                                       └─ {PREFIX1}56{SUFFIX1} Roblox Game Information
      ├─ {white}Browsers Data
      ├─ {white}Interesting Files                                                   
      ├─ {white}Camera Capture
      └─ {white}Screenshots"""

    elif page == 3:
        nav = f"{red}> {PREFIX}?{SUFFIX} {version_tool} Changelog            ░                       ░                                                  {white}Feedback {PREFIX}F{SUFFIX} {red}<\n{red}> {PREFIX}!{SUFFIX} Tool Information                                                                                Extras Files {PREFIX}E{SUFFIX} {red}<\n{red}> {PREFIX}B{SUFFIX} Back Page"
        content = f"""
╓──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╖
                                                         Discord                                                        
╙┬───────────────────────────────────────┬───────────────────────────────────────┬─────────────────────────────────────╜
 ├─ {PREFIX1}61{SUFFIX1} Discord Server Information      ├─ {PREFIX1}71{SUFFIX1} Discord Token Information       ├─ {PREFIX1}81{SUFFIX1} Discord Token Image Changer
 ├─ {PREFIX1}62{SUFFIX1} Discord Server Editor           ├─ {PREFIX1}72{SUFFIX1} Discord Token Login             ├─ {PREFIX1}82{SUFFIX1} Discord Token Bio Changer
 ├─ {PREFIX1}63{SUFFIXP} Discord Server Scraper          ├─ {PREFIX1}73{SUFFIX1} Discord Token Joiner            ├─ {PREFIX1}83{SUFFIX1} Discord Token Status Changer
 ├─ {PREFIX1}64{SUFFIXP} Discord Server Cloner           ├─ {PREFIX1}74{SUFFIX1} Discord Token Leaver            ├─ {PREFIX1}84{SUFFIX1} Discord Token Generator
 ├─ {PREFIX1}65{SUFFIXP} Discord Server Ban All          ├─ {PREFIX1}75{SUFFIXP} Discord Token Mass Dm           ├─ {PREFIX1}85{SUFFIX1} Discord Embed Creator
 ├─ {PREFIX1}66{SUFFIX1} Discord Server Kick All         ├─ {PREFIX1}76{SUFFIX1} Discord Token Spammer           ├─ {PREFIX1}86{SUFFIX1} Discord Injection Cleaner
 ├─ {PREFIX1}67{SUFFIX1} Discord Server Unban All        ├─ {PREFIX1}77{SUFFIX1} Discord Token Ghost Pinger      ├─ {PREFIX1}87{SUFFIX1} Discord Webhook Spammer
 ├─ {PREFIX1}68{SUFFIX1} Discord Server Mute All         ├─ {PREFIX1}78{SUFFIXP} Discord Token Nuker             ├─ {PREFIX1}88{SUFFIX1} Discord Webhook Information
 ├─ {PREFIX1}69{SUFFIXP} Discord Bot Nuker               ├─ {PREFIX1}79{SUFFIX1} Discord Token Disabler          ├─ {PREFIX1}89{SUFFIXP} Discord Vanity Url Sniper
 └─ {PREFIX1}70{SUFFIXP} Discord Bot Raider              └─ {PREFIX1}80{SUFFIX1} Discord Token Onliner           └─ {PREFIX1}90{SUFFIX1} Discord Snowflake Decoder"""

    return f"""{update}{buildware_banner}
{nav}
{content}"""

options = {
    "01": "Network-Ip-Port-Scanner",             "11": "Osint-Ip-Lookup",                          "21": "Utility-Password-Generator",
    "02": "Network-Ip-Pinger",                   "12": "Osint-Dns-Lookup",                         "22": "Utility-Temp-Mail",
    "03": "Network-Traceroute",                  "13": "Osint-Whois-Lookup",                       "23": "Utility-System-Information",
    "04": "Network-Reverse-Dns",                 "14": "Osint-Subdomain-Finder",                   "24": "Utility-Hash-Generator",
    "05": "Network-Mac-Lookup",                  "15": "Osint-Header-Analyzer",                    "25": "Utility-Hash-Identifier",
    "06": "Network-Interface-Information",       "16": "Osint-Website-Detector",                   "26": "Utility-File-Hasher",
    "07": "Network-Website-Status",              "17": "Osint-Username-Lookup",                    "27": "Utility-Base64-Converter",
    "08": "Network-Ssl-Checker",                 "18": "Osint-Email-Checker",                      "28": "Utility-Caesar-Cipher",
    "09": "Network-Proxy-Checker",               "19": "Osint-Email-Breach-Checker",               "29": "Utility-Text-Converter",
    "10": "Network-Wifi-Passwords",              "20": "Osint-Phone-Lookup",                       "30": "Utility-Url-Analyzer",

    "31": "Stealer-Builder",                     "41": "Soon",                                     "51": "Roblox-Cookie-Login",
                                                 "42": "Soon",                                     "52": "Roblox-Cookie-Information",
                                                 "43": "Soon",                                     "53": "Roblox-Id-Information",
                                                 "44": "Soon",                                     "54": "Roblox-Username-Information",
                                                 "45": "Not-Available",                            "55": "Roblox-Group-Information",
                                                 "46": "Not-Available",                            "56": "Roblox-Game-Information",
                                                 "47": "Not-Available",                            "57": "Not-Available",
                                                 "48": "Not-Available",                            "58": "Not-Available",
                                                 "49": "Not-Available",                            "59": "Not-Available",
                                                 "50": "Not-Available",                            "60": "Not-Available",

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

star_required = {"01", "10", "14", "17", "19", "22", "31", "45", "55", "63", "64", "65", "69", "70", "75", "78", "89"}

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
            if page < 3:
                page += 1
        elif choice in ['b', 'back']:
            if page > 1:
                page -= 1
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
            StartProgram('Not-Available.py')

        SavePage(page)

    except Exception as e:
        Error(e)