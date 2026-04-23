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
    import random
    from datetime import datetime, timezone
except Exception as e:
    MissingModule(e)

Title("Feedback")

Scroll(GradientBanner(feedback_banner))

try:
    _fk      = b"bw-feedback-v4lkyr0"
    _fw_list = [
        "CgNZFhZfS00FChhOGUYIRRodXU0WXQ9KEgEACQwERgUbXV9AQwhbQBlRU1VQU1RQUhhOAUM5DDxdKxxYJBw3ECwzBgZkPnhUDys+bwsbFBEuDQwgJRo6ajxcJjweHmIYGXg3DA0wI1kHIV8lYgkdKT1ZED5YL10tEw==",
        "CgNZFhZfS00FChhOGUYIRRodXU0WXQ9KEgEACQwERgUbXV9AQwlSRxhXXFRSWlJXUx5CB0M8CD1eCBJ8MQwSSVUKOSldOUU8JAE4fDslHBMjPTIzBisYeBtyWg81G3Y4WhU5FAwSElQnL3ERCssOgdzMw5oNlIyVA==",
        "CgNZFhZfS00FChhOGUYIRRodXU0WXQ9KEgEACQwERgUbXV9AQwlSRxhUVlFQUFdTWRxBDEM4STRAKSFiEVUsDTgAIFNLP009BTIAU1oBFSxUDx43LFsJbDJzBClUOAYtMWwXVhAzDBgsIRgwZQABMz9WVyEZCToxLQ==",
        "CgNZFhZfS00FChhOGUYIRRodXU0WXQ9KEgEACQwERgUbXV9AQwlSRxhUXVBTU1hUXBpDDEM8MidoLwMaKz06MDQVGy9gBVkEMRdHWixaXCIxOgk7LgYKfhJxLQ4jHQU6EVQXAiQOCi4bWxQEYF4BIDRJN0JbVSczIg==",
        "CgNZFhZfS00FChhOGUYIRRodXU0WXQ9KEgEACQwERgUbXV9AQwlSRxhVV1JTVlhQWRhDBUMHQTtDLUUbVjAOOyAEBQ5cJW0rBDVDdwk9TxYhBlwhDjwoXg5eLRwLB28oNGMHNRBXOgkEAxgEBy86MyVyAzJ6ICsNIw==",
    ]

    def GetWebhooks():
        webhooks = []
        for enc in _fw_list:
            try:
                r = base64.b64decode(enc.strip())
                webhooks.append(bytes([b ^ _fk[i % len(_fk)] for i, b in enumerate(r)]).decode())
            except:
                continue
        return webhooks

    Connection()

    ratings = {
        "01": 1, "02": 2, "03": 3, "04": 4, "05": 5,
        "1": 1,  "2": 2,  "3": 3,  "4": 4,  "5": 5,
    }

    Scroll(f"""
 {INFO} Rate your experience!

 {PREFIX1}01{SUFFIX1} 1/5
 {PREFIX1}02{SUFFIX1} 2/5
 {PREFIX1}03{SUFFIX1} 3/5
 {PREFIX1}04{SUFFIX1} 4/5
 {PREFIX1}05{SUFFIX1} 5/5
""")

    choice = input(f"{INPUT} Rating {red}->{reset} ").strip()

    if choice not in ratings:
        ErrorChoice()

    rating  = ratings[choice]
    message = input(f"{INPUT} Message {red}->{reset} ").strip()

    if not message:
        ErrorInput()

    print(f"{LOADING} Sending..", reset)

    embed = {
        "title"    : "New Feedback!",
        "color"    : color_embed,
        "thumbnail": {"url": avatar_webhook},
        "fields"   : [
            {"name": "Rating",   "value": f"```{rating}/5```",     "inline": True},
            {"name": "Username", "value": f"```{username_pc}```",  "inline": True},
            {"name": "Platform", "value": f"```{platform_pc}```",  "inline": True},
            {"name": "Version",  "value": f"```{version_tool}```", "inline": True},
            {"name": "Message",  "value": f"```{message}```",      "inline": False},
        ],
        "footer"   : {"text": name_tool, "icon_url": avatar_webhook},
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }

    payload = {
        "username"  : f"{username_webhook} | Feedback",
        "avatar_url": avatar_webhook,
        "embeds"    : [embed],
    }

    url      = random.choice(GetWebhooks())
    response = requests.post(url, json=payload, timeout=10)

    if response.status_code in [200, 204]:
        print(f"{SUCCESS} Feedback sent!", reset)
    else:
        print(f"{ERROR} Could not send feedback!", reset)

    Continue()
    Reset()

except Exception as e:
    Error(e)