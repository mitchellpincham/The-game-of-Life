import pygame
import random
pygame.init()

file = open("settings.txt", "r")
file_lines = file.readlines()
for i in range(len(file_lines)):
	try:
		file_lines[i] = int("".join(file_lines[i][:-1]).lower())
	except:
		pass

grid_width = file_lines[1]
grid_height = file_lines[4]
box_size = file_lines[7]

margin = file_lines[10]
fps = file_lines[13]

screen_width = grid_width * (box_size + margin) + margin
screen_height = grid_height * (box_size + margin) + margin

win = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
pygame.display.set_caption("Game Of Life")

def find_neib(x, y):
	global grid
	count = 0

	for i in range(-1, 2):
		for j in range(-1, 2):
			col = (x + i + grid_width) % grid_width
			row = (y + j + grid_height) % grid_height
			count += grid[col][row].status

	return count - grid[x][y].status


class Box(object):
	def __init__(self, x, y, rel_x, rel_y):
		self.x = x
		self.y = y
		self.rel_x = rel_x
		self.rel_y = rel_y
		self.status = round(random.random())

	def draw(self):
		self.status = self.change_to
		if self.status == 1:
			pygame.draw.rect(win, (255, 255, 255), (self.x, self.y, box_size, box_size))
		else:
			pygame.draw.rect(win, (0, 0, 0), (self.x, self.y, box_size, box_size))

	def update(self):
		self.change_to = self.status
		self.neib_count =  find_neib(self.rel_x, self.rel_y)
		if self.neib_count < 2:
			self.change_to = 0
		elif self.neib_count > 3:
			self.change_to = 0
		elif self.neib_count == 3:
			self.change_to = 1


def create_grid():
	grid = []
	for i in range(grid_width):
		grid.append([])
		for j in range(grid_height):
			grid[i].append(Box(i * (box_size + margin) + margin, j * (box_size + margin) + margin, i, j))
	return grid


def run_all():
	global grid
	for x in grid:
		for y in x:
			y.update()


def redraw_window():
	win.fill((0, 0, 0))
	global grid

	for x in grid:
		for y in x:
			y.draw()


	pygame.display.update()


grid = create_grid()

run = True
while run:
	clock.tick(fps)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

	keys = pygame.key.get_pressed()
	if not(keys[pygame.K_SPACE]):
		run_all()

	redraw_window()

pygame.quit()
