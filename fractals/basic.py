import pygame
size = [601, 601]
#X, Y
#Length, Hight

white = (0xFF, 0xFF, 0xFF)
red = (0xFF, 0, 0)
green = (0, 0xFF, 0)
blue = (0, 0, 0xFF)
black = (0, 0, 0)

dirs = [0, 2, 1, 3, 0]*2
colors = [green, blue, red, red, red]*2
repeat = 50

pygame.init()
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Drawer")

screen.fill(white)
pygame.display.flip()
    
sarr = pygame.surfarray.pixels3d(screen)

point = [size[0]/2,size[1]/2]

for i in range(repeat):
    print "repeat", i
    for j in range(len(dirs)):
        print "State", dirs[j]
        if dirs[j] == 0:
            point[0] += 1
        elif dirs[j] == 1:
            point[0] -= 1
        elif dirs[j] == 2:
            point[1] -= 1
        elif dirs[j] == 3:
            point[1] += 1
        sarr[point[0], point[1]] = colors[j]
        print 'color at point', point, 'set to', colors[j]
pygame.display.flip()


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
