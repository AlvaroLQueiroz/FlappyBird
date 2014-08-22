#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame
from random import randint

#Define um objeto do tipo cano. Esse objeto funciona como um grupo de outros objetos(quantidade definida em amount), ele possui duas lista(top e bottom) uma contendo todos os canos superiores e a outra todos os canos inferiores, essas listas contem as seguintes informacoes, [imagemDoCanoJaRedimenssionada, posicaoHorizontal, PosicaoVertical] e a lista top ainda contem um campo a mais que é usado para controlar a pontuaçao do jogador. Os canos sao gerados pseudos-aleatoriamente em um espaço definido por availableArea e sempre em uma posicao após o ultimo cano da lista. Obs.: Para um bom funcionamento a area disponivel para criacao dos canos deve ter o dobro da resolucao da tela e deve se iniciar apoós o meio da tela.
class Pipe:
	amount = 0 #Quantidade de canos
	width = 0 #Largura dos canos
	space = 0 #Espaço entre o cano superior e o inferior
	top = [] #lista de canos superiores
	bottom = [] #lista de canos inferiores
	availableArea = [] #Area disponivel para a criacao dos canos
	distance = 0
	def __init__(self, width, amount, space, distance, resolution):
		self.amount = amount
		self.width = width
		self.availableArea = resolution
		self.space = space
		self.distance = distance * width
		for i in range(0, self.amount):
			self.generate()
	
	def generate(self):
		#Se houver algum cano na lista, ele sera posicionado a uma distancia fixa do ultimo cano, se nao houver nenhum ele sera posicionado no meio da area disponivel.
		if len(self.top) > 0:
			w = self.top[len(self.top)-1][1] + self.distance
			
		else:
			w = self.availableArea[0] / 2

		#Gera uma altura pseudo-aleatoria para o espaco entre o cano superior e inferior.
		h = randint(0, self.availableArea[1] - self.space)
		
		self.top.append([pygame.transform.scale (pygame.image.load("img/pipeTop.png"), (self.width, h)), w, 0, False])
		self.bottom.append([pygame.transform.scale (pygame.image.load("img/pipeBottom.png"), (self.width, self.availableArea[1] - h - self.space)), w, h + self.space])

	#Movimenta os canos pela quantidade de pixel definida em speed.
	def move(self, speed):
		#Se o primeiro cano ja tiver saido da area de visualizacao ele é excluido da lista.
		if self.top[0][1] + self.width < 0:
			self.top.pop(0)
			self.bottom.pop(0)
			self.generate()

		for i in range(self.amount):
			self.top[i][1] -= speed
			self.bottom[i][1] -= speed
			
	
	def draw(self, screen):
		for i in range(0, self.amount):
			screen.blit(self.top[i][0], (self.top[i][1], self.top[i][2]))
			screen.blit(self.bottom[i][0], (self.bottom[i][1], self.bottom[i][2]))

	def setOverpast(self, position):
		self.top[position][3] = True

	def reset(self):
		for i in range(len(self.top)):
			self.top.pop()
			self.bottom.pop()

		self.amount = 0
		self.width = 0
		self.space = 0
		self.top = []
		self.bottom = []
		self.availableArea = []
		self.distance = 0