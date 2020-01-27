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
		self.status = 0

	def draw(self):
		try:
			self.status = self.change_to
		except AttributeError:
			pass
		if self.status == 1: # only draw if white because screen is filled black
			pygame.draw.rect(win, (255, 255, 255), (self.x, self.y, box_size, box_size))

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

	if editor:
		win.fill((255, 255, 255))
		for a in range(grid_width):
			for b in range(grid_height):
				pygame.draw.rect(win, (0, 0, 0), (a * (box_size + margin) + margin, b * (box_size + margin) + margin, box_size, box_size))

	for x in grid:
		for y in x:
			y.draw()


	pygame.display.update()


grid = create_grid()

editor = True
run = True
while run:
	clock.tick(fps)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
		if pygame.mouse.get_pressed()[0]: # and editor:
			try:
				clicked_x = int(event.pos[0] / (margin + box_size))
				clicked_y = int(event.pos[1] / (margin + box_size))


				if grid[clicked_x][clicked_y].status == 0:
					grid[clicked_x][clicked_y].status = 1
				#else:
				"""
				grid[clicked_x - 1][clicked_y].status = 1
				grid[clicked_x + 1][clicked_y].status = 1
				grid[clicked_x][clicked_y - 1].status = 1
				grid[clicked_x][clicked_y + 1].status = 1
				"""

			except AttributeError:
				pass
			except IndexError:
				pass

	keys = pygame.key.get_pressed()

	if not(editor):
		if not(keys[pygame.K_SPACE]):
			run_all()
	else:
		if keys[pygame.K_RETURN]:
			editor = False

	redraw_window()

pygame.quit()
