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
    import base64
    import json
except Exception as e:
    MissingModule(e)

Title("Jwt Decoder")
Connection()

Scroll(GradientBanner(utilities_banner))

def DecodeSegment(segment):
    padding = 4 - len(segment) % 4
    if padding != 4:
        segment += "=" * padding
    return json.loads(base64.urlsafe_b64decode(segment).decode())

try:
    token = input(f"{INPUT} Token {red}->{reset} ").strip()

    if not token:
        ErrorInput()

    print(f"{LOADING} Decoding..", reset)

    parts = token.split(".")

    if len(parts) != 3:
        print(f"{ERROR} Invalid Jwt token!", reset)
        Continue()
        Reset()

    try:
        header    = DecodeSegment(parts[0])
        payload   = DecodeSegment(parts[1])

        print(f"{SUCCESS} Header:", reset)
        for key, value in header.items():
            print(f"   {SUCCESS} {key:<12}{red} {value}", reset)

        print(f"{SUCCESS} Payload:", reset)
        for key, value in payload.items():
            print(f"   {SUCCESS} {key:<12}{red} {value}", reset)

        print(f"{SUCCESS} Signature:{red} {parts[2]}", reset)
    except:
        print(f"{ERROR} Could not decode Jwt token!", reset)

    Continue()
    Reset()

except Exception as e:
    Error(e)