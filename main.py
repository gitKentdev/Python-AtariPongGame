import pygame, sys, random
from Player import *
from Ball import *
from functionality import *

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 600

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('PONG_GAME')


ball = Ball(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, 20, (255, 0, 0), {'x':random.choice([-3, 3]), 'y':-3})
player1 = Player(25, SCREEN_HEIGHT/2, 25, 150, (255, 255, 255), 0)
player2 = Player(SCREEN_WIDTH - 50, SCREEN_HEIGHT/2, 25, 150, (255, 255, 255), 0)

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

		for key in [pygame.K_w, pygame.K_s, pygame.K_UP, pygame.K_DOWN]:
			if event.type == pygame.KEYDOWN:
				if event.key == key:
					player_move(key, player1, player2, True)

			if event.type == pygame.KEYUP:
				if event.key == key:
					player_move(key, player1, player2, False)

	screen.fill((25, 25, 25))
	ball.update(screen)
	player1.update(screen)
	player2.update(screen)

	collision(ball, player1, player2)
	checkpoint(ball)

	pygame.display.update()
	clock.tick(120)

