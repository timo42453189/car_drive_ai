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