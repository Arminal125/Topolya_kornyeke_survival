import pygame
import time
import random
import pygame.mixer
import sys
import os
# from main_menu import play

from objects.caracter import *

pygame.font.init()
pygame.mixer.init()



WIDTH, HEIGHT = 1920, 1080
caracter_SIZE_INCREMENT = 50
santa_SIZE_INCREMENT = 50
hoember_SIZE_INCREMENT = 50

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Topolya környéke és uszoda 2023 november")



caracter_size = caracter_HEIGHT
hoember_size = HOEMBER_HEIGHT
santa_size = SANTA_HEIGHT


level_complete_sound_playing = False


class game():


    def __init__(self, height = 1080, width = 1920, , ):
        self.game_heihgt = height
        self.game_width = width

        self.level_complete_sound_playing
        self.start_time

        self.character = None
        self.santa = None
        self.hoember = None
        self.hopehely = None
        self.star = None
        self.gost = None


        def initialise_game():

            self.character = None
            self.santa = None
            self.hoember = None
            self.hopehely = None
            self.star = None
            self.gost = None



        global star_add_increment
        run = True
        clock = pygame.time.Clock()
        elapsed_time = 0

        global counter
        global direction
        global index
        global images_right
        global images_left
        global walk_cooldown
        global CARACTER_IMG
        global hoemberek
        global hopehelyek
        global santas
        global HOPEHELY_IMG
        global rotate_index
        global caracter


##############################   FUNCTIONS

# return background music
def get_background_musci(folder = "level_music"):
    backgtound_music = []
    for i in os.listdir(folder):
        backgtound_music.append(folder + '/' + i)

    return backgtound_music

# load background music
def load_background_music(background_music):
    loaded_background_music = [pygame.mixer.Sound(music) for music in background_music]

    return loaded_background_music



# return background themes
def get_background_themes(folder="level_themes"):
    backgtound_temak = []
    for i in os.listdir(folder):
        backgtound_temak.append(folder + '/' + i)

    return backgtound_temak

# return background themes
def load_background_themes(background_themes, height, width):
    loaded_background_themes = [pygame.transform.scale(pygame.image.load(themes), (width, height)) for themes in
                                background_themes]

    return loaded_background_themes

def load_background(backgrounds, index):
    return backgrounds[index]



def draw_ghost():
    for ghost in ghosts:
        screen.blit(GHOST_IMG, (ghost.x, ghost.y))

def draw_hoember():
    for hoember in hoemberek:
        screen.blit(HOEMBER_IMG, (hoember.x, hoember.y))

def draw_santa():
    for santa in santas:
        screen.blit(SANTA_IMG, (santa.x, santa.y))

def draw_hopehely():
    global HOPEHELY_IMG
    global rotate_index

    for hopehely in hopehelyek:
        screen.blit(pygame.transform.rotate(HOPEHELY_IMG, rotate_index), (hopehely.x, hopehely.y))

def handle_ghosts_collision():
    global hit, caracter_size
    for ghost in ghosts[:]:
        ghost.y += GHOST_VEL
        if ghost.y > HEIGHT:
            ghosts.remove(ghost)
        elif ghost.colliderect(caracter):
            ghosts.remove(ghost)
            hit = True
            new_width = caracter.width + caracter_SIZE_INCREMENT
            if new_width <= WIDTH:  # Ellenőrizze, hogy a karakter új szélessége elfér-e a képernyőn
                caracter.width = new_width
                print("caracter size increased to:", caracter.width)
            break

def handle_hoemberek_collision():
    global hit
    for hoember in hoemberek[:]:
        hoember.y += HOEMBER_VEL
        if hoember.y > HEIGHT:
            hoemberek.remove(hoember)
        elif hoember.colliderect(caracter):
            hoemberek.remove(hoember)
            hit = True
            new_width = caracter.width + hoember_SIZE_INCREMENT
            if new_width <= WIDTH:
                caracter.width = new_width
                print("caracter size increased to:", caracter.width)
            break

