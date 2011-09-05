import pygame, sys

size = h, w = [600, 600]
tpf = 10

white = (255,255,255)

pygame.init()
pygame.display.set_caption('Grid')
screen = pygame.display.set_mode(size)
background = pygame.Surface(size)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print 'Closing'
            sys.exit()

    for i in range(tpf):
        background.fill(white)

    pygame.display.flip()
