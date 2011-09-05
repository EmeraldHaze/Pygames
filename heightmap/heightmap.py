import pygame
from numpy import random, zeros

size = w, h = [300, 300]
grid = random.randint(256, size = (w, h, 3))
newgrid = zeros((w, h, 3), int)

for y in range(10, w-9):
    for x in range(10, h-9):
        colors = []
        for row in grid[y-10:y+11, x-10:x+11]: colors.extend(row)
        for i in range(len(colors)): colors[i] = list(colors[i])
        newcolor = [sum(color)/len(color) for color in zip(*colors)]
        for c in range(len(newgrid[y, x])):
            newgrid[y, x, c] = newcolor[c]


pygame.init()

image = pygame.surfarray.make_surface(newgrid)
pygame.image.save(image, "image2.png")
