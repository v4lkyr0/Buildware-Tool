# Copyright (c) 2026 v4lkyr0
# See LICENSE file for details

from Plugins.Utils import *
from Plugins.Config import *

try:
    import requests
except Exception as e:
    MissingModule(e)

Title("Discord Invite Generator")
Connection()

try:
    token = ChoiceToken()
    
    server_id = input(f"{INPUT} Server ID {red}->{reset} ")
    if not server_id:
        ErrorId()
    
    channel_id = input(f"{INPUT} Channel ID {red}->{reset} ")
    if not channel_id:
        ErrorId()
    
    DEFAULT_MAX_AGE = 0
    DEFAULT_MAX_USES = 0
    
    max_age = input(f"{INPUT} Max Age {red}({white}seconds, 0 = never{red}){white} {red}->{reset} ").strip()
    try:
        max_age = int(max_age)
    except ValueError:
        max_age = DEFAULT_MAX_AGE
    
    max_uses = input(f"{INPUT} Max Uses {red}({white}0 = unlimited{red}){white} {red}->{reset} ").strip()
    try:
        max_uses = int(max_uses)
    except ValueError:
        max_uses = DEFAULT_MAX_USES
    
    headers = {"Authorization": token, "Content-Type": "application/json", "User-Agent": RandomUserAgents()}
    
    print(f"{LOADING} Generating Invite..", reset)
    
    payload = {
        "max_age": max_age,
        "max_uses": max_uses,
        "temporary": False,
        "unique": True
    }
    
    response = requests.post(f"https://discord.com/api/v9/channels/{channel_id}/invites", headers=headers, json=payload)
    
    if response.status_code == 200:
        invite_data = response.json()
        invite_code = invite_data.get("code", "Unknown")
        invite_url  = f"https://discord.gg/{invite_code}"
        
        print(f"{SUCCESS} Invite generated!", reset)
        print(f"{INFO} Code      {red}:{white} {red}{invite_code}", reset)
        print(f"{INFO} Url       {red}:{white} {red}{invite_url}", reset)
        print(f"{INFO} Max Uses  {red}:{white} {red}{max_uses if max_uses > 0 else 'Unlimited'}", reset)
        print(f"{INFO} Max Age   {red}:{white} {red}{max_age if max_age > 0 else 'Never'}", reset)
    else:
        print(f"{ERROR} Failed to generate Invite!", reset)
    
    Continue()
    Reset()

except Exception as e:
    Error(e)
