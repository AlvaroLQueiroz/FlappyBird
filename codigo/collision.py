#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame

#Inicializa o mixe da pygame.
pygame.mixer.init()

#Som de colisão.
bump = pygame.mixer.Sound("sound/bump.ogg")

tolerance = 10

#Verifica a colisão do passaro com o chão e com o teto.
#Recebe como argumento um objeto do tipo Bird e uma lista com o tamanho da area disponivel para movimentação do passaro.
def topBottom(bird, resolution):
	#Bateu no teto.
	if bird.Position[1] < 0:
		return True
	#Bateu no chão.
	elif bird.Position[1] + bird.Size[1] > resolution[1]:
		return True
	#Não bateu.
	else:
		return False

#Verifica a colisão entre o passaro e os canos.
#Recebe como argumento um objeto do tipo Bird e um do tipo Pipe.
def birdPipes(bird, pipes, score):
	#Controla se outro colisão.
	hit = False
	
	#Percorre todos os canos superiores contidos no objeto pipes.
	counter = 0
	for pipe in pipes.top:
		if bird.Position[0] + bird.Size[0] - tolerance > pipe[1] and\
			bird.Position[0] < pipe[1] + pipe[0].get_width() and \
			bird.Position[1] < pipe[0].get_height(): 
			hit = True
		#Verifica se o passaro ultrapassou um cano por completo.
		if bird.Position[0] > pipe[1] + pipe[0].get_width() and not pipe[3]:
			score.point()
			pipes.setOverpast(counter)
		counter += 1

	
	#Percorre todos os canos inferiores contidos no objeto pipes.
	for pipe in pipes.bottom:
		if bird.Position[0] + bird.Size[0] - tolerance > pipe[1] and \
			bird.Position[0] < pipe[1] + pipe[0].get_width() and\
			bird.Position[1] + bird.Size[1] > pipe[2]:
			hit = True
	
	return hit

#Verifica se houve alguma colisão com o passaro.
def check(resolution, bird, pipes, score):
	if topBottom(bird, resolution) or birdPipes(bird, pipes, score):
			bump.play()
			return True
	else:
		return False

