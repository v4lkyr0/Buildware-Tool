# Copyright (c) 2025 v4lkyr0
# See LICENSE file for details

from Plugins.Utils import *
from Plugins.Config import *

try:
    import requests
except Exception as e:
    MissingModule(e)

Title("Discord Token Alias Changer")
Connection()

try:
    token     = ChoiceToken()
    new_alias = input(f"{INPUT} Alias {red}->{reset} ")

    headers = {
        'Authorization': token,
        'Content-Type': 'application/json',
        'User-Agent': RandomUserAgents(),
        'X-Super-Properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImZyLUZSIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEyMC4wLjAuMCBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTIwLjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjI1MDAwMCwiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0='
    }

    url  = "https://discord.com/api/v9/users/@me"
    data = {"global_name": new_alias}

    try:
        response = requests.patch(url, json=data, headers=headers)
        if response.status_code == 200:
            print(f"{SUCCESS} Successfully changed Alias!", reset)
        else:
            print(f"{ERROR} Failed to change Alias!", reset)
    except:
        print(f"{ERROR} Error while trying to change Alias!", reset)

    Continue()
    Reset()

except Exception as e:
    Error(e)