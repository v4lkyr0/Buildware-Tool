# Copyright (c) 2025 v4lkyr0
# See LICENSE file for details

from Plugins.Utils import *
from Plugins.Config import *

try:
    import requests
except Exception as e:
    MissingModule(e)

Title("Discord Webhook Information")
Connection()

try:
    webhook = ChoiceWebhook()

    print(f"{INFO} Fetching Webhook information..", reset)

    try:
        response = requests.get(webhook)
        if response.status_code == 200:
            data = response.json()
        else:
            print(f"{PREFIX} {ERROR} Failed to retrieve Webhook information!", reset)
            Continue()
            Reset()
    except:
        print(f"{PREFIX} {ERROR} An error occurred while fetching Webhook information!", reset)
        Continue()
        Reset()

    try:
        webhook_url = webhook
    except:
        webhook_url = "None"

    try:
        webhook_name = data.get('name')
    except:
        webhook_name = "None"

    try:
        webhook_id = data.get('id')
    except:
        webhook_id = "None"
        
    try:
        webhook_token = webhook.split("/")[-1]
    except:
        webhook_token = "None"
    
    try:
        webhook_avatar = data.get('avatar')
        if webhook_avatar:
            webhook_avatar_url = f"https://cdn.discordapp.com/avatars/{webhook_id}/{webhook_avatar}.png"
        else:
            webhook_avatar_url = "None"
    except:
        webhook_avatar = "None"
        webhook_avatar_url = "None"

    try:
        if 'user' in data:
            webhook_creator = data['user']['username']
        else:
            webhook_creator = "None"
    except:
        webhook_creator = "None"

    try:
        webhook_type_raw = data.get('type')
        if webhook_type_raw == 1:
            webhook_type = "Incoming Webhook"
        elif webhook_type_raw == 2:
            webhook_type = "Channel Follower Webhook"
        elif webhook_type_raw == 3:
            webhook_type = "Application Webhook"
        else:
            webhook_type = f"Unknown {red}({white}{webhook_type_raw}{red})"
    except:
        webhook_type = "None"

    try:
        webhook_server_id = data.get('guild_id')
    except:
        webhook_server_id = "None"

    try:
        webhook_channel_id = data.get('channel_id')
    except:
        webhook_channel_id = "None"

    Scroll(f"""
 {SUCCESS} Url        :{red} {webhook_url}
 {SUCCESS} Id         :{red} {webhook_id}
 {SUCCESS} Name       :{red} {webhook_name}
 {SUCCESS} Token      :{red} {webhook_token}
 {SUCCESS} Avatar Url :{red} {webhook_avatar_url}
 {SUCCESS} Type       :{red} {webhook_type}
 {SUCCESS} Server Id  :{red} {webhook_server_id}
 {SUCCESS} Channel Id :{red} {webhook_channel_id}
 {SUCCESS} Creator    :{red} {webhook_creator} {reset}
""")
    
    Continue()
    Reset()

except Exception as e:
    Error(e)