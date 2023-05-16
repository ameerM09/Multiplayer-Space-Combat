from . import *

class Scroller():
	MOVEMENT_VELOCITY = 1
	ASSET = SPACE_BACKGROUND
	ASSET_HEIGHT = SPACE_BACKGROUND.get_height()

	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.y1 = 0 
		self.y2 = self.ASSET_HEIGHT

	def drag_movement(self):
		self.y1 = self.y1 - self.MOVEMENT_VELOCITY
		self.y2 = self.y2 - self.MOVEMENT_VELOCITY

		if self.y1 + self.ASSET_HEIGHT < 0:
			self.y1 = self.y2 + self.ASSET_HEIGHT

		elif self.y2 + self.ASSET_HEIGHT < 0:
			self.y2 = self.y1 + self.ASSET_HEIGHT

	def render(self, win):
		win.blit(self.ASSET, (self.x, self.y1))
		win.blit(self.ASSET, (self.x, self.y2))