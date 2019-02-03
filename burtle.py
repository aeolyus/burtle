## Imports
from constants import *
from pygame import *
from interp import *
from utils import *
import sys

def game_loop():
    k = 0
    last_key = ""
    while True:
        for e in event.get():
            if e.type == QUIT:
                sys.exit()
        if k:
            pressed_keys = key.get_pressed()
            last_key = user_key_manager(pressed_keys, last_key)
        draw_output(screen, messages, opensans_font)
        input_manager()
        display.flip()
        k += 1

game_loop()

"""
Ideas:
- add support for floats
- run interactively
- do:, hline, vline, 
- sprite on pointer square
"""







