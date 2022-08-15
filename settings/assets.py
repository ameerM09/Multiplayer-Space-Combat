from . import *

SPACE_BACKGROUND = pygame.transform.scale(pygame.image.load(os.path.join('assets/space_background.png')), (WIN_WIDTH, WIN_HEIGHT))

MAIN_MENU_LOGO = pygame.image.load(os.path.join('assets/space_combat_logo.png'))

MAIN_MENU_PLAY_BTN = pygame.transform.scale(pygame.image.load(os.path.join('assets/play_btn.png')), (PLAY_BTN_WIDTH, PLAY_BTN_HEIGHT))

# Modified player objects
PLAYER_A = pygame.image.load(os.path.join('assets/blue_spaceship.png'))

BLUE_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(PLAYER_A, (SHIP_WIDTH, SHIP_HEIGHT)), 270)

# Rotates and dilates image
PLAYER_B = pygame.image.load(os.path.join('assets/red_spaceship.png'))

RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(PLAYER_B, (SHIP_WIDTH, SHIP_HEIGHT)), 90)

HEART_HEALTH = pygame.transform.scale(pygame.image.load(os.path.join('assets/heart_health.png')), (HEART_WIDTH, HEART_HEIGHT))

PROJECTILE_SHOT = pygame.mixer.Sound('assets/projectile_shot.wav')

PROJECTILE_HIT = pygame.mixer.Sound('assets/projectile_hit.wav')
