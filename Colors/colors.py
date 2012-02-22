import pygame, math
size = X, Y = [200, 200]
#X, Y
#Length, Hight

pygame.init()
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Colors")

screen.fill(0xFFFFFF)
pygame.display.flip()

c = pygame.time.Clock()
sarr = pygame.surfarray.pixels2d(screen)


# -------- Wait loop-----------
print "Running"
i = 1
j = 1
while 1:
    for x in range(X):
        for y in range(Y):
            old = sarr[x, y]
            new = int(x**(y/(1 + j%100)) * j) % 0xFFFFFF
            sarr[x, y] = new
    pygame.display.flip()
    c.tick(20)
    j += 1

    print i,j
exit()