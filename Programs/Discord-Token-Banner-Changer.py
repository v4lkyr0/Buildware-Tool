# Copyright (c) 2026 v4lkyr0
# See LICENSE file for details

from Plugins.Utils import *
from Plugins.Config import *

try:
    import base64
    import requests
except Exception as e:
    MissingModule(e)

Title("Discord Token Banner Changer")
Connection()

try:
    token = ChoiceToken()
    banner_path = input(f"{INPUT} Banner Path {red}->{reset} ")

    if not banner_path or not os.path.exists(banner_path):
        print(f"{ERROR} Invalid file path!", reset)
        Continue()
        Reset()

    print(f"{LOADING} Changing Banner..", reset)

    SUPPORTED_FORMATS = {
        "png": "image/png",
        "jpg": "image/jpeg",
        "jpeg": "image/jpeg",
        "gif": "image/gif"
    }
    
    with open(banner_path, "rb") as f:
        banner_data = f.read()

    file_extension = banner_path.split(".")[-1].lower()
    
    if file_extension not in SUPPORTED_FORMATS:
        print(f"{ERROR} Unsupported file format! Use PNG, JPG, or GIF", reset)
        Continue()
        Reset()
    
    mime_type = SUPPORTED_FORMATS[file_extension]

    encoded_banner = base64.b64encode(banner_data).decode("utf-8")
    banner_string = f"data:{mime_type};base64,{encoded_banner}"

    headers = {"Authorization": token, "Content-Type": "application/json", "User-Agent": RandomUserAgents()}
    
    response = requests.patch("https://discord.com/api/v9/users/@me", headers=headers, json={"banner": banner_string})

    if response.status_code == 200:
        print(f"{SUCCESS} Banner changed!", reset)
    else:
        print(f"{ERROR} Failed to change Banner!", reset)

    Continue()
    Reset()

except Exception as e:
    Error(e)
