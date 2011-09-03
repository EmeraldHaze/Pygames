import pygame, sys
import random as rand

pygame.init()
c = pygame.time.Clock()

white = 255, 255, 255
size = h, w = [600, 600]

speed = [5, 7]
fric = 0.9
frameRate = 90
accelChance = 50
accelRate = 1.05

blank = pygame.Surface(size)
blank.fill(white)
blank.set_alpha(32)

screen = pygame.display.set_mode(size)

class Ball(pygame.sprite.Sprite):
    def __init__(self,  name, x = 300, y = 300, xspeed = 5, yspeed = 6):
        self.rect = ballpic.get_rect()
        self.rect.move_ip((x, y))
        self.speed =[xspeed, yspeed]
        self.name = name

    def boarders(self):
        if self.rect.top < 0 or self.rect.bottom > h:
            self.speed[1] *= -1
        if self.rect.left < 0 or self.rect.right > w:
            self.speed[0] *= -1

    def move(self):
        self.rect.move_ip(self.speed)

    def __str__(self):
        return "<" + self.name + ">"

ballpic = pygame.image.load("ball.png").convert_alpha()

balls = [Ball('ball1'), Ball("ball2")]

screen.fill(white)

while 1:
    for ball in balls:
        ball.move()
        ball.boarders()
        screen.blit(ballpic, ball.rect)

    screen.blit(blank, blank.get_rect())
    pygame.display.flip()
    c.tick(frameRate)
    for b in balls:
        for s in b.speed:
            s *= fric
    for i in range(1):
        if rand.randint(0,accelChance) == 0:
            for b in balls:
                b.speed[i] *= accelRate
    #print "FPS:",c.get_fps()
