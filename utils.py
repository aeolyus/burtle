from constants import *
from interp import *

#Setup
init()
font.init()
screen = display.set_mode(SIZE)
opensans_font = font.Font(font.get_default_font(), 11)
messages = ["hello", "there"]
color = RED
pos = [0, 0]
USER_IN = ""

#Utility functions
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

