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

Title("Bot Raider")
Connection()

Scroll(GradientBanner(discord_banner))

try:
    bot_token = ChoiceBot()

    server_id = input(f"{INPUT} Server Id {red}->{reset} ").strip()
    if not server_id:
        ErrorId()

    message = input(f"{INPUT} Message {red}->{reset} ").strip()
    if not message:
        ErrorInput()

    try:
        message_limit = int(input(f"{INPUT} Total Messages {red}->{reset} ").strip())
        if message_limit < 0:
            message_limit = 0
    except:
        message_limit = 0

    try:
        delay = float(input(f"{INPUT} Delay {red}->{reset} ").strip())
        if delay < 0.1:
            delay = 0.1
    except:
        delay = 0.5

    headers = {"Authorization": f"Bot {bot_token}", "Content-Type": "application/json", "User-Agent": RandomUserAgents()}

    print(f"{LOADING} Fetching channels..", reset)

    channels_response = requests.get(f"https://discord.com/api/v9/guilds/{server_id}/channels", headers=headers)

    if channels_response.status_code != 200:
        print(f"{ERROR} Could not fetch channels!", reset)
        Continue()
        Reset()

    channels      = channels_response.json()
    text_channels = [c for c in channels if c.get("type") == 0]

    if not text_channels:
        print(f"{ERROR} No text channels found!", reset)
        Continue()
        Reset()

    print(f"{SUCCESS} Found:{red} {len(text_channels)}{white} channel(s)", reset)
    print(f"{LOADING} Starting raid..", reset)

    message_count = 0

    while True:
        if message_limit > 0 and message_count >= message_limit:
            break

        for channel in text_channels:
            try:
                channel_id   = channel.get("id")
                channel_name = channel.get("name", "Unknown")

                response = requests.post(
                    f"https://discord.com/api/v9/channels/{channel_id}/messages",
                    headers=headers,
                    json={"content": message}
                )

                if response.status_code in [200, 201]:
                    message_count += 1
                    print(f"{SUCCESS} Messages:{red} {message_count:<6}{white} | Channel:{red} {channel_name}", reset)
                else:
                    print(f"{ERROR} Status:{red} Failed  {white}| Channel:{red} {channel_name}", reset)

                time.sleep(delay)

            except KeyboardInterrupt:
                print(f"{INFO} Total messages sent:{red} {message_count}", reset)
                Continue()
                Reset()

    print(f"{INFO} Total messages sent:{red} {message_count}", reset)

    Continue()
    Reset()

except Exception as e:
    Error(e)