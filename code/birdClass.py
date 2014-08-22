import pygame

class Bird:
	Size = [0, 0]
	Position = [0, 0]
	fallingSpeed = 0
	heightJump = 0
	Img = None
	Jumping = None
	Falling = None
	falling = None
	sond = None
	
	def __init__(self, size, position, speed, jump):
		self.Size  = size
		self.Position = position
		self.fallingSpeed = speed
		self.heightJump = jump
		self.Jumping = pygame.image.load("img/birdJumping.png")
		self.Jumping = pygame.transform.scale (self.Jumping, self.Size)
		self.Falling = pygame.image.load("img/birdFalling.png")
		self.Falling = pygame.transform.scale (self.Falling, self.Size)
		self.Img = self.Jumping
		self.falling = False
		self.sound = pygame.mixer.Sound("sound/jump.ogg")
	
	def setPosition(self, position):
		self.Position = position
	
	def jump(self):
		self.sound.play()
		if self.falling:
			self.Img = self.Jumping
			self.falling = False
		self.Position[1] -= self.heightJump

	def fall(self):
		if not self.falling:
			self.Img = self.Falling
			self.falling = True
		self.Position[1] += self.fallingSpeed

	def draw(self, screen):
		screen.blit (self.Img, self.Position)

