import pygame

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 600

class Ball():
	def __init__(self, x, y, radius, color, velocity):
		self.x = x
		self.y = y
		self.radius = radius
		self.color = color
		self.velocity = velocity

	def draw(self, screen):
		pygame.draw.circle(screen, self.color, (self.x - self.radius, self.y - self.radius), self.radius)

	def update(self, screen):
		self.draw(screen)
		self.x += self.velocity['x']
		self.y += self.velocity['y']

		if self.y - self.radius - 10 <= 0 or self.y - self.radius + 10 >= SCREEN_HEIGHT:
			self.velocity['y'] *= -1