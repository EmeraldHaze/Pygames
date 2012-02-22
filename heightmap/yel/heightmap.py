import pygame
from numpy import random, zeros
from random import randint

size = w, h = [300, 300]
grid = zeros((w, h), int)
newgrid = zeros((w, h), int)

def getat(x,y):
    n = 0
    if x >= 0 and x < w and y >= 0 and y < h:
        n = grid[x,y]
    return n

for x in range(0, w):
    for y in range(0, h):
        grid[x,y] = (x ** 1) * 5 + (y ** 2) * 5

for i in range(0):
    for x in range(0, w):
        for y in range(0, h):
            newgrid[x,y] = (getat(x,y) + getat(x-1,y) + getat(x,y+1) + getat(x-1,y) + getat(x,y-1)) / 5
    grid = newgrid
    print i+1

colorgrid = zeros((w, h, 3), int)
for x in range(0,w):
    for y in range(0,h):
        for i in range(1):
            colorgrid[x,y,1] = grid[x,y]

pygame.init()
image = pygame.surfarray.make_surface(colorgrid)

screen = pygame.display.set_mode(size)
screen.blit(image, image.get_rect())
pygame.display.flip()

#pygame.image.save(image, "oimage.png")

print 'Done'

#1, x * y
#2, (x * 3) * (y * 3)
#3, (x ** 2) + (y ** 2)
#4, (x ** 2) * 5 + (y ** 2) * 5
#5, (x ** 2) * (y ** 2)
#6, (x ** 2) * 5 * (y ** 2) * 5
#7, x - y
#8, y - x
#9, x - y * y - x
#10, (x - y) - (y - x)
