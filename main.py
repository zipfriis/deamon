from pynput import keyboard
# the subprocess is uses to run system commands
import subprocess



##################################################
#   hootkey
def on_activate_1():
    pass

def on_activate_1():
    pass

def on_activate_1():
    pass

with keyboard.GlobalHotKeys({
        '<ctrl>+<alt>+h': on_activate_1,
        '<ctrl>+<alt>+i': on_activate_2,
        '<cmd>+a': on_activate_3,}) as h:
    h.join()
##################################################
