# Copyright (c) 2025 v4lkyr0
# See LICENSE file for details

from .Config import *

try:
    from colorama import Fore
    import ctypes
    import time
    import os
    import requests
    import random
    import subprocess
    import sys
except Exception as e:
    print('Required Python modules for Buildware-Tool are not installed. Please run "Setup.py" to install them.')
    input(f"Error: {e}")

username_webhook = "Buildware-Tool"
avatar_webhook   = "https://i.imgur.com/7Gu71Gc.png"
color_embed      = 0x880000

red    = Fore.RED
white  = Fore.WHITE
green  = Fore.GREEN
reset  = Fore.RESET
blue   = Fore.BLUE
yellow = Fore.YELLOW

PREFIX  = f"{red}[{white}"
SUFFIX  = f"{red}]{white}"
PREFIX1 = f"{red + "{" + white}"
SUFFIX1 = f"{red + "}" + white}"

YESORNO = f"{red}({white}y/n{red}){white}"
INPUT   = f"{PREFIX}>{SUFFIX}"
INFO    = f"{PREFIX}?{SUFFIX}"
ERROR   = f"{PREFIX}-{SUFFIX}"
SUCCESS = f"{PREFIX}+{SUFFIX}"
LOADING = f"{PREFIX}~{SUFFIX}"

tool_path = os.path.dirname(os.path.abspath(__file__)).split("Programs\\")[0].split("Programs/")[0].strip()

try:
    username_pc = os.getlogin()
except:
    username_pc = "user"

try:
    if sys.platform.startswith("win"):
        platform_pc = "Windows"
    elif sys.platform.startswith("linux"):
        platform_pc = "Linux"
    else:
        platform_pc = "Unknown"
except:
    platform_pc = "None"

def Connection():
    try:
        requests.get("https://www.google.com", timeout=5)
        pass
    except:
        print(f"{ERROR} An internet connection is required to use this feature!", reset)
        Continue()

def Update():
    url = f"https://api.github.com/repos/v4lkyr0/Buildware-Tool/releases/latest"
    try:
        response = requests.get(url)
        response.raise_for_status()
        github_version = response.json()['tag_name']
    except:
        return ""
    
    local_version = version_tool
    if local_version != github_version:
        print(f"{INFO} New version available! {local_version} {red}->{white} {github_version} {red}|{white} Link:{red} {github_url + "/releases/latest"}", reset)
        return ""
    else:
        return ""

def Clear():
    if platform_pc == "Windows":
        os.system("cls")
    elif platform_pc == "Linux":
        os.system("clear")

def Title(title):
    if platform_pc == "Windows":
        ctypes.windll.kernel32.SetConsoleTitleW(f"{name_tool} {version_tool} - [{title}]")
    elif platform_pc == "Linux":
        sys.stdout.write(f"\x1b]2;{name_tool} {version_tool} - [{title}]\x07")

def Reset():
    if platform_pc == "Windows":
        file = ['python', os.path.join(tool_path, 'Buildware.py')]
        subprocess.run(file)
    elif platform_pc == "Linux":
        file = ['python3', os.path.join(tool_path, 'Buildware.py')]
        subprocess.run(file)

def StartProgram(program):
    if platform_pc == "Windows":
        file = ['python', os.path.join(tool_path, 'Programs', program)]
        subprocess.run(file)
    elif platform_pc == "Linux":
        file = ['python3', os.path.join(tool_path, 'Programs', program)]
        subprocess.run(file)

def Scroll(text):
    for line in text.split("\n"):
        print(line)
        time.sleep(0.03)

def Continue():
    input(f"{INPUT} Press to continue {red}->{reset} ")

def Error(e):
    print(f"{ERROR} Error:{red} {e}", reset)
    Continue()
    sys.exit()

def ErrorChoice():
    print(f"{ERROR} Invalid choice!", reset)
    time.sleep(2)
    Reset()

def ErrorId():
    print(f"{ERROR} Invalid Id!", reset)
    time.sleep(2)
    Reset()

def ErrorUrl():
    print(f"{ERROR} Invalid Url!", reset)
    time.sleep(2)
    Reset()

def ErrorToken():
    print(f"{ERROR} Invalid Token!", reset)
    time.sleep(2)
    Reset()

def ErrorNumber():
    print(f"{ERROR} Invalid Number!", reset)
    time.sleep(2)
    Reset()

def ErrorInput():
    print(f"{ERROR} Invalid Input!", reset)
    time.sleep(2)
    Reset()

def ErrorWebhook():
    print(f"{ERROR} Invalid Webhook!", reset)
    time.sleep(2)
    Reset()

