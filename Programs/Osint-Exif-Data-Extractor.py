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
    from PIL import Image
    from PIL.ExifTags import TAGS, GPSTAGS
    import os
except Exception as e:
    MissingModule(e)

Title("Exif Data Extractor")

Scroll(GradientBanner(osint_banner))

def GetGps(exif_raw):
    try:
        gps_info = {}
        for tag, value in exif_raw.items():
            decoded = TAGS.get(tag, tag)
            if decoded == "GPSInfo":
                for t, v in value.items():
                    gps_info[GPSTAGS.get(t, t)] = v

        if not gps_info:
            return None, None, None, None

        def ToDegrees(value):
            d, m, s = value
            return float(d) + float(m) / 60 + float(s) / 3600

        lat      = ToDegrees(gps_info["GPSLatitude"])
        lon      = ToDegrees(gps_info["GPSLongitude"])
        altitude = gps_info.get("GPSAltitude", None)
        speed    = gps_info.get("GPSSpeed", None)

        if gps_info.get("GPSLatitudeRef")  == "S": lat = -lat
        if gps_info.get("GPSLongitudeRef") == "W": lon = -lon

        return round(lat, 6), round(lon, 6), altitude, speed
    except Exception:
        return None, None, None, None

try:
    print(f"{INPUT} Select Image {red}->{reset} ", reset)

    filepath = BrowseFile("Select Image", [
        ("Image Files", "*.jpg;*.jpeg;*.png;*.tiff;*.tif;*.bmp;*.webp"),
        ("All Files",   "*.*")
    ])

    if not filepath:
        print(f"{ERROR} No file selected!", reset)
        Continue()
        Reset()

    if not os.path.exists(filepath):
        print(f"{ERROR} File not found!", reset)
        Continue()
        Reset()

    print(f"{SUCCESS} File:{red} {os.path.basename(filepath)}", reset)
    print(f"{LOADING} Extracting..", reset)

    try:
        img      = Image.open(filepath)
        exif_raw = img._getexif()
    except Exception:
        print(f"{ERROR} Could not open image!", reset)
        Continue()
        Reset()

    if not exif_raw:
        print(f"{ERROR} No Exif data found!", reset)
        Continue()
        Reset()

    exif_data = {}
    for tag, value in exif_raw.items():
        decoded = TAGS.get(tag, tag)
        if decoded != "MakerNote":
            exif_data[decoded] = value

    lat, lon, altitude, speed = GetGps(exif_raw)

    size     = os.path.getsize(filepath)
    size_str = f"{round(size / 1024 / 1024, 2)} MB" if size >= 1024 * 1024 else f"{round(size / 1024, 2)} KB"

    orientation_map = {
        1: "Normal", 2: "Mirrored", 3: "Rotated 180°", 4: "Mirrored 180°",
        5: "Mirrored 90° CW", 6: "Rotated 90° CW", 7: "Mirrored 90° CCW", 8: "Rotated 90° CCW",
    }

    flash_map = {
        0: "No Flash", 1: "Flash Fired", 5: "Flash Fired (No Strobe)", 7: "Flash Fired (Strobe)",
        9: "Flash Fired (Compulsory)", 16: "Flash Off", 24: "Flash Off (Auto)", 25: "Flash Fired (Auto)",
    }

    white_balance_map = {0: "Auto", 1: "Manual"}
    exposure_map      = {0: "Auto", 1: "Manual", 2: "Auto Bracket"}
    metering_map      = {0: "Unknown", 1: "Average", 2: "Center Weighted", 3: "Spot", 4: "Multi-Spot", 5: "Pattern", 6: "Partial"}
    light_map         = {0: "Unknown", 1: "Daylight", 2: "Fluorescent", 3: "Tungsten", 4: "Flash", 9: "Fine Weather", 10: "Cloudy", 11: "Shade"}

    def Get(key, default="None"):
        return str(exif_data.get(key, default)) if exif_data.get(key) is not None else "None"

    exposure = exif_data.get("ExposureTime")
    exposure_str = f"1/{round(1/float(exposure))}s" if exposure and float(exposure) < 1 else f"{exposure}s" if exposure else "None"

    focal = exif_data.get("FocalLength")
    focal_str = f"{round(float(focal), 1)}mm" if focal else "None"

    fnumber = exif_data.get("FNumber")
    fnumber_str = f"f/{round(float(fnumber), 1)}" if fnumber else "None"

    Scroll(f"""
 {SUCCESS} File Name       :{red} {os.path.basename(filepath)}{white}
 {SUCCESS} File Size       :{red} {size_str}{white}
 {SUCCESS} Format          :{red} {img.format or 'None'}{white}
 {SUCCESS} Mode            :{red} {img.mode or 'None'}{white}
 {SUCCESS} Dimensions      :{red} {img.size[0]}x{img.size[1]}{white}

 {SUCCESS} Make            :{red} {Get('Make')}{white}
 {SUCCESS} Model           :{red} {Get('Model')}{white}
 {SUCCESS} Software        :{red} {Get('Software')}{white}
 {SUCCESS} Artist          :{red} {Get('Artist')}{white}
 {SUCCESS} Copyright       :{red} {Get('Copyright')}{white}
 {SUCCESS} Host Computer   :{red} {Get('HostComputer')}{white}

 {SUCCESS} Date Time       :{red} {Get('DateTime')}{white}
 {SUCCESS} Date Original   :{red} {Get('DateTimeOriginal')}{white}
 {SUCCESS} Date Digitized  :{red} {Get('DateTimeDigitized')}{white}
 {SUCCESS} Offset Time     :{red} {Get('OffsetTime')}{white}
 {SUCCESS} SubSec Time     :{red} {Get('SubsecTimeOriginal')}{white}

 {SUCCESS} Exposure Time   :{red} {exposure_str}{white}
 {SUCCESS} F Number        :{red} {fnumber_str}{white}
 {SUCCESS} ISO             :{red} {Get('ISOSpeedRatings')}{white}
 {SUCCESS} Focal Length    :{red} {focal_str}{white}
 {SUCCESS} Flash           :{red} {flash_map.get(exif_data.get('Flash'), Get('Flash'))}{white}
 {SUCCESS} White Balance   :{red} {white_balance_map.get(exif_data.get('WhiteBalance'), Get('WhiteBalance'))}{white}
 {SUCCESS} Exposure Mode   :{red} {exposure_map.get(exif_data.get('ExposureMode'), Get('ExposureMode'))}{white}
 {SUCCESS} Metering Mode   :{red} {metering_map.get(exif_data.get('MeteringMode'), Get('MeteringMode'))}{white}
 {SUCCESS} Light Source    :{red} {light_map.get(exif_data.get('LightSource'), Get('LightSource'))}{white}
 {SUCCESS} Orientation     :{red} {orientation_map.get(exif_data.get('Orientation'), Get('Orientation'))}{white}
 {SUCCESS} Brightness      :{red} {Get('BrightnessValue')}{white}
 {SUCCESS} Sharpness       :{red} {Get('Sharpness')}{white}
 {SUCCESS} Saturation      :{red} {Get('Saturation')}{white}
 {SUCCESS} Contrast        :{red} {Get('Contrast')}{white}
 {SUCCESS} Digital Zoom    :{red} {Get('DigitalZoomRatio')}{white}
 {SUCCESS} Scene Type      :{red} {Get('SceneCaptureType')}{white}
 {SUCCESS} Color Space     :{red} {Get('ColorSpace')}{white}
 {SUCCESS} Sensing Method  :{red} {Get('SensingMethod')}{white}

 {SUCCESS} Width           :{red} {Get('ExifImageWidth', Get('ImageWidth'))}{white}
 {SUCCESS} Height          :{red} {Get('ExifImageHeight', Get('ImageLength'))}{white}
 {SUCCESS} X Resolution    :{red} {Get('XResolution')}{white}
 {SUCCESS} Y Resolution    :{red} {Get('YResolution')}{white}
 {SUCCESS} Compression     :{red} {Get('Compression')}{white}
 {SUCCESS} Bits Per Sample :{red} {Get('BitsPerSample')}{white}

 {SUCCESS} Latitude        :{red} {lat if lat else 'None'}{white}
 {SUCCESS} Longitude       :{red} {lon if lon else 'None'}{white}
 {SUCCESS} Altitude        :{red} {round(float(altitude), 2) if altitude else 'None'}{white}
 {SUCCESS} Speed           :{red} {round(float(speed), 2) if speed else 'None'}{white}
 {SUCCESS} Google Maps     :{red} {'https://www.google.com/maps?q=' + str(lat) + ',' + str(lon) if lat and lon else 'None'}{white}
""")

    Continue()
    Reset()

except Exception as e:
    Error(e)