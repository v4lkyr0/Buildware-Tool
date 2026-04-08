# Copyright (c) 2026 v4lkyr0
# See LICENSE file for details

from Plugins.Utils import *
from Plugins.Config import *

try:
    import requests
    import time
except Exception as e:
    MissingModule(e)

Title("Discord Invite Tracker")
Connection()

try:
    invite_code = input(f"{INPUT} Invite Code {red}->{reset} ").split("/")[-1]
    if not invite_code:
        ErrorInput()
    
    DEFAULT_CHECK_DELAY = 5
    MIN_CHECK_DELAY = 1
    
    delay = input(f"{INPUT} Check Delay {red}({white}seconds{red}){white} {red}->{reset} ").strip()
    try:
        delay = float(delay)
        if delay < MIN_CHECK_DELAY:
            delay = MIN_CHECK_DELAY
    except ValueError:
        delay = DEFAULT_CHECK_DELAY
    
    headers = {"User-Agent": RandomUserAgents()}
    
    print(f"{LOADING} Tracking Invite..", reset)
    print()
    
    previous_uses = None
    check_count   = 0
    
    while True:
        check_count += 1
        
        try:
            response = requests.get(f"https://discord.com/api/v9/invites/{invite_code}?with_counts=true", headers=headers)
            
            if response.status_code == 200:
                data = response.json()
                
                guild_name    = data.get("guild", {}).get("name", "Unknown")
                channel_name  = data.get("channel", {}).get("name", "Unknown")
                inviter       = data.get("inviter", {}).get("username", "Unknown")
                uses          = data.get("uses", 0)
                max_uses      = data.get("max_uses", 0)
                max_age       = data.get("max_age", 0)
                member_count  = data.get("approximate_member_count", 0)
                presence_count= data.get("approximate_presence_count", 0)
                
                if previous_uses is not None and uses > previous_uses:
                    print(f"{SUCCESS} Check:{red} {check_count:<6} {white}| Uses:{red} {uses}/{max_uses if max_uses > 0 else '∞'} {white}| New Member!", reset)
                else:
                    print(f"{LOADING} Check:{red} {check_count:<6} {white}| Uses:{red} {uses}/{max_uses if max_uses > 0 else '∞'} {white}| Members:{red} {member_count} {white}| Online:{red} {presence_count}", reset)
                
                previous_uses = uses
                
            elif response.status_code == 404:
                print(f"{ERROR} Invite expired or invalid!", reset)
                break
            else:
                print(f"{ERROR} Failed to fetch invite data!", reset)
        
        except Exception as e:
            print(f"{ERROR} Error:{red} {e}", reset)
        
        time.sleep(delay)
    
    Continue()
    Reset()

except Exception as e:
    Error(e)
