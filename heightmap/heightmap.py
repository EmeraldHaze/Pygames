import pygame
from numpy import random, zeros

size = w, h = [600, 600]
grid = random.randint(256, (w, h, 3))
newgrid = numpy.zeros((w, h, 3), int)

#pygame.init()
#screen = pygame.display.set_mode(size)
#pygame.display.set_caption("heightmap")
#screen.fill()
    
sarr = pygame.surfarray.pixels2d(screen)

for i in range(1, w):
    for h in range(1, h):
        print sarr[w,h]
