## Imports
from constants import *
from pygame import *
from interp import *
from utils import *
import sys

## Setup
init()
font.init()
messages = ["hello","there"]
opensans_font = font.Font(font.get_default_font(), 11)
pos = [0, 0]
color = RED


def game_loop():
    k = 0
    last_key = ""
    while True:
        draw_output(screen, messages, opensans_font)
        for e in event.get():
            if e.type == QUIT:
                sys.exit()
        if k:
            pressed_keys = key.get_pressed()
            last_key = user_key_manager(pressed_keys, last_key)
        input_manager()
        display.flip()
        k += 1


game_loop()

