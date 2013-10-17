# Python code for Conway's game of life
import pygame, sys
from pygame.locals import*

pygame.init()

disp = pygame.display.set_mode((520, 400), 0, 32)
pygame.display.set_caption("Conways's Game of Life")
clock=pygame.time.Clock()


b = (0, 0, 0)
g = (192, 192, 192)
w = (255, 255, 255)

disp.fill(w)

pix = pygame.PixelArray(disp)

def cell(a,b):# 
        return pygame.Rect(a, b, 18, 18)

def check(e):# check the rgb value of a point
        p = e.centerx
        q = e.centery
        if pix[p, q] == disp.map_rgb(b):
		return  1
	if pix[p, q] == disp.map_rgb(w):
		return  2
def live(d):# draw rectangle with black colour
        return pygame.draw.rect(disp, b, d)

def dead(c):#draw rectangle with white colour
        return pygame.draw.rect(disp, w, c)


# checking all neighbours rgb value and no.of dead cell is append to lists
def neighbours(u, v):
	m = 0
	a = cell(u-20, v-20)
	if check(a) == 1:
		m = m+1	
	t = cell(u-20, v)
	if check(t) == 1:
		m = m+1
	c = cell(u-20, v+20)
	if check(c) == 1:
		m = m+1
	d = cell(u, v-20)
	if check(d) == 1:
		m = m+1
	f = cell(u, v+20)
	if check(f) == 1:
		m = m+1
	g = cell(u+20, v-20)
	if check(g) == 1:
		m = m+1 
	h = cell(u+20, v)
	if check(h) == 1:
		m = m+1
	i = cell(u+20, v+20)
	if check(i) == 1:
		m = m+1
	e = cell(u, v)

	if check(e) == 1: # if the reference cell is live then no.of dead cell is append to list l
		l.append(m)
		l1.append((u, v))# append the corresponding coordinates
	
	if check(e) == 2: # if the reference cell is dead then no.of dead cell is append to list l2
		l2.append(m)
		l3.append((u, v))# append the corresponding coordinates
		
def gamerule():
	for x in range(len(l)):
        	if l[x] < 2 or l[x] > 3:
                	y = l1[x]
                	s = cell(y[0], y[1])
                	dead(s)
        	if l[x] == 2 or l[x] == 3:
                	y = l1[x]
                	s = cell(y[0], y[1])
                	live(s)
	for z in range(len(l2)):
        	if l2[z] == 3:
                	y = l3[z]
                	s = cell(y[0], y[1])
                	live(s)
# example pattern
s1 = cell(100,160)
s2 = cell(120,160)
s3 = cell(140,180)
s4 = cell(160,200)
s5 = cell(160,220)
s6 = cell(160,240)
s7 = cell(140, 260)
s8 = cell(120,280)
s9 = cell(140,280)
live(s1)
live(s2)
live(s3)
live(s4)
live(s5)
live(s6)
live(s7)
live(s8)
live(s9)

while True:
	l = []
        l1 = []
        l2 = []
        l3 = []

	for p in range(500):
        	for q in range(380):
			if p % 20 == 0 and q % 20 == 0:
				neighbours(p, q)
	gamerule()

	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
	pygame.display.update()
	clock.tick(5)
