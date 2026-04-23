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
    import webbrowser
    import os
except Exception as e:
    MissingModule(e)

Title("Reverse Image Search")
Connection()

Scroll(GradientBanner(osint_banner))

try:
    Scroll(f"""
 {PREFIX}01{SUFFIX} Image Path
 {PREFIX}02{SUFFIX} Image Url
""")

    choice = input(f"{INPUT} Choice {red}->{reset} ").strip().lstrip("0")

    if choice == "1":
        if tk is None:
            print(f"{ERROR} Tkinter is not available!", reset)
            Continue()
            Reset()
        image_path = BrowseFile("Select Image", [("Image Files", "*.png *.jpg *.jpeg *.gif *.bmp *.webp")])
        if not image_path:
            ErrorInput()
        if not os.path.exists(image_path):
            print(f"{ERROR} File not found!", reset)
            Continue()
            Reset()
        print(f"{LOADING} Uploading..", reset)
        try:
            with open(image_path, "rb") as f:
                response = requests.post("https://litterbox.catbox.moe/resources/internals/api.php", data={"reqtype": "fileupload", "time": "1h"}, files={"fileToUpload": f}, timeout=15)
            if response.status_code == 200:
                url = response.text.strip()
            else:
                print(f"{ERROR} Upload failed!", reset)
                Continue()
                Reset()
        except:
            print(f"{ERROR} Upload failed!", reset)
            Continue()
            Reset()
    elif choice == "2":
        url = input(f"{INPUT} Image Url {red}->{reset} ").strip()
        if not url:
            ErrorInput()
    else:
        ErrorChoice()

    print(f"{LOADING} Opening..", reset)

    webbrowser.open(f"https://lens.google.com/uploadbyurl?url={url}")
    webbrowser.open(f"https://yandex.com/images/search?url={url}&rpt=imageview")
    webbrowser.open(f"https://tineye.com/search?url={url}")

    print(f"{SUCCESS} Opened in browser!", reset)

    Continue()
    Reset()

except Exception as e:
    Error(e)