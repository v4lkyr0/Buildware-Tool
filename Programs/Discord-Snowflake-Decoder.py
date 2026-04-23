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
    from datetime import datetime
except Exception as e:
    MissingModule(e)

Title("Snowflake Decoder")

Scroll(GradientBanner(discord_banner))

def DecodeSnowflake(snowflake):
    try:
        snowflake_int = int(snowflake)
        timestamp_ms  = (snowflake_int >> 22) + 1420070400000
        timestamp     = datetime.fromtimestamp(timestamp_ms / 1000.0)
        worker_id     = (snowflake_int & 0x3E0000) >> 17
        process_id    = (snowflake_int & 0x1F000) >> 12
        increment     = snowflake_int & 0xFFF

        return {
            'valid'       : True,
            'snowflake'   : snowflake,
            'timestamp'   : timestamp,
            'timestamp_ms': timestamp_ms,
            'worker_id'   : worker_id,
            'process_id'  : process_id,
            'increment'   : increment,
            'binary'      : bin(snowflake_int)[2:].zfill(64),
        }
    except:
        return {'valid': False}

try:
    snowflake = input(f"{INPUT} Snowflake Id {red}->{reset} ").strip()

    if not snowflake:
        ErrorId()

    print(f"{LOADING} Decoding..", reset)

    result = DecodeSnowflake(snowflake)

    if not result['valid']:
        ErrorId()

    now            = datetime.now()
    age            = now - result['timestamp']
    days           = age.days
    years          = days // 365
    remaining_days = days % 365

    Scroll(f"""
 {SUCCESS} Snowflake Id    :{red} {snowflake}{white}
 {SUCCESS} Created At      :{red} {result['timestamp'].strftime('%Y-%m-%d %H:%M:%S')}{white}
 {SUCCESS} Timestamp {red}({white}ms{red}){white}  :{red} {result['timestamp_ms']}{white}
 {SUCCESS} Worker Id       :{red} {result['worker_id']}{white}
 {SUCCESS} Process Id      :{red} {result['process_id']}{white}
 {SUCCESS} Increment       :{red} {result['increment']}{white}
 {SUCCESS} Binary          :{red} {result['binary']}{white}
 {SUCCESS} Age             :{red} {years} years, {remaining_days} days{white}
""")

    Continue()
    Reset()

except Exception as e:
    Error(e)