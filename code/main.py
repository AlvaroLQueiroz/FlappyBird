#!/usr/bin/python
# -*- coding: utf-8 -*-
 
import pygame, sys
from random import randint
from birdClass import *
from groundClass import *
from backgroundClass import *
from pipeClass import *
import collision
import scoreClass
import menu

pygame.init() #Inicializa PyGame.

#Obtem as informacoes de video e seta a resolucao da janela.
videoInfo  = pygame.display.Info()
resolution = (videoInfo.current_w, videoInfo.current_h)
screen = pygame.display.set_mode(resolution, pygame.FULLSCREEN)


pygame.display.set_caption("Flappy Bird 1.0")#Seta o nome da janela

terrain = [resolution[0] * 2, int(resolution[1] * 0.3)]#Area do terreno.

skye = [resolution[0] * 2, resolution[1] - terrain[1]]#Area onde o passaro se movimenta.

bird = Bird([50, 50], [100, 100], 5, 40)#Cria um objeto passaro. ([tamanhoW, tamanhoH], [posicaoW, posicaoH], velocidadeDeQueda, alturaDoPulo)

#Cria um objeto terreno. ([tamanhoW, tamanhoH]).
#Obs: O tamanhoW é o dobro da resolucao da tela, para possibilitar o efeito de movimento
ground = Ground(terrain)

#Cria um objeto fundo. ([tamanhoW, tamanhoH]).
#Obs: O tamanhoW é o dobro da resolucao da tela, para possibilitar o efeito de movimento
background = Background(skye)

options = menu.menu(screen, resolution, ground, background, bird)

pipe = Pipe(80, options[1], options[2], options[3], skye)#Cria um objeto cano. (largura, quantidade, espaçoEntreSuperiorEInferior, AreaDisponivel)

score = scoreClass.Score(screen)#Cria um objeto do tipo Score.

#Inicializa o relogio do jogo.
clock = pygame.time.Clock()

#Controla o fim do jogo.
exit = options[0]

#Controla o fim da partida.
done = False
hit = False
#Controla o tempo entre cada pulo.
delayJump = 0

#Controla a ultima ação do passaro.
jumped = False

#Loop principal.
while not exit:
	if not done and not hit:
		screen.fill(0)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP and jumped == False:
					Jumped = True
					delayJump = pygame.time.get_ticks()
					bird.jump()
				if event.key == pygame.K_ESCAPE:
					done = True

			if event.type == pygame.KEYUP:
				if event.key == pygame.K_UP:
					jumped = False
		if pygame.time.get_ticks() - delayJump > 200:
			bird.fall()

		#Move os elementos.
		ground.move(5)
		background.move(5)
		pipe.move(5)

		#Imprime os elementos do jogo.
		background.draw(screen, 0)
		ground.draw(screen, resolution[1])
		pipe.draw(screen)
		bird.draw(screen)
		score.draw([resolution[0] / 2, 10])
		
		#Verifica se houve uma colisão
		hit = collision.check([resolution[0], resolution[1] - int(resolution[1] * 0.3)], bird, pipe, score)

	else:
		if menu.gameOver(screen, resolution, score, ground, background, bird):
			options = menu.menu(screen, resolution, ground, background, bird)
			pipe.reset()
			pipe = Pipe(80, options[1], options[2], options[3], skye)#Cria um objeto cano. (largura, quantidade, espaçoEntreSuperiorEInferior, AreaDisponivel)
			score.reset()
			done = options[0]
			hit = options[0]
			bird.setPosition([100,100])
		else:
			exit = True

	pygame.display.flip()
	clock.tick(60)

pygame.quit()
sys.exit()
