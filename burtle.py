## Imports
from constants import *
from pygame import *
from interp import *
import sys

## Constants
WIDTH, HEIGHT = 480, 630
SIZE = (WIDTH, HEIGHT)
USER_IN = ""
EXEC_CLEAR = False
ALPHA_NUM_CHARS = "abcdefghijklmnopqrstuvwxyz0123456789B! "
ALPHA_NUM_KEYS =    [K_a, K_b, K_c, K_d, K_e, K_f, K_g, K_h, K_i, K_j, 
                    K_k, K_l, K_m, K_n, K_o,K_p, K_q, K_r, K_s, K_t, 
                    K_u, K_v, K_w, K_x, K_y, K_z, K_0, K_1, K_2, K_3,
                    K_4, K_5, K_6, K_7, K_8, K_9, 
                    K_BACKSPACE, K_RETURN,K_SPACE]
## Setup
init()
font.init()
screen = display.set_mode(SIZE)
messages = ["hello","there"]
opensans_font = font.Font(font.get_default_font(), 11)
pos = [0, 0]
color = RED

def user_key_manager(keys, last_key):
    global USER_IN
    global EXEC_CLEAR
    untouched = True
    #User Input
    index = [i for i, key in enumerate(ALPHA_NUM_KEYS) if keys[key]]
    if index:
        index = index[0]
        untouched = False
        char_key = ALPHA_NUM_CHARS[index]
        if char_key != last_key:
            last_key = char_key
            if char_key == "!":
                EXEC_CLEAR = True
            elif char_key == "B":
                USER_IN = USER_IN[:len(USER_IN) - 1]
            else:
                USER_IN += char_key
    if untouched:
        last_key = ""
    return last_key

def input_manager():
    global EXEC_CLEAR
    global USER_IN
    draw_input(screen, USER_IN, EXEC_CLEAR, opensans_font)
    if EXEC_CLEAR:
        messages.append(USER_IN)
        execute_input(USER_IN, screen)
        USER_IN = ""
        EXEC_CLEAR = False

def draw_output(screen, messages, font_obj):
    #White Background
    source = transform.scale(image.load("white.png"), (WIDTH, 120))
    screen.blit(source, source.get_rect().move(0, WIDTH))
    #Text rendering
    for i in range(min(5, len(messages))):
        message = str(messages[::-1][i])
        col = (140, 140, 140) if i else (0, 0, 0)
        textsurface = font_obj.render(message, True, col)
        screen.blit(textsurface,(10, WIDTH + 10 + i * 17))

def draw_input(screen, text, clear, font_obj):
    source = transform.scale(image.load("offwhite.png"), (480, 30))
    screen.blit(source, source.get_rect().move(0, 600))
    text = "" if clear else text
    #Text rendering
    textsurface = font_obj.render(str(text), True, (20, 20, 20))
    screen.blit(textsurface,(10, 605))

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