def handle_santas_collision():
    global hit
    for santa in santas[:]:
        santa.y += SANTA_VEL
        if santa.y > HEIGHT:
            santas.remove(santa)
        elif santa.colliderect(caracter):
            santas.remove(santa)
            hit = True
            new_width = caracter.width + caracter_SIZE_INCREMENT
            if new_width <= WIDTH:
                # Adjust the character's width and position
                caracter.x = min(caracter.x - (new_width - caracter.width), WIDTH - new_width)
                caracter.width = new_width
            break



def handle_hopehely_collision():
    global hit
    for hopehely in hopehelyek[:]:
        hopehely.y += HOPEHELY_VEL
        if hopehely.y > HEIGHT:
            hopehelyek.remove(hopehely)
        elif hopehely.colliderect(caracter):
            hopehelyek.remove(hopehely)
            hit = True
            new_height = caracter.height + caracter_SIZE_INCREMENT
            if new_height <= HEIGHT:  # Ellenőrizze, hogy a karakter új magassága elfér-e a képernyőn
                # Az új karakter pozícióját úgy állítsuk be, hogy a karakter teteje ne menjen ki a képernyőből
                caracter.y = min(caracter.y - (new_height - caracter.height), HEIGHT - new_height)
                caracter.height = new_height
                print("caracter height increased to:", caracter.height)
            break



# load all the background music
backround_theme_music = get_background_musci()
loaded_backroung_music = load_background_music(backround_theme_music)

# load all the background themes
backround_theme_pictures = get_background_themes()
loaded_backroung_thems = load_background_themes(backround_theme_pictures, HEIGHT, WIDTH)

# Level compleate zene sound
LEVEL_COMPLETE_SOUND = pygame.mixer.Sound("music/zeneatvezeto.mp3")

# Select font of the game
FONT = pygame.font.SysFont("comicsans", 30)

# Deklaráld a start_time változót globális változóként a főprogram tetején
start_time = time.time()
star_add_increment = 10000




def draw(caracter, elapsed_time, stars, background, ghosts, hoemberek, santas ,hopehelyek, caracter_size):
    screen.blit(background, (0, 0))

    time_text = FONT.render(f"Time: {round(elapsed_time)}s", 1, "red")
    screen.blit(time_text, (10, 10))

    # Rajzold ki a karakter képét a karakter pozícióján, figyelembe véve a méretét
    screen.blit(pygame.transform.scale(CARACTER_IMG, (caracter.width, caracter.height)), (caracter.x, caracter.y))

    for star in stars:
        pygame.draw.rect(screen, "white", star)

    draw_ghost()
    draw_hopehely()
    draw_hoember()
    draw_santa()

    pygame.display.update()

    for star in stars:
        pygame.draw.rect(screen, "white", star)

    draw_ghost()

    pygame.display.update()


def show_level_complete():
    global level_complete_sound_playing
    global caracter_size
    screen.fill((0, 0, 0))
    level_complete_text = FONT.render("Level Complete!", 1, "white")
    screen.blit(level_complete_text, (WIDTH / 2 - level_complete_text.get_width() / 2, HEIGHT / 2 -
                                      level_complete_text.get_height() / 2))

    pygame.display.update()
    # Stop the current background sound
    pygame.mixer.stop()
    # Play the common "Level Complete!" sound
    LEVEL_COMPLETE_SOUND.play()
    level_complete_sound_playing = True
    # Wait for a key press
    wait_for_key()
    # Reset caracter size to the original value
    #TODO: ################################################## berakni a resett funkciot
    self.character.return_default_size()

    level_complete_sound_playing = False



def wait_for_key():
    global level_complete_sound_playing
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                waiting = False
                if level_complete_sound_playing:
                    LEVEL_COMPLETE_SOUND.stop()  # Megállítja a "Level Complete" zenét
        pygame.time.delay(10)

