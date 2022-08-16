from . import *

HEART_HEALTH = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'heart_health.png')), (HEART_HEIGHT, HEART_WIDTH))

class Heart():
	def __init__(self, x, y, heart_image):
		self.x = x
		self.y = y 
		self.heart_image = HEART_HEALTH

	def draw(self, win):
		win.blit(self.heart_image, (self.x, self.y))
