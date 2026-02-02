# HIDNeedle
# A lightweight keystroke injection framework for CircuitPython-supported devices.
# Author - WireBits

import time
import usb_hid
from scriptengine import run_payload
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS

payloadFile = "payload.txt"

keyboard = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(keyboard)

def load_payload(filename):
    try:
        with open(filename, "r") as f:
            return f.readlines()
    except OSError:
        print("[!] payload.txt not found")
        return None

print("[*] Loading payload...")
payload = load_payload(payloadFile)

if payload:
    time.sleep(2)
    run_payload(payload, keyboard, layout)
    print("[*] Payload executed!")

while True:
    pass