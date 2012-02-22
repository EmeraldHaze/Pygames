import pygame
size = [601, 601]
#X, Y
#Length, Hight

white = (0xFF, 0xFF, 0xFF)
red = (0xFF, 0, 0)
green = (0, 0xFF, 0)
blue = (0, 0, 0xFF)
black = (0, 0, 0)

pygame.init()
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Colors")

screen.fill(white)
pygame.display.flip()

sarr = pygame.surfarray.pixels3d(screen)


# -------- Wait loop-----------
print "Running"
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.flip()
            print "Quit."
            pygame.quit ()
            break

exit()
