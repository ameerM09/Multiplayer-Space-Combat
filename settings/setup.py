from . import *

# Constant variables
WIN_WIDTH = 900
WIN_HEIGHT = 550
CAPTION = 'Space Combat'

# Sets the position of hte barrier between two players
BARRIER = pygame.Rect((WIN_WIDTH // 2) - 5, 0, 3, WIN_HEIGHT)

# Screen display
WIN = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption(CAPTION)

# Setting colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
PURPLE = (80, 0, 215)
RED = (255, 0, 0)
NEON_GREEN = (25, 225, 25)

# Sets the refresh rate of the game
FPS = 60

# Setting new pygame events for projectile colissions
PLAYER_BLUE_COLLISION = pygame.USEREVENT + 1
PLAYER_RED_COLLISION = pygame.USEREVENT + 2

# Sets velocity of player and bullet movements
VELOCITY = 5
PROJECTILE_VELOCITY = 8

# Scale factors for ship dilations
SHIP_WIDTH = 64
SHIP_HEIGHT = 64

# Maximum number of bullets that can be fired at once
MAX_PROJECTILE_FIRE = 3

# Sets fonts used in game
RENDER_WINNER = pygame.font.SysFont('Comicsans', 45)
