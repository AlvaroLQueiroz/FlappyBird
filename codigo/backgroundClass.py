import pygame

class Background:
	backgroundWidth = 0
	backgroundHeight = 0
	backgroundImg = None
	background = []
	
	def __init__(self, area):
		self.backgroundWidth  = int(area[0] / 10)
		self.backgroundHeight = area[1]
		self.backgroundImg = pygame.image.load("img/background.png")
		self.backgroundImg = pygame.transform.scale (self.backgroundImg, (self.backgroundWidth, self.backgroundHeight))
		for i in range(0, 10):
			self.background.append(i * self.backgroundWidth)
		
	def move(self, speed):
		if abs(self.background[0]) >= self.backgroundWidth:
			speed = -self.backgroundWidth
		for i in range(0, 10):
			self.background[i] -= speed
		
	def draw(self, screen, height):
		for i in range(0, 10):
			screen.blit(self.backgroundImg, (self.background[i], height))
