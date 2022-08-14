# Module import from settings package
from settings import *

SPACE_BACKGROUND = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'space_background.png')), (WIN_WIDTH, WIN_HEIGHT))

# Modified player objects
PLAYER_A = pygame.image.load(os.path.join('assets', 'blue_spaceship.png'))

BLUE_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(PLAYER_A, (SHIP_WIDTH, SHIP_HEIGHT)), 270)

# Rotates and dilates image
PLAYER_B = pygame.image.load(os.path.join('assets', 'red_spaceship.png'))

RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(PLAYER_B, (SHIP_WIDTH, SHIP_HEIGHT)), 90)

# Function to draw and update elements on screen
def draw_elements(player_blue, player_red, blue_projectile, red_projectile, player_blue_health, player_red_health, menu_bar):
    WIN.blit(SPACE_BACKGROUND, (0, 0))

    WIN.blit(BLUE_SPACESHIP, (player_blue.x, player_blue.y))

    WIN.blit(RED_SPACESHIP, (player_red.x, player_red.y))

    for projectile in blue_projectile:
        pygame.draw.rect(WIN, BLUE, projectile)

    for projectile in red_projectile:
        pygame.draw.rect(WIN, RED, projectile)

    pygame.draw.rect(WIN, PURPLE, menu_bar)

    if player_blue_health == 5:
        player_blue_hearts = [
            Heart(90, 0, HEART_HEALTH),
            Heart(140, 0, HEART_HEALTH),
            Heart(190, 0, HEART_HEALTH),
            Heart(240, 0, HEART_HEALTH),
            Heart(290, 0, HEART_HEALTH)
        ]

    elif player_blue_health == 4:
        player_blue_hearts = [
            Heart(115, 0, HEART_HEALTH),
            Heart(165, 0, HEART_HEALTH),
            Heart(215, 0, HEART_HEALTH),
            Heart(265, 0, HEART_HEALTH)
        ]

    elif player_blue_health == 3:
        player_blue_hearts = [
            Heart(140, 0, HEART_HEALTH),
            Heart(190, 0, HEART_HEALTH),
            Heart(240, 0, HEART_HEALTH)
        ]

    elif player_blue_health == 2:
        player_blue_hearts = [
            Heart(165, 0, HEART_HEALTH),
            Heart(215, 0, HEART_HEALTH)
        ]

    else:
        player_blue_hearts = [
            Heart(190, 0, HEART_HEALTH)
        ]

    for player_blue_heart in player_blue_hearts:
        player_blue_heart.draw(WIN)

    if player_red_health == 5:
        player_red_hearts = [
            Heart(550, 0, HEART_HEALTH),
            Heart(600, 0, HEART_HEALTH),
            Heart(650, 0, HEART_HEALTH),
            Heart(700, 0, HEART_HEALTH),
            Heart(750, 0, HEART_HEALTH)
        ]

    elif player_red_health == 4:
        player_red_hearts = [
            Heart(575, 0, HEART_HEALTH),
            Heart(625, 0, HEART_HEALTH),
            Heart(675, 0, HEART_HEALTH),
            Heart(725, 0, HEART_HEALTH)
        ]

    elif player_red_health == 3:
        player_red_hearts = [
            Heart(600, 0, HEART_HEALTH),
            Heart(650, 0, HEART_HEALTH),
            Heart(700, 0, HEART_HEALTH)
        ]

    elif player_red_health == 2:
        player_red_hearts = [
            Heart(625, 0, HEART_HEALTH),
            Heart(675, 0, HEART_HEALTH)
        ]

    else:
        player_red_hearts = [
            Heart(650, 0, HEART_HEALTH)
        ]

    for player_red_heart in player_red_hearts:
        player_red_heart.draw(WIN)

# Sets appropriate icon for pygame window
    pygame.display.set_icon(PLAYER_A)

# Draws barrier on screen using built-in pygame method 
    pygame.draw.rect(WIN, WHITE, BARRIER)

    pygame.display.update()

# Key bindings for blue spaceship
def key_bindings(on_key_pressed, player_blue, player_red):
# Additional conditions are added to add borders around screen
# Players cannot move outside of window or past barrier between the two
    if on_key_pressed[pygame.K_w] and player_blue.y - VELOCITY > 55:
        player_blue.y = player_blue.y - VELOCITY

    elif on_key_pressed[pygame.K_a] and player_blue.x - VELOCITY > 0:
        player_blue.x = player_blue.x - VELOCITY

    elif on_key_pressed[pygame.K_s] and player_blue.y + VELOCITY + player_blue.height < WIN_HEIGHT:
        player_blue.y = player_blue.y + VELOCITY

    elif on_key_pressed[pygame.K_d] and player_blue.x + VELOCITY + player_blue.width < BARRIER.x:
        player_blue.x = player_blue.x + VELOCITY

# Key bindings for red spaceship
    if on_key_pressed[pygame.K_UP] and player_red.y - VELOCITY > 55:
        player_red.y = player_red.y - VELOCITY

    elif on_key_pressed[pygame.K_LEFT] and player_red.x - VELOCITY > BARRIER.x:
        player_red.x = player_red.x - VELOCITY

    elif on_key_pressed[pygame.K_DOWN] and player_red.y + VELOCITY + player_red.height < WIN_HEIGHT: 
        player_red.y = player_red.y + VELOCITY

    elif on_key_pressed[pygame.K_RIGHT] and player_red.x + VELOCITY + player_red.width < WIN_WIDTH:
        player_red.x = player_red.x + VELOCITY

