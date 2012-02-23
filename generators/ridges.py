"""
Makes a mountain ridge line
"""
import pygame, time, pdb
from random import randrange

pygame.init()

window = pygame.display.set_mode((600, 600))
while 1:
    points = [(0, 300), (600, 300)]
    modrange = 100

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
        modrange *= 0.7
        modrange = int(modrange)
        time.sleep(0.1)
    #raw_input()
#pygame.image.save(window, raw_input("Filename? ") + ".png")
