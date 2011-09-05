import pygame
import numpy as N
import pygame.surfarray as surfarray
from math import sqrt

precis = 100
black = N.array([  0,   0,   0])
white = N.array([255, 255, 255])
size = [601, 601]
#X, Y
#Length, Hight



bb = 50
bw = 50
lbb = precis/100.0*bb
lbw = precis/100.0*bw

bbspace = N.linspace(0, 255, lbb)
bbcolor = N.zeros(lbw)
bbcolor[:] = (
bwspace = N.linspace(0, 255, lbw)




def check_mad(c, precis):
    count = 0
    color = black
    Z = [complex(0)]
    for i in range(precis):
        old = Z[-1]
        new = (old**2)+c
        if (new.imag**2 + new.real**2) >= 4:
            color = white
            count = 0
            break
        Z.append(new)
        count+=1
    if not count:
        color[2] = space[count]
    return color
        
pygame.init()
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Fractals")

screen.fill(white)
pygame.display.flip()
    
sarr = surfarray.pixels3d(screen)

Yc = 0
Xc = 0
space = N.linspace(-2, 2, size[0]-1)
for Y in space:
    Yc+=1
    for X in space:
        C = complex(X, Y)
        print Yc, ",",Xc, ":  ",C
        color = check_mad(C, precis)
        print "Color: ",color
        sarr[Yc,Xc] = color
        #The surface array is odd. sarr[0] is the first coulum.
        Xc+=1
    Xc = 0
    
pygame.display.flip()


# -------- Wait loop-----------
print "Running"
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print "Quit."
            pygame.quit ()
            break
            
#600 coulums, 600 items each.

exit()
