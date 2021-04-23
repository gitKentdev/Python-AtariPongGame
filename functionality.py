import pygame, time, random

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 600

def player_move(key, player1, player2, state):
	if state:
		if key == pygame.K_w:
			player1.velocity = -5
		elif key == pygame.K_s:
			player1.velocity = 5

		if key == pygame.K_UP:
			player2.velocity = -5
		elif key == pygame.K_DOWN:
			player2.velocity = 5

	if not state:
		if key == pygame.K_w or key == pygame.K_s:
			player1.velocity = 0
		if key == pygame.K_UP or key == pygame.K_DOWN:
			player2.velocity = 0


def collision(ball, player1, player2):
	if ball.x - ball.radius - 10 <= player1.x + player1.width:
		# Collision with player 1 (LEFT ONE)
		if  ball.y - ball.radius >= player1.y - player1.height/2 and ball.y + ball.radius <= player1.y + player1.height:
			ball.velocity['x'] = random.random()* 3 + 2 

	if ball.x - 10 >= player2.x:
		# Collision with player 2 (RIGHT ONE
		if  ball.y + ball.radius >= player2.y - player2.height/2 and ball.y + ball.radius <= player2.y + player2.height:
			ball.velocity['x'] = -1* (random.random()* 3 + 2) 

def checkpoint(ball):
	if ball.x - ball.radius <= 0:
		ball.color = (random.randint(100, 200), 0, 170)
		ball.x = SCREEN_WIDTH/2
		ball.y = SCREEN_HEIGHT/2
		ball.velocity = {'x':3, 'y':-3}
		time.sleep(0.8)

	if ball.x - ball.radius >= SCREEN_WIDTH:
		ball.color = (0, random.randint(100, 200), 170)
		ball.x = SCREEN_WIDTH/2
		ball.y = SCREEN_HEIGHT/2
		ball.velocity = {'x':-3, 'y':-3}
		time.sleep(0.8)