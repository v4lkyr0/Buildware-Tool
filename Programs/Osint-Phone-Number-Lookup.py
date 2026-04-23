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
    import phonenumbers
    from phonenumbers import geocoder, carrier, timezone
except Exception as e:
    MissingModule(e)

Title("Phone Number Lookup")
Connection()

Scroll(GradientBanner(osint_banner))

try:
    phone = input(f"{INPUT} Phone Number {red}->{reset} ").strip()

    if not phone:
        ErrorInput()

    print(f"{LOADING} Looking up..", reset)

    try:
        parsed   = phonenumbers.parse(phone)

        if not phonenumbers.is_valid_number(parsed):
            print(f"{ERROR} Invalid phone number!", reset)
            Continue()
            Reset()

        country  = geocoder.description_for_number(parsed, "en")
        operator = carrier.name_for_number(parsed, "en")
        zones    = timezone.time_zones_for_number(parsed)
        format1  = phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
        format2  = phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.NATIONAL)
        format3  = phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.E164)

        Scroll(f"""
 {SUCCESS} Number   :{red} {format1}{white}
 {SUCCESS} National :{red} {format2}{white}
 {SUCCESS} E164     :{red} {format3}{white}
 {SUCCESS} Country  :{red} {country if country else 'Unknown'}{white}
 {SUCCESS} Carrier  :{red} {operator if operator else 'Unknown'}{white}
 {SUCCESS} Timezone :{red} {', '.join(zones) if zones else 'Unknown'}{white}
 {SUCCESS} Valid    :{red} {phonenumbers.is_valid_number(parsed)}{white}
 {SUCCESS} Possible :{red} {phonenumbers.is_possible_number(parsed)}{white}
""")
    except:
        print(f"{ERROR} Invalid phone number!", reset)

    Continue()
    Reset()

except Exception as e:
    Error(e)