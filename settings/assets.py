from . import *

SPACE_BACKGROUND = pygame.transform.scale(pygame.image.load(os.path.join('assets/space_background.png')), (WIN_WIDTH, WIN_HEIGHT))

MAIN_MENU_LOGO = pygame.image.load(os.path.join('assets/space_combat_logo.png'))

MAIN_MENU_PLAY_BTN = pygame.image.load(os.path.join('assets/start_btn.png'))

RESTART_BTN = pygame.transform.scale(pygame.image.load(os.path.join('assets/restart_btn.png')), (RESTART_BTN_WIDTH, RESTART_BTN_HEIGHT))

EXIT_BTN = pygame.transform.scale(pygame.image.load(os.path.join('assets/exit_btn.png')), (EXIT_BTN_WIDTH, EXIT_BTN_HEIGHT))

# Modified player objects
PLAYER_A = pygame.image.load(os.path.join('assets/blue_spaceship.png'))

BLUE_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(PLAYER_A, (SHIP_WIDTH, SHIP_HEIGHT)), 270)

# Rotates and dilates image
PLAYER_B = pygame.image.load(os.path.join('assets/red_spaceship.png'))

RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(PLAYER_B, (SHIP_WIDTH, SHIP_HEIGHT)), 90)

HEART_HEALTH = pygame.transform.scale(pygame.image.load(os.path.join('assets/heart_health.png')), (HEART_WIDTH, HEART_HEIGHT))

BLUE_WIN = pygame.image.load(os.path.join('assets/blue_winning_statement.png'))

RED_WIN = pygame.image.load(os.path.join('assets/red_winning_statement.png'))

# Game sound effects
PROJECTILE_SHOT = pygame.mixer.Sound('assets/projectile_shot.wav')

PROJECTILE_HIT = pygame.mixer.Sound('assets/projectile_hit.wav')

BTN_SOUND_EFFECT = pygame.mixer.Sound('assets/btn_sound_effect.wav')

# MP3 sound effects
pygame.mixer.music.load('assets/game_over.mp3')