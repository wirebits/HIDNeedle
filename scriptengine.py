# Script Engine File for HIDNeedle
# Author - WireBits

import time
from keys import hidKeys
from adafruit_hid.keycode import Keycode

def to_keycode(code):
    if isinstance(code, int):
        return code
    else:
        None

def press_keys(kbd, pressCodes):
    for codes in pressCodes:
        kbd.press(codes)
    kbd.release_all()

def convert_hid_line(line):
    keycodes = []
    for key in line.split():
        key = key.upper()
        if key in hidKeys:
            keycodes.append(hidKeys[key])
        elif hasattr(Keycode, key):
            keycodes.append(getattr(Keycode, key))
    return keycodes

def run_payload(lines, keyboard, layout):
    i = 0
    length = len(lines)
    while i < length:
        line = lines[i].strip()
        if not line or line.startswith("CMT"):
            i += 1
            continue
        if line.startswith("WAIT"):
            time.sleep(int(line.split()[1]) / 1000)
        elif line.startswith("TYPE"):
            layout.write(line.split(" ", 1)[1])
        elif line.startswith("TYNL"):
            layout.write(line.split(" ", 1)[1])
            press_keys(keyboard, [Keycode.ENTER])
        elif line.startswith("LOOP"):
            count = int(line.split()[1])
            block = []
            i += 1
            while i < length and lines[i].strip() != "EXIT":
                block.append(lines[i])
                i += 1
            for _ in range(count):
                run_payload(block, keyboard, layout)
        elif line == "INF":
            block = []
            i += 1
            while i < length and lines[i].strip() != "EXIT":
                block.append(lines[i])
                i += 1
            while True:
                run_payload(block, keyboard, layout)
        elif line == "EXIT":
            return
        else:
            keys = convert_hid_line(line)
            if keys:
                press_keys(keyboard, keys)
        i += 1