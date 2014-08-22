import pygame

def menu(screen, resolution, ground, background, bird):
	background.draw(screen, 0)
	ground.draw(screen, resolution[1])
	bird.draw(screen)
	font = pygame.font.Font("font/font.ttf", 60)
	screen.blit (font.render ("E - easy ", True, (0, 255, 0)), (200, 100))
	screen.blit (font.render ("M - medium", True, (0, 255, 0)), (200, 200))
	screen.blit (font.render ("H - hard", True, (0, 255, 0)), (200, 300))
	pygame.display.flip()
	
	amount = 0
	middle = 0
	space = 0	
	exit = False
	while not exit:
		for event in pygame.event.get():
				if event.type == pygame.QUIT:
					exit = True

				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_e:
						amount = 3
						middle = 200
						space = 5
						start = False
						exit = True

					if event.key == pygame.K_m:
						amount = 4
						middle = 150
						space = 4
						start = False
						exit = True
					
					if event.key == pygame.K_h:
						amount = 5
						middle = 130
						space = 5
						start = False
						exit = True
					
					if event.key == pygame.K_ESCAPE:
						start = True
						exit = True

	return [start, amount, middle, space]

def gameOver(screen, resolution, score, ground, background, bird):
	screen.fill(0)
	background.draw(screen, 0)
	ground.draw(screen, resolution[1])
	bird.draw(screen)
	score.end(resolution)
	font = pygame.font.Font("font/font.ttf", 40)
	screen.blit (font.render ("R - restart ", True, (0, 255, 0)), (200, 100))
	screen.blit (font.render ("ESC - exit ", True, (0, 255, 0)), (200, 200))
	pygame.display.flip()
	exit = False
	while not exit:
		for event in pygame.event.get():
				if event.type == pygame.QUIT:
					exit = True
					continua = False

				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_ESCAPE:
						exit = True
						continua =  False
				
					if event.key == pygame.K_r:
						exit = True
						continua =  True
	return continua
