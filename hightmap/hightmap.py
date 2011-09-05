import pygame
from numpy import random, zeros

size = w, h = [600, 600]
grid = random.randint(256, (w, h, 3))
newgrid = numpy.zeros((w, h, 3), int)

for i in range(1, w):
    for h in range(1, h):
