from Plugins.Utils import *
from Plugins.Config import *

try:
    import requests
    import time
except Exception as e:
    MissingModule(e)

Title("Discord Token Ghost Pinger")
Connection()

try:
    token   = ChoiceToken()
    message = input(f"{INPUT} Message {red}->{reset} ")
    if not message:
        ErrorInput()

    delay = input(f"{INPUT} Delay Pings {red}->{reset} ").strip()
    try:
        delay = float(delay)
    except:
        delay = 0.5

    print(f"{LOADING} Fetching Friends..", reset)

    headers = {
        "Authorization": token,
        "Content-Type": "application/json",
        "User-Agent": RandomUserAgents()
    }

    relationships = requests.get(
        "https://discord.com/api/v9/users/@me/relationships",
        headers=headers
    ).json()

    friends = [r for r in relationships if r.get("type") == 1]

    if not friends:
        print(f"{ERROR} No Friends found!", reset)
        Continue()
        Reset()

    print(f"{INFO} {len(friends)} Friend(s) found!", reset)
    print(f"{LOADING} Starting Ghost Pinger..", reset)

    for friend in friends:
        user_id  = friend["id"]
        username = friend["user"]["username"]

        try:
            dm_response = requests.post(
                "https://discord.com/api/v9/users/@me/channels",
                headers=headers,
                json={"recipient_id": user_id}
            )

            if dm_response.status_code != 200:
                print(f"{ERROR} Status:{red} Failed  {white}| Username:{red} {username}", reset)
                continue

            channel_id = dm_response.json()["id"]

            ping_response = requests.post(
                f"https://discord.com/api/v9/channels/{channel_id}/messages",
                headers=headers,
                json={"content": f"<@{user_id}>"}
            )

            if ping_response.status_code not in [200, 201]:
                print(f"{ERROR} Status:{red} Failed  {white}| Username:{red} {username}", reset)
                continue

            ping_message_id = ping_response.json()["id"]
            time.sleep(0.3)

            edit_response = requests.patch(
                f"https://discord.com/api/v9/channels/{channel_id}/messages/{ping_message_id}",
                headers=headers,
                json={"content": message}
            )

            if edit_response.status_code == 200:
                print(f"{SUCCESS} Status:{red} Pinged  {white}| Username:{red} {username}", reset)
            else:
                print(f"{ERROR} Status:{red} Failed  {white}| Username:{red} {username}", reset)

        except:
            print(f"{ERROR} Status:{red} Error   {white}| Username:{red} {username}", reset)

        time.sleep(delay)

    Continue()
    Reset()

except Exception as e:
    Error(e)