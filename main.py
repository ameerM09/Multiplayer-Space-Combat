# Module import from settings package
from settings import * 

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
        player_blue_heart.render(WIN)

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
            Heart(580, 0, HEART_HEALTH),
            Heart(630, 0, HEART_HEALTH),
            Heart(680, 0, HEART_HEALTH),
            Heart(730, 0, HEART_HEALTH)
        ]

    elif player_red_health == 3:
        player_red_hearts = [
            Heart(605, 0, HEART_HEALTH),
            Heart(655, 0, HEART_HEALTH),
            Heart(705, 0, HEART_HEALTH)
        ]

    elif player_red_health == 2:
        player_red_hearts = [
            Heart(630, 0, HEART_HEALTH),
            Heart(680, 0, HEART_HEALTH)
        ]

    else:
        player_red_hearts = [
            Heart(655, 0, HEART_HEALTH)
        ]

    for player_red_heart in player_red_hearts:
        player_red_heart.render(WIN)

    restart_btn = Button(5, 13, RESTART_BTN)

    restart_btn.render(WIN)

    if restart_btn.check_for_click():
        game_loop()

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

def render_game_winner(winning_img):
    WIN.blit(winning_img, (WIN_WIDTH // 2 - winning_img.get_width() // 2, WIN_HEIGHT // 2 - winning_img.get_height() // 2))

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
                    PROJECTILE_SHOT.play()

                elif event.key == pygame.K_RALT and len(red_projectile) < MAX_PROJECTILE_FIRE:
                    projectile = pygame.Rect(player_red.x, player_red.y + player_red.height // 2, 10, 5)
                    red_projectile.append(projectile)
                    PROJECTILE_SHOT.play()

# New events are posted to check if there is collision with projectile and either one of the players
            if event.type == PLAYER_BLUE_COLLISION:
                player_blue_health = player_blue_health - 1
                PROJECTILE_HIT.play()

            if event.type == PLAYER_RED_COLLISION:
                player_red_health = player_red_health - 1
                PROJECTILE_HIT.play()

        game_over = False

        if player_blue_health <= 0:

# Set to the maximum volume by default
            pygame.mixer.music.play()

            WIN.blit(SPACE_BACKGROUND, (0, 0))
            render_game_winner(RED_WIN)
            game_over = True

        if player_red_health <= 0:
            pygame.mixer.music.play()

            WIN.blit(SPACE_BACKGROUND, (0, 0))
            render_game_winner(BLUE_WIN)
            game_over = True

        if game_over:
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

        win.blit(MAIN_MENU_LOGO, (WIN_WIDTH // 2 - MAIN_MENU_LOGO.get_width() // 2, 50))

        play_btn = Button(WIN_WIDTH // 2 - MAIN_MENU_PLAY_BTN.get_width() // 2, 150, MAIN_MENU_PLAY_BTN)

        play_btn.render(WIN)
        
        if play_btn.check_for_click():
            BTN_SOUND_EFFECT.play()
            game_loop()

        exit_btn = Button(WIN_WIDTH // 2 - EXIT_BTN.get_width() // 2, 275, EXIT_BTN)

        exit_btn.render(WIN)

        if exit_btn.check_for_click():
            run = False
            pygame.quit()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run  = False

                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_loop()

        pygame.display.update()

main_menu(WIN)

if __name__ == '__main__':
    main_menu(WIN)