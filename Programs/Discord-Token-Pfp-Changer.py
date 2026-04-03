# Copyright (c) 2025 v4lkyr0
# See LICENSE file for details

from Plugins.Utils import *
from Plugins.Config import *

try:
    import requests
    from tkinter import filedialog
    import tkinter as tk
    import base64
    from pathlib import Path
except Exception as e:
    MissingModule(e)

Title("Discord Token Pfp Changer")
Connection()

try:
    token = ChoiceToken()

    def HasNitro(token):
        try:
            headers = {"Authorization": token, "User-Agent": RandomUserAgents()}
            response = requests.get("https://discord.com/api/v9/users/@me", headers=headers)
            if response.status_code == 200:
                user = response.json()
                return user.get("premium_type", 0) in [1, 2]
        except:
            pass
        return False

    def ChoicePfp():
        root = tk.Tk()
        root.withdraw()

        try:
            root.iconbitmap(os.path.join(tool_path, 'Programs', 'Images', 'BuildwareIcon.ico'))
        except:
            pass

        if HasNitro(token):
            file_types = [("Image Files", "*.png;*.jpg;*.jpeg;*.gif")]
        else:
            file_types = [("Image Files", "*.png;*.jpg;*.jpeg")]

        file_path = filedialog.askopenfilename(title=f"{name_tool} {version_tool} - Select Profile Picture", filetypes=file_types)
        return file_path
    
    def ChangePfp(token, pfp_path):
        print(f"{INFO} Changing Profile Picture..", reset)

        url = "https://discord.com/api/v9/users/@me"

        headers = {"Authorization": token, "Content-Type": "application/json", "User-Agent": RandomUserAgents()}

        try:
            with open(pfp_path, "rb") as pfp_file:
                pfp_data = base64.b64encode(pfp_file.read()).decode('utf-8')

            ext = Path(pfp_path).suffix.lower()
            mime_type = {
                ".png": "image/png",
                ".jpg": "image/jpeg",
                ".jpeg": "image/jpeg",
                ".gif": "image/gif"
            }
            mime_type = mime_type.get(ext, "image/png")

            avatar_data = f"data:{mime_type};base64,{pfp_data}"
            payload     = {"avatar": avatar_data}

            try:
                response = requests.patch(url, headers=headers, json=payload)
                if response.status_code == 200:
                    print(f"{SUCCESS} Profile Picture changed!", reset)
                    return response.json()
                else:
                    print(f"{ERROR} Failed to change Profile Picture!", reset)
                    return None
            except:
                print(f"{ERROR} Error while trying to change Profile Picture!", reset)
                return None

        except:
            print(f"{ERROR} Could not read the Image file!", reset)
            return None

    print(f"{INPUT} Select Image {red}->", reset)
    
    pfp_path = ChoicePfp()
    if not pfp_path:
        print(f"{ERROR} No Image selected!", reset)
        time.sleep(2)
        Reset()

    print(f"{INFO} Image selected:{red} {pfp_path}", reset)

    ChangePfp(token, pfp_path)
    Continue()
    Reset()

except Exception as e:
    Error(e)