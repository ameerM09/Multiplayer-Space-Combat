from . import *

class Button():
	def __init__(self, x, y, btn_image):
		self.btn_image = btn_image
		self.rect = self.btn_image.get_rect()
		self.rect.topleft = (x, y)
		self.clicked = False

	def check_for_click(self):
		action = False
		cursor_pos = pygame.mouse.get_pos()

		if self.rect.collidepoint(cursor_pos):
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
				self.clicked = True
				action = True

			if pygame.mouse.get_pressed()[0] == 0:
				self.clicked = False

		return action

	def render(self, win):
		win.blit(self.btn_image, (self.rect.x, self.rect.y))