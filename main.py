from pynput import keyboard
import subprocess



##################################################
#   hootkey
def on_activate_a():
    print('<ctrl>+<alt>+a pressed')

def on_activate_h():
    print('<ctrl>+<alt>+h pressed')

def on_activate_i():
    print('<ctrl>+<alt>+i pressed')

with keyboard.GlobalHotKeys({
        '<ctrl>+<alt>+h': on_activate_h,
        '<ctrl>+<alt>+i': on_activate_i,
        '<cmd>+a': on_activate_a,}) as h:
    h.join()
##################################################