import sys, pygame
from random import choice

pygame.init()
size = (800, 800)
screen = pygame.display.set_mode(size)
done = False
colors = [(50,200,50), (255,0,0), (23,44,180)]
color = [255, 255, 255]

pos = [0, 0]
def move(dir, steps):
    while (steps > 0):
        pygame.draw.rect(screen, colors[steps%2], [pos[0]*30, pos[1]*30, 30, 30])
        if (dir == 'l' or dir == 'r'):
            pos[0] += -1 if dir == 'l' else 1
        if (dir == 'u' or dir == 'd'):
            pos[1] += -1 if dir == 'u' else 1
        print(pos) #debugging
        steps -= 1

drawn = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    if not drawn:
        move('r', 10)
        move('d', 10)
        drawn = True
    #for i in range(30):
    #    for j in range(30):
    #pygame.draw.rect(screen, choice(colors), [20*i, 20*j, 20*i+20, 20*j+20])
            #screen, color, lefttop,, bottomright
    pygame.display.flip()

