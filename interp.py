from pygame import draw
import phase_main
import sys
import constants
import math

#Initalize
SQ_SIZE = constants.SQ_SIZE
NUM_SQ_WIDE = constants.NUM_SQ_WIDE
COLORS = constants.COLORS
pos = [0, 0]
color = COLORS["red"]

def execute_input(user_input, screen):
	tokens = user_input.split()
	command, arguments = tokens[0], tokens[1:]
	if command in ("exit", "quit"):
		quit()
	elif command in SHELL_CMDS:
		try:
			env = SHELL_CMDS.copy()
			env["screen"] = screen
			SHELL_CMDS[command](env, *arguments)
			return 0
		except Exception as ex:
			print(ex)
			return 1
	else:
		print("Invalid command: {} not found".format(command))
		return 1

def run(env, fname):
	phase_main.eval_program(phase_main.load("{}.phs".format(fname)), complement_env=env)

def circle(env, rad):
	rad = int(rad)
	for i in range(360):
		x = int(math.cos(i) * rad)
		y = int(math.sin(i) * rad)
		fill(env, color, (pos[0] + x, pos[1] + y))

def move(env, dir, steps):
	DIRS = {"u": (0, -1), "d": (0, 1), "l": (-1,0), "r": (1,0)}
	for i in range(int(steps)):
		fill(env, color, pos)
		dx, dy = DIRS[dir]
		pos[0] += dx
		pos[1] += dy

def jump(env, x, y):
	pos[0], pos[1] = int(x), int(y)

def chg_col(env, col):
	global color
	color = COLORS[col]

def fill(env, col, pos):
	draw.rect(env["screen"], col, [pos[0]*SQ_SIZE, pos[1]*SQ_SIZE, SQ_SIZE, SQ_SIZE])

def clear(env):
	draw.rect(env["screen"], COLORS["white"], [0, 0, constants.HEIGHT, constants.WIDTH])
	jump(env, 1, 1)

def bomb(env, n):
	n = int(n)
	for i in range(-n, n+1):
		for j in range(-n, n+1):
			fill(env, color, (pos[0] + i, pos[1] + j))

def hline(env):
	for i in range(NUM_SQ_WIDE):
		fill(env, color, (i, pos[1]))

def vline(env):
	for i in range(NUM_SQ_WIDE):
		fill(env, color, (pos[0], i))

def rightln(env):
	for i in range(pos[0], NUM_SQ_WIDE):
		fill(env, color, (i, pos[1]))

def leftln(env):
	for i in range(0, pos[0]):
		fill(env, color, (i, pos[1]))

def upln(env):
	for i in range(0, pos[0]):
		fill(env, color, (pos[1], i))

def downln(env):
	for i in range(pos[0], NUM_SQ_WIDE):
		fill(env, color, (pos[1], i))

def quit():
	sys.exit()

#rainbow lines & circles 

SHELL_CMDS = {"mv": move, "jump": jump, "col": chg_col, "bomb": bomb, "run": run, 
			  "clr": clear, "hline": hline, "vline": vline, "leftln": leftln, 
			  "rightln": rightln, "upln":upln, "downln": downln, "circ": circle}
