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
    import os
    import shutil
    import psutil
    import ctypes
    import time
    import winreg
except Exception as e:
    MissingModule(e)

Title("Injection Cleaner")
Connection()

Scroll(GradientBanner(discord_banner))

if platform_pc != "Windows":
    print(f"{ERROR} This feature is only available on Windows!", reset)
    Continue()
    Reset()

paths = {
    'Discord'             : os.path.join(os.getenv('LOCALAPPDATA', ''), 'Discord'),
    'Discord Ptb'         : os.path.join(os.getenv('LOCALAPPDATA', ''), 'DiscordPTB'),
    'Discord Canary'      : os.path.join(os.getenv('LOCALAPPDATA', ''), 'DiscordCanary'),
    'Discord Development' : os.path.join(os.getenv('LOCALAPPDATA', ''), 'DiscordDevelopment'),
    'Lightcord'           : os.path.join(os.getenv('APPDATA', ''), 'Lightcord'),
    'Discord Scoop'       : os.path.join(os.getenv('USERPROFILE', ''), 'scoop', 'apps', 'discord', 'current'),
    'BetterDiscord'       : os.path.join(os.getenv('APPDATA', ''), 'BetterDiscord'),
}

discord_processes = ['Discord.exe', 'DiscordPTB.exe', 'DiscordCanary.exe', 'DiscordDevelopment.exe', 'Lightcord.exe']

def FindModules(base_path):
    modules = []
    try:
        for entry in sorted(os.listdir(base_path), reverse=True):
            if not entry.startswith('app'):
                continue
            app_path   = os.path.join(base_path, entry)
            if not os.path.isdir(app_path):
                continue
            modules_dir = os.path.join(app_path, 'modules')
            if not os.path.exists(modules_dir):
                continue
            for mod in os.listdir(modules_dir):
                if mod.startswith('discord_desktop_core'):
                    core = os.path.join(modules_dir, mod, 'discord_desktop_core')
                    if os.path.exists(core):
                        modules.append(core)
    except:
        pass
    return modules

def CleanModule(module_path):
    index_file  = os.path.join(module_path, 'index.js')
    backup_file = os.path.join(module_path, 'index.js.bak')
    if not os.path.exists(index_file):
        return 'missing'
    try:
        with open(index_file, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        if '_0xW' not in content:
            return 'clean'
        if os.path.exists(backup_file):
            shutil.copy2(backup_file, index_file)
            os.remove(backup_file)
            return 'restored'
        idx = content.find('module.exports')
        if idx != -1:
            with open(index_file, 'w', encoding='utf-8') as f:
                f.write(content[idx:])
            return 'stripped'
        return 'invalid'
    except:
        return 'error'

def KillDiscord():
    killed = []
    for proc in psutil.process_iter(['name']):
        try:
            if proc.info['name'] in discord_processes:
                proc.kill()
                killed.append(proc.info['name'].replace('.exe', ''))
        except:
            pass
    return list(set(killed))

def RestartDiscord():
    started    = []
    restart_paths = {
        'Discord'            : os.path.join(os.getenv('LOCALAPPDATA', ''), 'Discord'),
        'DiscordPTB'         : os.path.join(os.getenv('LOCALAPPDATA', ''), 'DiscordPTB'),
        'DiscordCanary'      : os.path.join(os.getenv('LOCALAPPDATA', ''), 'DiscordCanary'),
        'DiscordDevelopment' : os.path.join(os.getenv('LOCALAPPDATA', ''), 'DiscordDevelopment'),
    }
    for name, path in restart_paths.items():
        exe = os.path.join(path, 'Update.exe')
        if os.path.exists(exe):
            try:
                ctypes.windll.shell32.ShellExecuteW(None, 'open', exe, f'--processStart {name}.exe', None, 0)
                started.append(name)
            except:
                continue
    return started

def RemovePersistence():
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, 'Software\\Microsoft\\Windows\\CurrentVersion\\Run', 0, winreg.KEY_SET_VALUE | winreg.KEY_QUERY_VALUE)
        try:
            winreg.QueryValueEx(key, 'DiscordUpdate')
            winreg.DeleteValue(key, 'DiscordUpdate')
            winreg.CloseKey(key)
            return True
        except:
            winreg.CloseKey(key)
            return False
    except:
        return False

try:
    print(f"{LOADING} Scanning..", reset)

    infected = []

    for name, path in paths.items():
        if not os.path.exists(path):
            continue
        modules = FindModules(path)
        for module in modules:
            index_file = os.path.join(module, 'index.js')
            if not os.path.exists(index_file):
                continue
            with open(index_file, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            if '_0xW' in content:
                infected.append((name, module))

    if not infected:
        print(f"{SUCCESS} No injection found!", reset)
        Continue()
        Reset()

    print(f"{INFO} Found:{red} {len(infected)}{white} infected client(s)", reset)

    for name, path in infected:
        print(f"{ERROR} Client:{red} {name}{white} | Path:{red} {path}", reset)

    confirm = input(f"{INPUT} Remove all injections? {YESORNO} {red}->{reset} ").strip().lower()

    if confirm not in ["y", "yes"]:
        print(f"{INFO} Cancelled.", reset)
        Continue()
        Reset()

    print(f"{LOADING} Killing Discord processes..", reset)

    killed = KillDiscord()

    if killed:
        print(f"{SUCCESS} Killed:{red} {', '.join(killed)}", reset)
        time.sleep(2)

    cleaned = 0

    for name, module in infected:
        result = CleanModule(module)
        if result == 'restored':
            print(f"{SUCCESS} Client:{red} {name}{white} | Status:{red} Restored from backup", reset)
            cleaned += 1
        elif result == 'stripped':
            print(f"{SUCCESS} Client:{red} {name}{white} | Status:{red} Injection stripped", reset)
            cleaned += 1
        elif result == 'error':
            print(f"{ERROR} Client:{red} {name}{white} | Status:{red} Failed to clean", reset)

    print(f"{LOADING} Checking registry..", reset)

    if RemovePersistence():
        print(f"{SUCCESS} Registry startup entry removed!", reset)
    else:
        print(f"{INFO} No registry startup entry found.", reset)

    persist_files = [
        os.path.join(os.getenv('APPDATA', ''), 'Microsoft', 'DiscordUpdate.exe'),
        os.path.join(os.getenv('APPDATA', ''), 'Microsoft', 'DiscordUpdate.pyw'),
        os.path.join(os.getenv('APPDATA', ''), 'Microsoft', 'DiscordUpdate.py'),
    ]

    for pf in persist_files:
        if os.path.exists(pf):
            try:
                os.remove(pf)
                print(f"{SUCCESS} Removed:{red} {pf}", reset)
            except:
                print(f"{ERROR} Could not remove:{red} {pf}", reset)

    if killed:
        print(f"{LOADING} Restarting Discord..", reset)
        started = RestartDiscord()
        if started:
            print(f"{SUCCESS} Restarted:{red} {', '.join(started)}", reset)

    print(f"{SUCCESS} Cleaned:{red} {cleaned}/{len(infected)}{white} client(s)!", reset)

    Continue()
    Reset()

except Exception as e:
    Error(e)