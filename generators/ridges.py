MODRANGE = 200
MODFACTOR = 0.6
PAUSE = 0.1
SAVE = True

"""
Makes a mountain ridge line
"""
import pygame, time, pdb
from random import randrange

pygame.init()

window = pygame.display.set_mode((600, 600))
I = -1
while 1:
    I += 1
    points = [(0, 300), (600, 300)]
    modrange = MODRANGE

    avrg = lambda *a: sum(a) / len(a)
    newpoints = list(points)


    while modrange > 1:
        print(modrange)
        window.fill(0)
        pygame.draw.lines(window, 0xFFFFFF, False, points)
        pygame.display.flip()
        offset = 0
        for n, point in enumerate(points):
            try:
                point2 = points[n + 1]
                mid = (
                    avrg(point[0], point2[0]),
                    avrg(point[1], point2[1]) + randrange(-modrange, modrange)
                )
                print(point, point2, mid)
                newpoints.insert(n + offset + 1, mid)
                offset += 1
            except IndexError:
                pass
                #This happens at the last item
        points = list(newpoints)
        modrange *= MODFACTOR
        modrange = int(modrange)
        time.sleep(PAUSE)
        if SAVE:
            pygame.image.save(window, "mountains%s.png" % I)
    #raw_input()