def projectile_functionality(player_blue, player_red, blue_projectile, red_projectile):
# Adds velocity to projectile because they move further away from (0, 0) on screen
    for projectile in blue_projectile:
        projectile.x = projectile.x + PROJECTILE_VELOCITY
        if player_red.colliderect(projectile):
            pygame.event.post(pygame.event.Event(PLAYER_RED_COLLISION))
            blue_projectile.remove(projectile)

# Must remove projectile from list when at the end of screen such that player's max bullets can be reset
        if projectile.x > WIN_WIDTH:
            blue_projectile.remove(projectile)

# Subtracts velocity from projectile coming from right as it gets closer to (0, 0) on screen
    for projectile in red_projectile:
        projectile.x = projectile.x - PROJECTILE_VELOCITY
        if player_blue.colliderect(projectile):
            pygame.event.post(pygame.event.Event(PLAYER_BLUE_COLLISION))
            red_projectile.remove(projectile)

# The x value of the projecetile must be less than (0, 0) at the left-hand end of the screen
        if projectile.x < 0:
            red_projectile.remove(projectile)

def render_game_winner(winner_text):
    RENDER_TEXT = RENDER_WINNER.render(winner_text, 1, NEON_GREEN)
    WIN.blit(RENDER_TEXT, (WIN_WIDTH // 2 - RENDER_TEXT.get_width() // 2, WIN_HEIGHT // 2 - RENDER_TEXT.get_height() // 2))

    pygame.display.update()
    pygame.time.delay(5000)

# Main game loop to run the program
def game_loop():
    player_blue = pygame.Rect(WIN_WIDTH // 4 - SHIP_WIDTH // 2, WIN_HEIGHT // 2 - SHIP_HEIGHT // 2, SHIP_WIDTH, SHIP_HEIGHT)
    player_red = pygame.Rect(WIN_WIDTH // 2 + SHIP_WIDTH * 3, WIN_HEIGHT // 2 - SHIP_HEIGHT // 2, SHIP_WIDTH, SHIP_HEIGHT)

    blue_projectile = []
    red_projectile = []

    menu_bar = pygame.Rect(0, 0, WIN_WIDTH, 55)

    player_blue_health = 5
    player_red_health = 5

    player_blue_winning_statements = [
        'BLUE WINS!',
        'A SPECTACULAR TAKEDOWN BY BLUE!',
        'WHAT A PRECISE SHOT FROM BLUE!'
    ]

    player_red_winning_statements = [
        'RED WINS!',
        'A SPECTACULAR TAKEDOWN BY RED!',
        'WHAT A PRECISE SHOT FROM RED!'
    ]

    refresh_rate = pygame.time.Clock()
    run = True

    while run:
        refresh_rate.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
    
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LALT and len(blue_projectile) < MAX_PROJECTILE_FIRE:
                    projectile = pygame.Rect(player_blue.x + player_blue.width, player_blue.y + player_blue.height // 2, 10, 5)
                    blue_projectile.append(projectile)

                elif event.key == pygame.K_RALT and len(red_projectile) < MAX_PROJECTILE_FIRE:
                    projectile = pygame.Rect(player_red.x, player_red.y + player_red.height // 2, 10, 5)
                    red_projectile.append(projectile)

# New events are posted to check if there is collision with projectile and either one of the players
            if event.type == PLAYER_BLUE_COLLISION:
                player_blue_health = player_blue_health - 1

            if event.type == PLAYER_RED_COLLISION:
                player_red_health = player_red_health - 1

        render_winner_text = ''
        if player_blue_health <= 0:
            WIN.blit(SPACE_BACKGROUND, (0, 0))
            render_winner_text = random.choice(player_red_winning_statements)

        if player_red_health <= 0:
            WIN.blit(SPACE_BACKGROUND, (0, 0))
            render_winner_text = random.choice(player_blue_winning_statements)

        if render_winner_text != '':
            render_game_winner(render_winner_text)
            break

# Variable to keep track of key bindings        
        on_key_pressed = pygame.key.get_pressed()

        key_bindings(on_key_pressed, player_blue, player_red)

        draw_elements(player_blue, player_red, blue_projectile, red_projectile, player_blue_health, player_red_health, menu_bar)

        projectile_functionality(player_blue, player_red, blue_projectile, red_projectile)

def main_menu(win):
    run = True

    while run:
        win.blit(SPACE_BACKGROUND, (0, 0))

        RENDER_MAIN_MENU = MENU_FONT.render('Press the mouse to begin...', 1, NEON_GREEN)

        win.blit(RENDER_MAIN_MENU, (WIN_WIDTH // 2 - RENDER_MAIN_MENU.get_width() // 2, WIN_HEIGHT // 2 - RENDER_MAIN_MENU.get_height() // 2 - 10))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run  = False

                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                game_loop()

        pygame.display.update()

main_menu(WIN)

if __name__ == '__main__':
    main_menu(WIN)
