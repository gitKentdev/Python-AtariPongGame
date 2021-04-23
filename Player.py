import pygame

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 600

class Player():
	def __init__(self, x, y, width, height, color, velocity):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.color = color
		self.velocity = velocity

	def draw(self, screen):
		pygame.draw.rect(screen, self.color, pygame.Rect(self.x, self.y - self.height/2, self.width, self.height))

	def update(self, screen):
		self.draw(screen)
		if self.y - self.height/2<= 0:
			self.y = self.height/2
		elif self.y + self.height / 2 >= SCREEN_HEIGHT:
			self.y = SCREEN_HEIGHT - self.height/2
		self.y += self.velocity
