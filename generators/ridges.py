modrange = 200
modfactor = 0.6
pause = 0.01
save = True
width = 600

"""
Makes a mountain ridge line
"""
import pygame, time, pdb, math, random
from random import randrange

pygame.init()
#415
window = pygame.display.set_mode((600, width))

avrg = lambda *a: sum(a) / len(a)

points = [[0, 300], [600, 300]]
newpoints = list(points)

def draw():
    window.fill(0)
    pygame.draw.lines(window, 0xFFFFFF, False, points)
    pygame.display.flip()

for i in range(int(math.log(width, 2)) + 1 ):
    #This should make the closest thing to one point for pixel
    draw()
    offset = 0
    for n, point in enumerate(points):
        try:
            point2 = points[n + 1]
            mid = [
                avrg(point[0], point2[0]),
                avrg(point[1], point2[1]) + randrange(-modrange, modrange)
            ]
            newpoints.insert(n + offset + 1, mid)
            offset += 1
        except IndexError:
            pass
            #This happens at the last item
    points = list(newpoints)
    modrange = int(modrange * modfactor)
    time.sleep(pause)

i = 0
while 1:
    i += 1
    time.sleep(pause)
    for i, point in enumerate(points):
        if i == 0:
            points = []
        else:
            point[0] -= 1
            points.append(point)
    points.append(
        [width, points[-1][1] + random.triangular(-10, 10, math.sin(i))]
    )
    draw()


