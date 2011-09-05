import pygame
from numpy import random, zeros

size = w, h = [600, 600]
grid = random.randint(256, size = (w, h, 3))
newgrid = zeros((w, h, 3), int)

for y in range(1, w):
    for x in range(1, h):
        colors = []
        for row in grid[y-1:y+2, x-1:x+2]: colors.extend(row)
        for i in range(len(colors)): colors[i] = list(colors[i])
        newcolor = [sum(color)/len(color) for color in zip(*colors)]
        for c in range(len(newgrid[y, x])):
            newgrid[y, x, c] = newcolor[c]


pygame.init()

image = pygame.surfarray.make_surface(newgrid)
pygame.image.save(image, "image.png")
