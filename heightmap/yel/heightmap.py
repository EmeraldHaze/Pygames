import pygame
from numpy import random, zeros

size = w, h = [100, 100]
grid = random.randint(256, size = (w, h))
newgrid = zeros((w, h), int)

print grid
print newgrid

def getat(x,y):
    n = 0
    if x >= 0 and x < w and y >= 0 and y < h:
        n = grid[x,y]
    return n

for i in range(input('Smooth how much? ')):
    for x in range(0, w):
        for y in range(0, h):
            newgrid[x,y] = (getat(x,y) + getat(x-1,y) + getat(x,y+1) + getat(x-1,y) + getat(x,y-1)) / 5
    grid = newgrid

colorgrid = zeros((w, h, 3), int)
for x in range(0,w):
    for y in range(0,h):
        colorgrid[x,y,1] = grid[x,y]

pygame.init()
image = pygame.surfarray.make_surface(colorgrid)
pygame.image.save(image, "image.png")
