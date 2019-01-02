## Imports
from random import choice
from pygame import *
import sys
import pygame.transform as pytr
import pygame.image as pyim
import pygame.font as pyfont

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
pyfont.init()
screen = display.set_mode(SIZE)
messages = ["hello","there"]
opensans_font = pyfont.Font(pyfont.get_default_font(), 11)

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
        execute_input(USER_IN)
        USER_IN = ""
        EXEC_CLEAR = False

def draw_output(screen, messages, font_obj):
    #White Background
    source = pytr.scale(pyim.load("white.png"), (480, 120))
    screen.blit(source, source.get_rect().move(0, 480))
    #Text rendering
    for i in range(min(5, len(messages))):
        message = str(messages[::-1][i])
        if i == 0:
            col = (0,0,0)
        else:
            col = (140, 140, 140)
        textsurface = font_obj.render(message, True, col)
        screen.blit(textsurface,(10, 490 + i * 17))

def draw_input(screen, text, clear, font_obj):
    source = pytr.scale(pyim.load("offwhite.png"), (480, 30))
    screen.blit(source, source.get_rect().move(0, 600))
    if clear:
        text = ""
    #Text rendering
    textsurface = font_obj.render(str(text), True, (20, 20, 20))
    screen.blit(textsurface,(10, 605))

### Move to another file!
def execute_input(USER_IN):
    messages.append(USER_IN)
    tokens = USER_IN.split()
    #move(1, 2)
    funcs = {"move":move}
    funcs[tokens[0]](*tokens[1:])

colors = [(50,200,50), (255,0,0), (23,44,180)]
color = [255, 255, 255]
pos = [0, 0]

# Commands
def move(dir, steps):
    for i in range(int(steps)):
        draw.rect(screen, colors[int(steps)%2], [pos[0]*30, pos[1]*30, 30, 30])
        if (dir == 'l' or dir == 'r'):
            pos[0] += -1 if dir == 'l' else 1
        if (dir == 'u' or dir == 'd'):
            pos[1] += -1 if dir == 'u' else 1
        print(pos) #debugging
### Moved!

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

