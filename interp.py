from pygame import draw

def execute_input(user_input, screen):
    tokens = user_input.split()
    command, arguments = tokens[0], tokens[1:]
    CMDS[command](screen, *arguments)

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

pos = [0, 0]
color = RED

def do_for(scree, *args):
	num = int(args[0][:-1])
	for i in range(int(num)):
		execute_input(*args[1:], screen)

def move(screen, dir, steps):
    for i in range(int(steps)):
        fill(screen, color, pos)
        dx, dy = DIRS[dir]
        pos[0] += dx
        pos[1] += dy

def jump(screen, x, y):
	pos[0], pos[1] = int(x), int(y)

def chg_col(screen, col):
	global color
	color = COLORS[col]

def fill(screen, col, pos):
	draw.rect(screen, col, [pos[0]*30, pos[1]*30, 30, 30])

def bomb(screen, n):
	n = int(n)
	for i in range(-n, n+1):
		for j in range(-n, n+1):
			fill(screen, color, (pos[0] + i, pos[1] + j))
CMDS = {"mv": move, "jump": jump, "col": chg_col, "do": do_for, "bomb": bomb}
