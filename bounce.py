import pygame, sys

pygame.init()

size = h, w = [600, 600]
speed = [5, 4]
fric = 0.9

white = 255, 255, 255

screen = pygame.display.set_mode(size)

c = pygame.time.Clock()

ball = pygame.image.load("ball.png").convert_alpha()
ballr = ball.get_rect()
print "running, rect:", ballr
screen.fill(white)
while 1:
    ballr = ballr.move(speed)
    if ballr.top < 0 or ballr.bottom > h:
        speed[1] *= -1
    if ballr.left < 0 or ballr.right > w:
        speed[0] *= -1
    #screen.fill(white)
    screen.blit(ball, ballr)
    pygame.display.flip()
    c.tick(70)
    #print "FPS:",c.get_fps()