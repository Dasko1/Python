#message_box.py: simple message box using Python!

import ctypes  # An included library with Python install.
ctypes.windll.user32.MessageBoxA(0, "This is a message box in Python!", "Your title", 0)
