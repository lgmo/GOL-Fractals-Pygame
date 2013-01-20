import pygame, sys
from pygame.locals import*
from math import sqrt

pygame.init()
clock=pygame.time.Clock()

disp = pygame.display.set_mode((500, 400), 0, 32)
pygame.display.set_caption('Sierpinski triangle')

b = (0, 0, 0)
w = (255, 255, 255)

disp.fill(w)

r = pygame.Rect(50, 100, 200, 150*sqrt(3))
# three coordinates of first triangle
l = [(r[0], r[1]), (r[0]+2*r[2], r[1]),(r[0]+r[2], r[1]+r[3])]

def midpoint(p1, p2):
    return ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)

def iteration(level, p1, p2, p3):
	if level == 1:
		pygame.draw.polygon(disp, b, (p1,p2,p3),1)
	else:
		p4 = midpoint(p1, p2)
            	p5 = midpoint(p2, p3)
            	p6 = midpoint(p1, p3)
	
         	iteration(level - 1, p1,p4,p6)
		iteration(level - 1, p4,p2,p5)
		iteration(level - 1, p6,p5,p3)

iteration(7, l[0], l[1], l[2])
while True:
        for event in pygame.event.get():
                if event.type == QUIT:
                        pygame.quit()
                        sys.exit()
        pygame.display.update()
