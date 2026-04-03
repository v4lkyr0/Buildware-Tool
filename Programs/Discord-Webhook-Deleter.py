# Copyright (c) 2025 v4lkyr0
# See LICENSE file for details

from Plugins.Utils import *
from Plugins.Config import *

try:
    import requests
except Exception as e:
    MissingModule(e)

Title("Discord Webhook Deleter")
Connection()

try:
    webhook = ChoiceWebhook()

    print(f"{INFO} Deleting Webhook..", reset)

    try:
        response = requests.delete(webhook)
        if response.status_code == 204:
            print(f"{SUCCESS} Webhook deleted!", reset)
        else:
            print(f"{ERROR} Failed to delete Webhook!", reset)
    except:
        print(f"{ERROR} Error while trying to delete the Webhook!", reset)

    Continue()
    Reset()

except Exception as e:
    Error(e)