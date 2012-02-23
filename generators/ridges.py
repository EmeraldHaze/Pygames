"""
Makes a mountain ridge line
"""
import pygame, time, pdb
from random import randrange

pygame.init()

window = pygame.display.set_mode((600, 600))

points = [(0, 300), (600, 300)]
modrange = 200

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
    modrange /= 1.5
    modrange = int(modrange)
    time.sleep(1)

pygame.image.save(window, raw_input("Filename? ") + ".png")
