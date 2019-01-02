from pygame import *

WHITE = (255, 255, 255)
RED = (255, 71, 26)
ORANGE = (255, 173, 51)
YELLOW = (255, 255, 51)
GREEN = (51, 255, 51)
BLUE = (0, 85, 255)
PURPLE = (153, 0, 153)
BLACK = (0, 0, 0)
BROWN = (128, 64, 0)
GREY = (100, 100, 100)
AQUA = (0, 255, 153)
PINK = (255, 128, 255)
MAROON = (128,0,0)
COLORS = {"white": WHITE, "red": RED, "orange": ORANGE, "yellow": YELLOW, "green": GREEN, 
		  "blue": BLUE, "purple": PURPLE, "black": BLACK, "brown": BROWN, "grey": GREY, 
		  "aqua": AQUA, "pink": PINK, "maroon": MAROON}

DIRS = {"u": (0, -1), "d": (0, 1), "l": (-1,0), "r": (1,0)}

WIDTH, HEIGHT = 480, 630
SIZE = (WIDTH, HEIGHT)
EXEC_CLEAR = False
ALPHA_NUM_CHARS = "abcdefghijklmnopqrstuvwxyz0123456789B! "
ALPHA_NUM_KEYS =    [K_a, K_b, K_c, K_d, K_e, K_f, K_g, K_h, K_i, K_j, 
                    K_k, K_l, K_m, K_n, K_o,K_p, K_q, K_r, K_s, K_t, 
                    K_u, K_v, K_w, K_x, K_y, K_z, K_0, K_1, K_2, K_3,
                    K_4, K_5, K_6, K_7, K_8, K_9, 
                    K_BACKSPACE, K_RETURN,K_SPACE]
