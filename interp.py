def execute_input(user_input):
    messages.append(user_input)
    tokens = user_input.split()
    command, arguments = token[0], tokens[1:]
    CMDS[command](*arguments)

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
CMDS = {"mv": move, "jump": jump, "chg_col": chg_col, "do": do_for, "bomb": bomb}

pos = [0, 0]
color = RED

def do_for(*args):
	num = int(args[0][:-1])
	for i in range(int(num)):
		execute_input(*args[1:])

def move(dir, steps):
    for i in range(int(steps)):
        fill(color, pos)
        dx, dy = DIRS[dir]
        pos[0] += dx
        pos[1] += dy

def jump(x, y):
	pos[0], pos[1] = x, y

def chg_col(col):
	global color
	color = col

def fill(col, pos):
	draw.rect(screen, col, [pos[0]*30, pos[1]*30, 30, 30])

def bomb(n):
	for i in range(-n, n+1):
		for j in range(-n, n+1):
			fill(color, (i,j))
