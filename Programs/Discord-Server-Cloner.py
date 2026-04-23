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

Title("Server Cloner")
Connection()

Scroll(GradientBanner(discord_banner))

try:
    token = ChoiceToken()

    source_id = input(f"{INPUT} Source Server Id {red}->{reset} ").strip()
    if not source_id:
        ErrorId()

    target_id = input(f"{INPUT} Target Server Id {red}->{reset} ").strip()
    if not target_id:
        ErrorId()

    headers = {"Authorization": token, "Content-Type": "application/json", "User-Agent": RandomUserAgents()}

    print(f"{LOADING} Fetching servers..", reset)

    source_response = requests.get(f"https://discord.com/api/v9/guilds/{source_id}", headers=headers)

    if source_response.status_code != 200:
        print(f"{ERROR} Could not access source server!", reset)
        Continue()
        Reset()

    target_response = requests.get(f"https://discord.com/api/v9/guilds/{target_id}", headers=headers)

    if target_response.status_code != 200:
        print(f"{ERROR} Could not access target server!", reset)
        Continue()
        Reset()

    source_name = source_response.json().get("name", "Unknown")
    target_name = target_response.json().get("name", "Unknown")

    print(f"{SUCCESS} Source:{red} {source_name}", reset)
    print(f"{SUCCESS} Target:{red} {target_name}", reset)

    print(f"{LOADING} Deleting target channels..", reset)

    channels_response = requests.get(f"https://discord.com/api/v9/guilds/{target_id}/channels", headers=headers)

    if channels_response.status_code == 200:
        for channel in channels_response.json():
            requests.delete(f"https://discord.com/api/v9/channels/{channel['id']}", headers=headers)
            print(f"{SUCCESS} Deleted:{red} {channel.get('name', 'Unknown')}", reset)
            time.sleep(0.3)

    print(f"{LOADING} Cloning channels..", reset)

    source_channels_response = requests.get(f"https://discord.com/api/v9/guilds/{source_id}/channels", headers=headers)

    if source_channels_response.status_code == 200:
        source_channels = sorted(source_channels_response.json(), key=lambda x: x.get("position", 0))

        for channel in source_channels:
            channel_data = {
                "name"                 : channel.get("name"),
                "type"                 : channel.get("type"),
                "topic"                : channel.get("topic"),
                "position"             : channel.get("position"),
                "permission_overwrites": channel.get("permission_overwrites", []),
                "nsfw"                 : channel.get("nsfw", False),
                "rate_limit_per_user"  : channel.get("rate_limit_per_user", 0),
            }

            create_response = requests.post(
                f"https://discord.com/api/v9/guilds/{target_id}/channels",
                headers=headers,
                json=channel_data
            )

            if create_response.status_code == 201:
                print(f"{SUCCESS} Created:{red} {channel.get('name', 'Unknown')}", reset)
            else:
                print(f"{ERROR} Failed:{red} {channel.get('name', 'Unknown')}", reset)

            time.sleep(0.5)

    print(f"{SUCCESS} Server cloned!", reset)

    Continue()
    Reset()

except Exception as e:
    Error(e)