# boot.py file for HIDNeedle
# Author - WireBits

from usb_hid import Device
import board, digitalio, storage, usb_cdc, usb_hid

mode_pin = digitalio.DigitalInOut(board.GPX)
mode_pin.direction = digitalio.Direction.INPUT
mode_pin.pull = digitalio.Pull.UP

if not mode_pin.value:
    # Show CIRCUITPY drive, no keyboard
    usb_cdc.enable()
    usb_hid.disable()
    storage.enable_usb_drive()
else:
    usb_cdc.disable()
    storage.disable_usb_drive()
    usb_hid.enable((Device.KEYBOARD),boot_device=1)