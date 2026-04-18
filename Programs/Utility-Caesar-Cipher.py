# Copyright (c) 2025-2026 v4lkyr0 — Buildware-Tools
# See the file 'LICENSE' for copying permission.
# --------------------------------------------------------
# EN: Non-commercial use only. Do not sell, remove credits
#     or redistribute without prior written permission.
# FR: Usage non-commercial uniquement. Ne pas vendre, supprimer
#     les crédits ou redistribuer sans autorisation écrite.

from Plugins.Utils import *
from Plugins.Config import *

Title("Caesar Cipher")

Scroll(GradientBanner(utilities_banner))

try:
    Scroll(f"""
 {PREFIX}01{SUFFIX} Encrypt
 {PREFIX}02{SUFFIX} Decrypt
 {PREFIX}03{SUFFIX} Brute Force
""")
    choice = input(f"{INPUT} Choice {red}->{reset} ").strip().lstrip("0")

    text = input(f"{INPUT} Text {red}->{reset} ").strip()
    if not text:
        ErrorInput()

    def caesar_shift(text, shift):
        result = []
        for char in text:
            if char.isalpha():
                base = ord('A') if char.isupper() else ord('a')
                result.append(chr((ord(char) - base + shift) % 26 + base))
            else:
                result.append(char)
        return ''.join(result)

    if choice == "1":
        shift = input(f"{INPUT} Shift {red}->{reset} ").strip()
        shift = int(shift) if shift.isdigit() else 3
        encrypted = caesar_shift(text, shift)
        print(f"\n {SUCCESS} Encrypted:{red} {encrypted}", reset)

    elif choice == "2":
        shift = input(f"{INPUT} Shift {red}->{reset} ").strip()
        shift = int(shift) if shift.isdigit() else 3
        decrypted = caesar_shift(text, -shift)
        print(f"\n {SUCCESS} Decrypted:{red} {decrypted}", reset)

    elif choice == "3":
        output = f"\n {INFO} Brute Force Results:"
        for shift in range(1, 26):
            result = caesar_shift(text, -shift)
            output += f"\n {PREFIX}{shift:02d}{SUFFIX} {red}{result}{reset}"
        Scroll(output)

    else:
        ErrorChoice()

    print()
    Continue()
    Reset()

except Exception as e:
    Error(e)
