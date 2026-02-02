# ⌨️HIDNeedle

# ℹ️About
A lightweight keystroke injection framework for CircuitPython-supported devices.

# ⏳Working
It basically add the mnemonics in .txt file and its converts the mnemonics with values with script engine so that it perform keystroke injection.

# ✨Features
- Easy to setup.
- Ultimate stealth mode for execute payload.
- Easy to edit payload.

# ✅Supported Boards
- Those boards which support `CircuitPython` and it supports `usb_hid` module.

>[!TIP]
> Use those boards which have atleast `2MB` flash memory.

>[!CAUTION]
> - Some boards does not have built-in UF2 bootloader.  
> - It need to flash UF2 bootloader to allows you to flash your firmware by just dragging and dropping `.uf2` file onto the flash drive without using an external programmer.  
> - Check CircuitPython page of that board.  
> - At the end of the page, if it contain link for bootloader `.bin` file, that means it does not have built-in UF2 bootloader.

# 📦Requirements
- `1` Your Board
- `1` Micro-B USB / Type-C USB Cable with data transfer support
