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
    import hashlib
    import os
except Exception as e:
    MissingModule(e)

Title("File Hasher")
Connection()

Scroll(GradientBanner(utilities_banner))

try:
    if tk is None:
        print(f"{ERROR} Tkinter is not available!", reset)
        Continue()
        Reset()

    file_path = BrowseFile("Select File")

    if not file_path:
        ErrorInput()

    if not os.path.exists(file_path):
        print(f"{ERROR} File not found!", reset)
        Continue()
        Reset()

    print(f"{LOADING} Hashing..", reset)

    with open(file_path, "rb") as f:
        data = f.read()

    md5    = hashlib.md5(data).hexdigest()
    sha1   = hashlib.sha1(data).hexdigest()
    sha256 = hashlib.sha256(data).hexdigest()
    sha512 = hashlib.sha512(data).hexdigest()

    Scroll(f"""
 {SUCCESS} File   :{red} {os.path.basename(file_path)}{white}
 {SUCCESS} Size   :{red} {round(os.path.getsize(file_path) / 1024, 2)} Kb{white}
 {SUCCESS} Md5    :{red} {md5}{white}
 {SUCCESS} Sha1   :{red} {sha1}{white}
 {SUCCESS} Sha256 :{red} {sha256}{white}
 {SUCCESS} Sha512 :{red} {sha512}{white}
""")

    Continue()
    Reset()

except Exception as e:
    Error(e)