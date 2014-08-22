import pygame

class Ground:
	groundWidth = 0
	groundHeight = 0
	groundImg = None
	ground = []
	
	def __init__(self, area):
		self.groundWidth  = int(area[0] / 10)
		self.groundHeight = area[1]
		self.groundImg = pygame.image.load("img/ground.png")
		self.groundImg = pygame.transform.scale (self.groundImg, (self.groundWidth, self.groundHeight))
		for i in range(0, 10):
			self.ground.append(i * self.groundWidth)

	def move(self, speed):
		if abs(self.ground[0]) >= self.groundWidth:
			speed = -self.groundWidth
		for i in range(0, 10):
			self.ground[i] -= speed
		
	def draw(self, screen, height):
		for i in range(0, 10):
			screen.blit(self.groundImg, (self.ground[i], height - self.groundHeight))
