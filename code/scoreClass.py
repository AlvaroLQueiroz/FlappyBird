import pygame

class Score:
	highscore = None
	sond = None
	screen = None
	def __init__(self, screen):
		self.highscore = 0
		self.sound = pygame.mixer.Sound("sound/point.ogg")
		self.screen = screen

	def point(self):
		self.highscore += 1
		self.sound.play()

	def draw(self, position):
		font = pygame.font.Font("font/font.ttf", 60)
		text = font.render (str(self.highscore), True, (255,255,255))
		self.screen.blit (text, position)
		
	def end(self, resolution):
		font = pygame.font.Font("font/font.ttf", 60)
		text = font.render (str(self.highscore), True, (255,255,255))
		self.screen.blit (text, [resolution[0] / 2, resolution[1] / 4])

	def reset(self):
		self.highscore = 0