def MissingModule(e):
    print(f"{ERROR} Missing Module:{red} {e}", reset)
    Continue()
    Reset()

def Gradient(text):
    start_color = (223, 5, 5)
    end_color   = (121, 3, 3)
    num_steps   = 18
    colors      = []
    
    for i in range(num_steps):
        R = start_color[0] + (end_color[0] - start_color[0]) * i // (num_steps - 1)
        G = start_color[1] + (end_color[1] - start_color[1]) * i // (num_steps - 1)
        B = start_color[2] + (end_color[2] - start_color[2]) * i // (num_steps - 1)
        colors.append((R, G, B))

    colors += list(reversed(colors[:-1]))
    chars = '╖╜╙╓┴┼┘┤└┐▌▀()╚╗═╔╝─┬├┌└│]░▒░▒█▓▄'

    def ColorText(R, G, B, Char):
        return f"\033[38;2;{R};{G};{B}m{Char}"

    lines = text.split('\n')
    result = []

    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            if char in chars:
                color = colors[(i + j) % len(colors)]
                result.append(ColorText(*color, char))
            else:
                result.append(char)
        result.append('\033[0m\n')

    return ''.join(result)

def RandomUserAgents():
    file = os.path.join(tool_path, 'Programs', 'Extras', 'UserAgents.txt')

    with open(file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    if lines:
        user_agent = random.choice(lines).strip()
    else:
        user_agent = "Mozilla/5.0 (Linux; Android 4.4.4; Nexus 7 Build/KTU84P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.84 Safari/537.36"
    
    return user_agent

def CheckWebhook(webhook):
    try:
        response = requests.get(webhook, timeout=5)
        if response.status_code in [200, 204]:
            return True
        else:
            return False
    except:
        return None
    
def CheckToken(token):
    api = "https://discord.com/api/v8/users/@me"
    headers = {"Authorization": token, "User-Agent": RandomUserAgents()}
    try:
        response = requests.get(api, headers=headers, timeout=5)
        if response.status_code == 200:
            return True
        else:
            return False
    except:
        return None
    
def SaveWebhook(webhook):
    result = CheckWebhook(webhook)
    if result is True:
        with open(os.path.join(tool_path, 'Programs', 'Extras', 'DiscordWebhooks.txt'), 'a', encoding='utf-8') as f:
            f.write('\n' + webhook)
        return True
    return False

def SaveToken(token):
    result = CheckToken(token)
    if result is True:
        with open(os.path.join(tool_path, 'Programs', 'Extras', 'DiscordTokens.txt'), 'a', encoding='utf-8') as f:
            f.write('\n' + token)
        return True
    return False

def ChoiceWebhook():
    file_webhooks = os.path.join(tool_path, 'Programs', 'Extras', 'DiscordWebhooks.txt')
    path_name = f'{red}"{white}Programs/Extras/DiscordWebhooks.txt{red}"{white}'
    
    if not os.path.exists(file_webhooks):
        open(file_webhooks, 'w').close()
    
    webhooks       = {}
    valid_webhooks = {}
    webhook_number = 0
    
    with open(file_webhooks, 'r', encoding='utf-8') as file:
        for line in file:
            if not line.strip():
                continue
            
            webhook_number        += 1
            current_webhook        = line.strip()
            webhooks[webhook_number] = current_webhook
            
            if CheckWebhook(current_webhook):
                valid_webhooks[webhook_number] = current_webhook
    
    if not webhooks:
        print(f"{INFO} No Webhook found in {path_name}!", reset)
        while True:
            new_webhook = input(f"{INPUT} Webhook Url {red}->{reset} ")
            if CheckWebhook(new_webhook):
                with open(file_webhooks, 'w', encoding='utf-8') as f:
                    f.write(new_webhook)
                    print(f"{SUCCESS} Webhook added to {path_name}.", reset)
                time.sleep(1)
                return new_webhook
            else:
                ErrorWebhook()
    
    if not valid_webhooks:
        print(f"{INFO} No valid Webhook found in {path_name}!", reset)
        while True:
            new_webhook = input(f"{INPUT} Webhook Url {red}->{reset} ")
            if CheckWebhook(new_webhook):
                with open(file_webhooks, 'a', encoding='utf-8') as f:
                    f.write('\n' + new_webhook)
                    print(f"{SUCCESS} Webhook added to {path_name}.", reset)
                time.sleep(1)
                return new_webhook
            else:
                ErrorWebhook()
    
    print()
    for num, wh in webhooks.items():
        token_webhook  = wh.split("/")[-1]
        masked_webhook = token_webhook[:30] + ".." if len(token_webhook) > 30 else token_webhook

        if num in valid_webhooks:
            print(f"{red}[{white}{num:02d}{red}]{white} Status: {red}Valid{white}   | Webhook:{red} {masked_webhook}", reset)
        else:
            print(f"{red}[{white}{num:02d}{red}]{white} Status: {red}Invalid{white} | Webhook:{red} {masked_webhook}", reset)
    
    print(f'\n{INFO} To add more Webhooks, open {red}"{white}Programs/Extras/DiscordWebhooks.txt{red}"{white}.', reset)
    choice = int(input(f"{INPUT} Choice {red}->{reset} "))

    if choice not in webhooks:
        ErrorChoice()

    if choice in valid_webhooks:
        return valid_webhooks[choice]
    else:
        ErrorWebhook()
    
    selected_webhook = valid_webhooks.get(choice)
    if selected_webhook:
        return selected_webhook
    else:
        ErrorChoice()

def ChoiceToken():
    file_tokens   = os.path.join(tool_path, 'Programs', 'Extras', 'DiscordTokens.txt')
    path_name = f'{red}"{white}Programs/Extras/DiscordTokens.txt{red}"{white}'
    
    if not os.path.exists(file_tokens):
        open(file_tokens, 'w').close()
    
    tokens       = {}
    valid_tokens = {}
    token_number = 0
    
    with open(file_tokens, 'r', encoding='utf-8') as file:
        for line in file:
            if not line.strip():
                continue
            
            token_number        += 1
            current_token        = line.strip()
            tokens[token_number] = current_token
            
            if CheckToken(current_token):
                valid_tokens[token_number] = current_token
    
    if not tokens:
        print(f"{INFO} No Token found in {path_name}!", reset)
        while True:
            new_token = input(f"{INPUT} Token {red}->{reset} ")
            if CheckToken(new_token):
                with open(file_tokens, 'w', encoding='utf-8') as f:
                    f.write(new_token)
                    print(f"{SUCCESS} Token added to {path_name}.", reset)
                time.sleep(1)
                return new_token
            else:
                ErrorToken()
    
    if not valid_tokens:
        print(f"{INFO} No valid Token found in {path_name}!", reset)
        while True:
            new_token = input(f"{INPUT} Token {red}->{reset} ")
            if CheckToken(new_token):
                with open(file_tokens, 'a', encoding='utf-8') as f:
                    f.write('\n' + new_token)
                    print(f"{SUCCESS} Token added to {path_name}.", reset)
                time.sleep(1)
                return new_token
            else:
                ErrorToken()
    
    print()
    for num, tok3n in tokens.items():
        masked_token = tok3n[:30] + ".." if len(tok3n) > 30 else tok3n

        if num in valid_tokens:
            print(f"{PREFIX}{num:02d}{SUFFIX} Status: {red}Valid{white}   | Token:{red} {masked_token}", reset)
        else:
            print(f"{PREFIX}{num:02d}{SUFFIX} Status: {red}Invalid{white} | Token:{red} {masked_token}", reset)
    
    print(f'\n{INFO} To add more Tokens, open {red}"{white}Programs/Extras/DiscordTokens.txt{red}"{white}.', reset)
    choice = int(input(f"{INPUT} Choice {red}->{reset} "))
    
    if choice not in tokens:
        ErrorChoice()

    if choice in valid_tokens:
        return valid_tokens[choice]
    else:
        ErrorToken()

    selected_token = valid_tokens.get(choice)
    if selected_token:
        return selected_token
    else:
        ErrorChoice()

def ChoiceMultiToken():
    file_tokens   = os.path.join(tool_path, 'Programs', 'Extras', 'DiscordTokens.txt')
    path_name = f'{red}"{white}Programs/Extras/DiscordTokens.txt{red}"{white}'
    
    if not os.path.exists(file_tokens):
        open(file_tokens, 'w').close()
    
    tokens       = {}
    valid_tokens = {}
    token_number = 0
    
    with open(file_tokens, 'r', encoding='utf-8') as file:
        for line in file:
            if not line.strip():
                continue
            
            token_number        += 1
            current_token        = line.strip()
            tokens[token_number] = current_token
            
            if CheckToken(current_token):
                valid_tokens[token_number] = current_token
    
    if not tokens:
        print(f"{INFO} No Token found in {path_name}!", reset)
        print(f"{ERROR} Please add Tokens to {path_name}.", reset)
        time.sleep(2)
        Reset()
    
    if not valid_tokens:
        print(f"{INFO} No valid Token found in {path_name}!", reset)
        print(f"{ERROR} Please add valid Tokens to {path_name}.", reset)
        time.sleep(2)
        Reset()
    
    print()
    for num, tok3n in tokens.items():
        masked_token = tok3n[:30] + ".." if len(tok3n) > 30 else tok3n

        if num in valid_tokens:
            print(f"{PREFIX}{num:02d}{SUFFIX} Status: {red}Valid{white}   | Token:{red} {masked_token}", reset)
        else:
            print(f"{PREFIX}{num:02d}{SUFFIX} Status: {red}Invalid{white} | Token:{red} {masked_token}", reset)

    print(f'\n {INFO} To add more Tokens, open {red}"{white}Programs/Extras/DiscordTokens.txt{red}"{white}.')
    
    while True:
        try:
            num_tokens = int(input(f"{INPUT} Number {red}->{reset} "))
            
            if num_tokens <= 0:
                ErrorNumber()
            
            if num_tokens > len(valid_tokens):
                print(f"{ERROR} Not enough valid Tokens!", reset)
                time.sleep(2)
                Reset()
            
            break
        except ValueError:
            ErrorNumber()
    
    selected_tokens = []
    
    for i in range(num_tokens):
        while True:
            try:
                choice = int(input(f"{INPUT} Token {i + 1} {red}->{reset} "))
                
                if choice not in tokens:
                    ErrorChoice()
                
                if choice not in valid_tokens:
                    ErrorToken()
                
                if valid_tokens[choice] not in selected_tokens:
                    selected_tokens.append(valid_tokens[choice])
                    break
                else:
                    print(f"{ERROR} Token already selected!", reset)
                    Continue()
                    Reset()
                    
            except ValueError:
                ErrorNumber()
    
    return selected_tokens

def ChoiceMultiWebhook():
    file_webhooks = os.path.join(tool_path, 'Programs', 'Extras', 'DiscordWebhooks.txt')
    path_name = f'{red}"{white}Programs/Extras/DiscordWebhooks.txt{red}"{white}'
    
    if not os.path.exists(file_webhooks):
        open(file_webhooks, 'w').close()
    
    webhooks       = {}
    valid_webhooks = {}
    webhook_number = 0
    
    with open(file_webhooks, 'r', encoding='utf-8') as file:
        for line in file:
            if not line.strip():
                continue
            
            webhook_number        += 1
            current_webhook        = line.strip()
            webhooks[webhook_number] = current_webhook
            
            if CheckWebhook(current_webhook):
                valid_webhooks[webhook_number] = current_webhook
    
    if not webhooks:
        print(f"{INFO} No Webhook found in {path_name}!", reset)
        print(f"{ERROR} Please add Webhooks to {path_name}.", reset)
        time.sleep(2)
        Reset()
    
    if not valid_webhooks:
        print(f"{INFO} No valid Webhook found in {path_name}!", reset)
        print(f"{ERROR} Please add valid Webhooks to {path_name}.", reset)
        time.sleep(2)
        Reset()
    
    print()
    for num, wh in webhooks.items():
        token_webhook  = wh.split("/")[-1]
        masked_webhook = token_webhook[:30] + ".." if len(token_webhook) > 30 else token_webhook

        if num in valid_webhooks:
            print(f"{PREFIX}{num:02d}{SUFFIX} Status: {red}Valid{white}   | Webhook:{red} {masked_webhook}", reset)
        else:
            print(f"{PREFIX}{num:02d}{SUFFIX} Status: {red}Invalid{white} | Webhook:{red} {masked_webhook}", reset)

    print(f'\n{INFO} To add more Webhooks, open {red}"{white}Programs/Extras/DiscordWebhooks.txt{red}"{white}.')
    
    while True:
        try:
            num_webhooks = int(input(f"{INPUT} Number {red}->{reset} "))
            
            if num_webhooks <= 0:
                ErrorNumber()
            
            if num_webhooks > len(valid_webhooks):
                print(f"{ERROR} Not enough valid Webhooks!", reset)
                time.sleep(2)
                Reset()
            
            break
        except ValueError:
            ErrorNumber()
    
    selected_webhooks = []
    
    for i in range(num_webhooks):
        while True:
            try:
                choice = int(input(f"{INPUT} Webhook {i + 1} {red}->{reset} "))
                
                if choice not in webhooks:
                    ErrorChoice()
                
                if choice not in valid_webhooks:
                    ErrorWebhook()
                
                if valid_webhooks[choice] not in selected_webhooks:
                    selected_webhooks.append(valid_webhooks[choice])
                    break
                else:
                    print(f"{ERROR} Webhook already selected!", reset)
                    Continue()
                    Reset()
                    
            except ValueError:
                ErrorNumber()
    
    return selected_webhooks