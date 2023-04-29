import pygame
from drawing import Draw
import time


def setup():
    global WIN, fill_color
    WIDTH = 800
    HEIGHT = 400
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))
    fill_color = (255, 255, 255)


circles = []
def main():
	setup()
	global circles, fill_color
	while 1:
		WIN.fill(fill_color)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.qiut()
				break

		mouse_pressed = pygame.mouse.get_pressed()
		if mouse_pressed[0]:
			drawing = True
			mouse_pos = pygame.mouse.get_pos()
			if drawing:
				draw = Draw(WIN, mouse_pos[0], mouse_pos[1], (0, 117, 255), 20)
				circles.append(draw)

		for circle in circles:
			circle.draw()

		keys = pygame.key.get_pressed()
		if keys[pygame.K_k]:
			pygame.image.save(WIN, 'track.png' )

		pygame.display.update()

