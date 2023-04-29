import os
import pygame

class Draw:
	def __init__(self, WIN, x, y, color, size):
		self.WIN = WIN
		self.x = x
		self.y = y
		self.COLOR = color
		self.PEN_SIZE = size

	def draw(self):
		pygame.draw.circle(self.WIN, self.COLOR, (self.x, self.y), self.PEN_SIZE)

	def get_pos(self):
		return (self.x, self.y)


class Button():
	def __init__(self, WIN, IMG, name, x, y):
		self.IMG = IMG
		self.WIN = WIN
		self.NAME = name
		self.x = x
		self.y = y
		self.width = self.IMG.get_width()
		self.height = self.IMG.get_height()

	def show(self):
		# show img
		self.WIN.blit(self.IMG, (self.x, self.y))

	def get_name(self):
		return self.NAME

	def hit_mouse(self):
		# calculate if you press on the img
		mouse_pressed = pygame.mouse.get_pressed()
		mouse_pos = pygame.mouse.get_pos()
		if mouse_pressed[0]:
			if self.x <= mouse_pos[0] <= self.x + self.width and self.y <= mouse_pos[1] <= self.y + self.height:
				return True
			else:
				return False