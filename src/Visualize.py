import pygame as pg
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

file = open('log1.txt', 'r')
lines = []

for line in file:
	lines.append([])
	for l in line:
		v = 0
		if l =='+': 
			v = 1

		lines[len(lines)-1].append(v)

file.close()

pg.init()
screen = pg.display.set_mode((1200, 600))

objects = []

for i in range(len(lines[0])):
	objects.append([i*22, 300, 20, 20])

done = False
clock = pg.time.Clock()

i = 0
while not done:
	for event in pg.event.get():
		if event.type == pg.QUIT:
			done = True

	screen.fill(BLACK)
	
	for o in range(len(objects)):
		color = (25, 25, 25)

		if lines[i][o] == 1: 
			color = RED

		pg.draw.rect(screen, color, objects[o])

	i += 1
	if i >= len(lines): done = True
	pg.display.flip()
	clock.tick(60)

pg.quit()