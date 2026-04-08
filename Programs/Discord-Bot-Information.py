# Copyright (c) 2026 v4lkyr0
# See LICENSE file for details

from Plugins.Utils import *
from Plugins.Config import *

try:
    import requests
    from datetime import datetime, timezone
except Exception as e:
    MissingModule(e)

Title("Discord Bot Information")
Connection()

try:
    bot_token = ChoiceBot()

    print(f"{LOADING} Retrieving Information..", reset)

    headers = {"Authorization": f"Bot {bot_token}", "Content-Type": "application/json"}
    
    response = requests.get("https://discord.com/api/v9/users/@me", headers=headers)
    
    if response.status_code != 200:
        print(f"{ERROR} Failed to retrieve bot information!", reset)
        Continue()
        Reset()
    
    api = response.json()
    
    status           = "Valid" if response.status_code == 200 else "Invalid"
    username         = api.get("username")
    bot_id           = api.get("id")
    discriminator    = api.get("discriminator")
    avatar           = api.get("avatar")
    bot_public       = api.get("public")
    bot_flag         = api.get("bot")
    flags            = api.get("flags")
    public_flags     = api.get("public_flags")
    accent_color     = api.get("accent_color")
    banner           = api.get("banner")
    banner_color     = api.get("banner_color")
    
    try:
        created_at_raw = datetime.fromtimestamp(((int(bot_id) >> 22) + 1420070400000) / 1000, timezone.utc)
        created_at     = created_at_raw.strftime("%Y-%m-%d %H:%M:%S")
    except:
        created_at = "None"
    
    try:
        if avatar:
            avatar_url = f"https://cdn.discordapp.com/avatars/{bot_id}/{avatar}.gif" if requests.get(f"https://cdn.discordapp.com/avatars/{bot_id}/{avatar}.gif").status_code == 200 else f"https://cdn.discordapp.com/avatars/{bot_id}/{avatar}.png"
        else:
            avatar_url = "No Avatar"
    except:
        avatar_url = "No Avatar"
    
    try:
        app_response = requests.get(f"https://discord.com/api/v9/applications/{bot_id}/rpc", headers=headers)
        if app_response.status_code == 200:
            app_info     = app_response.json()
            description  = app_info.get("description", "None")
            bot_public   = app_info.get("bot_public", "Unknown")
            bot_require_code_grant = app_info.get("bot_require_code_grant", "Unknown")
            verify_key   = app_info.get("verify_key", "None")
        else:
            description  = "None"
            bot_require_code_grant = "Unknown"
            verify_key   = "None"
    except:
        description  = "None"
        bot_require_code_grant = "Unknown"
        verify_key   = "None"
    
    try:
        guilds_response = requests.get("https://discord.com/api/v9/users/@me/guilds", headers=headers)
        if guilds_response.status_code == 200:
            guilds       = guilds_response.json()
            guild_count  = len(guilds)
        else:
            guild_count  = "None"
    except:
        guild_count = "None"
    
    Scroll(f"""
    {red}[{white}>{red}]{white} Status        {red}:{white} {red}{status}
    {red}[{white}>{red}]{white} Username      {red}:{white} {red}{username}
    {red}[{white}>{red}]{white} ID            {red}:{white} {red}{bot_id}
    {red}[{white}>{red}]{white} Discriminator {red}:{white} {red}{discriminator if discriminator and discriminator != "0" else "None"}
    {red}[{white}>{red}]{white} Created       {red}:{white} {red}{created_at}
    {red}[{white}>{red}]{white} Avatar        {red}:{white} {red}{avatar_url}
    {red}[{white}>{red}]{white} Description   {red}:{white} {red}{description}
    {red}[{white}>{red}]{white} Public Bot    {red}:{white} {red}{bot_public}
    {red}[{white}>{red}]{white} Code Grant    {red}:{white} {red}{bot_require_code_grant}
    {red}[{white}>{red}]{white} Flags         {red}:{white} {red}{flags}
    {red}[{white}>{red}]{white} Public Flags  {red}:{white} {red}{public_flags}
    {red}[{white}>{red}]{white} Accent Color  {red}:{white} {red}{accent_color if accent_color else "None"}
    {red}[{white}>{red}]{white} Banner        {red}:{white} {red}{banner if banner else "None"}
    {red}[{white}>{red}]{white} Banner Color  {red}:{white} {red}{banner_color if banner_color else "None"}
    {red}[{white}>{red}]{white} Verify Key    {red}:{white} {red}{verify_key}
    {red}[{white}>{red}]{white} Guild Count   {red}:{white} {red}{guild_count}
    """)

    Continue()
    Reset()

except Exception as e:
    Error(e)