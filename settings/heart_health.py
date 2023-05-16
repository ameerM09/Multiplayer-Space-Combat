from . import *

class Heart():
	def __init__(self, x, y, heart_image):
		self.x = x
		self.y = y 
		self.heart_image = heart_image

	def render(self, win):
		win.blit(self.heart_image, (self.x, self.y))