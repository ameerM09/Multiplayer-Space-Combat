# Potential game module to add an option for players to choose the type of spaceship they use

from . import *

def draw_shop_elements(win, menu_bar, main_menu, player_one_shop, player_two_shop):
	win.blit(SPACE_BACKGROUND, (0, 0))

	pygame.draw.rect(win, PURPLE, menu_bar)

	return_menu_btn.render(win)

	win.blit(player_one_shop, (WIN_WIDTH // 4 - player_one_shop.get_width() // 2, 16))

	win.blit(player_two_shop, (WIN_WIDTH // 2 + player_two_shop.get_width() // 2 - 20, 16))

	pygame.draw.rect(WIN, WHITE, BARRIER)

	if return_menu_btn.check_for_click():
		BTN_SOUND_EFFECT.play()
		main_menu(win)

def draw_ships():
	pass

def shop_screen(win, main_menu):
	run = True

	while run:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

				pygame.quit()

		draw_shop_elements(win, menu_bar, main_menu, PLAYER_ONE_SHOP, PLAYER_TWO_SHOP)
		draw_ships()

		pygame.display.update()