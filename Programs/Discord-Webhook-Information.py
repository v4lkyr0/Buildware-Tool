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
except Exception as e:
    MissingModule(e)

Title("Webhook Information")
Connection()

Scroll(GradientBanner(discord_banner))

try:
    webhook = ChoiceWebhook()

    print(f"{LOADING} Fetching..", reset)

    response = requests.get(webhook, headers={"User-Agent": RandomUserAgents()})

    if response.status_code != 200:
        print(f"{ERROR} Could not fetch webhook information!", reset)
        Continue()
        Reset()

    data           = response.json()
    webhook_id     = data.get("id", "None")
    webhook_name   = data.get("name", "None")
    webhook_token  = webhook.split("/")[-1] if "/" in webhook else "None"
    webhook_avatar = data.get("avatar")
    webhook_avatar_url = f"https://cdn.discordapp.com/avatars/{webhook_id}/{webhook_avatar}.png" if webhook_avatar else "None"
    webhook_creator    = data.get("user", {}).get("username", "None") if "user" in data else "None"
    webhook_server_id  = data.get("guild_id", "None")
    webhook_channel_id = data.get("channel_id", "None")

    type_map     = {1: "Incoming Webhook", 2: "Channel Follower Webhook", 3: "Application Webhook"}
    webhook_type = type_map.get(data.get("type"), "None")

    Scroll(f"""
 {SUCCESS} Url        :{red} {webhook}{white}
 {SUCCESS} Id         :{red} {webhook_id}{white}
 {SUCCESS} Name       :{red} {webhook_name}{white}
 {SUCCESS} Token      :{red} {webhook_token}{white}
 {SUCCESS} Avatar Url :{red} {webhook_avatar_url}{white}
 {SUCCESS} Type       :{red} {webhook_type}{white}
 {SUCCESS} Server Id  :{red} {webhook_server_id}{white}
 {SUCCESS} Channel Id :{red} {webhook_channel_id}{white}
 {SUCCESS} Creator    :{red} {webhook_creator}{white}
""")

    Continue()
    Reset()

except Exception as e:
    Error(e)