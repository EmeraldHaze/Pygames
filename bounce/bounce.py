import pygame
from itertools import combinations as combo
from random import randint

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
blank.set_alpha(3)

screen = pygame.display.set_mode(size)

class Ball(pygame.sprite.Sprite):
    def __init__(self,  name, x = 300, y = 300, xspeed = 6, yspeed = 3):
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

    def collide(self, other):
        if self.rect.colliderect(other.rect):
            print "Bounce"
            if (self.rect.centerx - other.rect.centerx) > (self.rect.centery - other.rect.centery):
                #If the Ys are less diffrent than Xs,
                # he's on the same horizontal line
                #And Xspeeds get fliped
                self.speed[0] *= -1
                other.speed[0] *= -1
            else:
                self.speed[1] *= -1
                other.speed[1] *= -1

    def __str__(self):
        return "<" + self.name + ">"

ballpic = pygame.image.load("ball.png").convert_alpha()


balls = [Ball('ball1', 300, 200, 2, 7),
         Ball('ball2', 300, 300, 4, 7),
         Ball('ball3', 400, 300, 9, 7),
         Ball('ball4', 300, 400, 5, 9),]

screen.fill(white)

while 1:
    for ball in balls:
        ball.speed = [s * -1 for s in ball.speed]
        ball.move()
        ball.boarders()
        screen.blit(ballpic, ball.rect)

    for b1, b2 in combo(balls, 2):
        b1.collide(b2)

    for i in range(1):
        if rand.randint(0, accelChance) == 0:
            for ball in balls:
                ball.speed[i] *= accelRate

    screen.blit(blank, blank.get_rect())
    pygame.display.flip()
    c.tick(frameRate)
