from random import randint

import threading

from pynput.keyboard import Listener

from PIL import Image

from pystray import Icon as icon, Menu as menu, MenuItem as item

import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
from pygame import mixer

mixer.init()

sound1 = mixer.Sound("click4_1.wav")
sound2 = mixer.Sound("click4_2.wav")
sound3 = mixer.Sound("click4_3.wav")
sound4 = mixer.Sound("click4_4.wav")
sound5 = mixer.Sound("click4_5.wav")
sound6 = mixer.Sound("click4_6.wav")

state = True
    
def tray():
    global state

    def on_clicked(icon, item):
        global state
        if state == True:
                icon.icon = Image.open('icon_off.ico')
                icon._update_icon()
        else:
            icon.icon = Image.open('icon.ico')
            icon._update_icon()
        state = not item.checked

    icon('Keyboard Sound', Image.open('icon.ico'), menu=menu(
            item(
                'Active', on_clicked, default=True, visible=True, checked=lambda item: state))).run()

def main():

    global state
    global sound1, sound2, sound3, sound4, sound5, sound6

    def on_press(key):
        if state == True:
            mixer.Sound.play(globals()[f'sound{randint(1,6)}'])
    def on_release(key): pass

    with Listener(
        on_press=on_press, on_release=on_release
        ) as listener: listener.join()

if __name__ == '__main__':
    t1 = threading.Thread(target=tray)
    t2 = threading.Thread(target=main) 
    print('i')
    t1.start()
    t2.start()