def main1():
    global level_complete_sound_playing
    global start_time
    global star_add_increment
    run = True
    clock = pygame.time.Clock()
    elapsed_time = 0

    global counter
    global direction
    global index
    global images_right
    global images_left
    global walk_cooldown
    global CARACTER_IMG
    global hoemberek
    global hopehelyek
    global santas
    global HOPEHELY_IMG
    global rotate_index
    global caracter

    rotate_index = 0
    walk_cooldown = 5
    images_right = []
    images_left = []
    counter = 0
    index=0
    direction=0

    star_count = 0
    stars = []
    hoemberek = []
    hoember_count = 0
    santas = []
    hit = False
    caracter_size = caracter_HEIGHT  # Inicializáld a caracter_size változót itt


    # Kezdeti pozíció a képernyő alján, középen
    caracter.x = (WIDTH - caracter_WIDTH) // 2
    caracter.y = HEIGHT - caracter_HEIGHT



    # start the first background in the game
    current_background_index = 0
    current_background = load_background(current_background_index)

    # Zenék kezelése az elso zenet kezdi el jatszani
    loaded_backroung_music[0].set_volume(0.3)
    loaded_backroung_music[0].play(-1)


    #  player pictures
    for num in range(1, 5):
        img_right = pygame.image.load(f'playerx/guy{num}.png')
        img_right = pygame.transform.scale(img_right, (40, 80))
        img_left = pygame.transform.flip(img_right, True, False)

        images_right.append(img_right)
        images_left.append(img_left)


    # background sound handling
    for bg_music in loaded_backroung_music:
        bg_music.set_volume(0.3)
        # BG_SOUNDS[i].set_volume(0.3)

    # level compleate sound handling
    LEVEL_COMPLETE_SOUND.set_volume(0.5)


    # a jatekos kezdeti pozicioja
    player = Player((WIDTH - caracter_WIDTH) // 2, HEIGHT - caracter_HEIGHT)

    # start the game
    while run:
        star_count += clock.tick(60)
        elapsed_time = time.time() - start_time




        # setup the count of each object and start to go on scree
        # do some auto stuff to send to screen

        if star_count > star_add_increment:
            for _ in range(current_background_index + 1):  # Csillagok számának növelése

                # Ghost caracter elinditasa
                ghost_x = random.randint(0, WIDTH - GHOST_WIDTH)
                ghost = pygame.Rect(ghost_x, -GHOST_HEIGHT, GHOST_WIDTH, GHOST_HEIGHT)
                ghosts.append(ghost)


                # object_hopehely start
                hopehely_x = random.randint(0, WIDTH - HOPEHELY_WIDTH)
                hopehely = pygame.Rect(hopehely_x, -HOPEHELY_HEIGHT, HOPEHELY_WIDTH, HOPEHELY_HEIGHT)
                hopehelyek.append(hopehely)

                # csillagok elinditasa
                star_x = random.randint(0, WIDTH - STAR_WIDTH)
                star = pygame.Rect(star_x, -STAR_HEIGHT, STAR_WIDTH, STAR_HEIGHT)
                stars.append(star)

                # hoember elinditasa
                hoember_x = random.randint(0, WIDTH - HOEMBER_WIDTH)
                hoember = pygame.Rect(hoember_x, -HOEMBER_HEIGHT, HOEMBER_WIDTH, HOEMBER_HEIGHT)
                hoemberek.append(hoember)

                # Santa elinditasa
                santa_x = WIDTH // 2 - SANTA_WIDTH // 2  # A képernyő közepén helyezze el a Santát
                santa = pygame.Rect(santa_x, 0, SANTA_WIDTH, SANTA_HEIGHT)  # A képernyő tetején jelenjen meg
                santas.append(santa)




            star_add_increment = max(200, star_add_increment - 50)
            star_count = 0


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break






        for star in stars[:]:
            star.y += STAR_VEL
            if star.y > HEIGHT:
                stars.remove(star)
            elif star.y + star.height >= caracter.y and star.colliderect(caracter):
                stars.remove(star)
                hit = True
                break

        for hoember in hoemberek[:]:
            hoember.y += HOEMBER_VEL
            if hoember.y > HEIGHT:
                hoemberek.remove(hoember)
            elif hoember.y + hoember.height >= caracter.y and hoember.colliderect(caracter):
                hoemberek.remove(hoember)
                hit = True
                break

        for santa in santas[:]:
            santa.y += SANTA_VEL
            if santa.y > HEIGHT:
                santas.remove(santa)
            elif santa.y + santa.height >= caracter.y and santa.colliderect(caracter):
                santas.remove(santa)
                hit = True
                break


        # rotate the star
        if rotate_index >= 360:
            rotate_index = 0
        else:
            rotate_index = rotate_index + 1


        # Draw caracter
        game_over = player.update(game_over)





        # if player has died
        if game_over == -1:
            if restart_button.draw():
                world_data = []
                world = reset_level(level)
                game_over = 0
                score = 0

        # if player has completed the level
        if game_over == 1:
            # reset game and go to next level
            level += 1
            if level <= max_levels:
                # reset level
                world_data = []
                world = reset_level(level)
                game_over = 0
            else:
                draw_text('YOU WIN!', font, blue, (screen_width // 2) - 140, screen_height // 2)
                if restart_button.draw():
                    level = 1
                    # reset level
                    world_data = []
                    world = reset_level(level)
                    game_over = 0
                    score = 0






        handle_ghosts_collision()
        handle_hopehely_collision()
        handle_hoemberek_collision()
        handle_santas_collision()

        if hit:
            lost_text = FONT.render("You Lost!", 1, "white")
            screen.blit(lost_text, (WIDTH / 2 - lost_text.get_width() / 2, HEIGHT / 2 - lost_text.get_height() / 2))
            pygame.display.update()
            pygame.time.delay(4000)
            pygame.quit()
            sys.exit()

        if elapsed_time >= 60 and not level_complete_sound_playing:
            show_level_complete()

            current_background_index += 1
            if current_background_index < len(background_list):
                current_background = background_list[current_background_index]
                BG_SOUNDS[current_background_index].play(-1)
                star_add_increment += 10

                # Állítsd vissza a karakter eredeti méreteit
                caracter.width = caracter_WIDTH
                caracter.height = caracter_HEIGHT

                # Kezdeti pozíció a képernyő alján, középen
                caracter.x = (WIDTH - caracter_WIDTH) // 2
                caracter.y = HEIGHT - caracter_HEIGHT
            else:
                run = False
                break

            start_time = time.time()
            hoember_time = time.time()

        if level_complete_sound_playing:
            continue

        draw(caracter, elapsed_time, stars, current_background, ghosts, hoemberek, santas, hopehelyek, caracter_size)

    if current_background_index == len(background_list) and not hit:
        screen.fill((0, 0, 0))
        won_text = FONT.render("Congratulations! You won the game!", 1, "white")
        screen.blit(won_text, (WIDTH / 2 - won_text.get_width() / 2, HEIGHT / 2 - won_text.get_height() / 2))
        pygame.display.update()
        pygame.time.delay(5000)

        # Állítsd vissza a karakter eredeti méreteit
        caracter.width = caracter_WIDTH
        caracter.height = caracter_HEIGHT

        # Kezdeti pozíció a képernyő alján, középen
        caracter.x = (WIDTH - caracter_WIDTH) // 2
        caracter.y = HEIGHT - caracter_HEIGHT

    pygame.quit()



while run:

    clock.tick(fps)

    screen.blit(bg_img, (0, 0))
    screen.blit(sun_img, (100, 100))

    if main_menu == True:
        if exit_button.draw():
            run = False
        if start_button.draw():
            main_menu = False
    else:
        world.draw()

        if game_over == 0:
            blob_group.update()
            platform_group.update()
            # update score
            # check if a coin has been collected
            if pygame.sprite.spritecollide(player, coin_group, True):
                score += 1
                coin_fx.play()
            draw_text('X ' + str(score), font_score, white, tile_size - 10, 10)

        blob_group.draw(screen)
        platform_group.draw(screen)
        lava_group.draw(screen)
        coin_group.draw(screen)
        exit_group.draw(screen)

        game_over = player.update(game_over)

        # if player has died
        if game_over == -1:
            if restart_button.draw():
                world_data = []
                world = reset_level(level)
                game_over = 0
                score = 0

        # if player has completed the level
        if game_over == 1:
            # reset game and go to next level
            level += 1
            if level <= max_levels:
                # reset level
                world_data = []
                world = reset_level(level)
                game_over = 0
            else:
                draw_text('YOU WIN!', font, blue, (screen_width // 2) - 140, screen_height // 2)
                if restart_button.draw():
                    level = 1
                    # reset level
                    world_data = []
                    world = reset_level(level)
                    game_over = 0
                    score = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()






# if __name__ == "__main__":
#     global caracter
#     caracter = pygame.Rect(200, HEIGHT - caracter_HEIGHT, caracter_WIDTH, caracter_HEIGHT)
#     main()