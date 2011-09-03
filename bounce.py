import pygame, sys
import random as rand

pygame.init()

size = h, w = [600, 600]
speed = [10, 10]
fric = 0.9

white = 255, 255, 255
frameRate = 70
accelChance = 50
accelRate = 1.05

blank = pygame.Surface(size)
blank.fill(white)
blank.set_alpha(64)

screen = pygame.display.set_mode(size)

c = pygame.time.Clock()

ball = pygame.image.load("ball.png").convert_alpha()
ballr = ball.get_rect()

screen.fill(white)

print "running, rect:", ballr

while 1:
    ballr = ballr.move(speed)
    if ballr.top < 0 or ballr.bottom > h:
        speed[1] *= -1
    if ballr.left < 0 or ballr.right > w:
        speed[0] *= -1

    screen.blit(blank, blank.get_rect())
    screen.blit(ball, ballr)
    pygame.display.flip()
    c.tick(frameRate)
    for x in speed:
        x *= fric
    for i in range(1):
        if rand.randint(0,accelChance) == 0:
            speed[i] *= accelRate
    #print "FPS:",c.get_fps()
