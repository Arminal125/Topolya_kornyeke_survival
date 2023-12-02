import pygame
import time
import random
import pygame.mixer
import sys
# from main_menu import play


pygame.font.init()
pygame.mixer.init()


caracter_WIDTH = 40
caracter_HEIGHT = 60
caracter_VEL = 5


GHOST_WIDTH = 50
GHOST_HEIGHT = 80
GHOST_VEL = 4

HOEMBER_WIDTH = 50
HOEMBER_HEIGHT = 70
HOEMBER_VEL = 3

SANTA_WIDTH = 50
SANTA_HEIGHT = 70
SANTA_VEL = 3

HOPEHELY_WIDTH = 40
HOPEHELY_HEIGHT = 60
HOPEHELY_VEL = 4

HOPEHELY_IMG = pygame.transform.scale(pygame.image.load("object_hopehely/hopehely.png"), (HOPEHELY_WIDTH, HOPEHELY_HEIGHT))


GHOST_IMG = pygame.transform.scale(pygame.image.load("object_ghost/szellem.png"), (GHOST_WIDTH, GHOST_HEIGHT))
CARACTER_IMG = pygame.transform.scale(pygame.image.load("themes/caracter.png"), (caracter_WIDTH, caracter_HEIGHT))
HOEMBER_IMG = pygame.transform.scale(pygame.image.load("object_hoember/hoember.png"), (HOEMBER_WIDTH, HOEMBER_HEIGHT))
SANTA_IMG = pygame.transform.scale(pygame.image.load("object_santa/Santa.png"), (SANTA_WIDTH, SANTA_HEIGHT))

global counter
global index
global images_right
global images_left
global caracter
rotate_index = 0
WIDTH, HEIGHT = 1920, 1080
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Topolya környéke és uszoda 2023 november")

BG_SOUNDS = [
    pygame.mixer.Sound("level_music/zene1.mp3"),
    pygame.mixer.Sound("level_music/zene2.mp3"),
    pygame.mixer.Sound("level_music/zene3.mp3"),
    pygame.mixer.Sound("level_music/zene4.mp3"),
    pygame.mixer.Sound("level_music/zene5.mp3"),
    pygame.mixer.Sound("level_music/zene6.mp3"),
    pygame.mixer.Sound("level_music/zene7.mp3"),
    pygame.mixer.Sound("level_music/zene8.mp3"),
    pygame.mixer.Sound("level_music/zene9.mp3"),
    pygame.mixer.Sound("level_music/zene10.mp3"),
]

BG = pygame.transform.scale(pygame.image.load("level_themes/Kep01.jpg"), (WIDTH, HEIGHT))
BG1 = pygame.transform.scale(pygame.image.load("level_themes/Kep02.jpg"), (WIDTH, HEIGHT))
BG2 = pygame.transform.scale(pygame.image.load("level_themes/Kep03.jpg"), (WIDTH, HEIGHT))
BG3 = pygame.transform.scale(pygame.image.load("level_themes/Kep04.jpg"), (WIDTH, HEIGHT))
BG4 = pygame.transform.scale(pygame.image.load("level_themes/Kep05.jpg"), (WIDTH, HEIGHT))
BG5 = pygame.transform.scale(pygame.image.load("level_themes/Kep06.jpg"), (WIDTH, HEIGHT))
BG6 = pygame.transform.scale(pygame.image.load("level_themes/Kep07.jpg"), (WIDTH, HEIGHT))
BG7 = pygame.transform.scale(pygame.image.load("level_themes/Kep08.jpg"), (WIDTH, HEIGHT))
BG8 = pygame.transform.scale(pygame.image.load("level_themes/Kep09.jpg"), (WIDTH, HEIGHT))
BG9 = pygame.transform.scale(pygame.image.load("level_themes/Kep010.jpg"), (WIDTH, HEIGHT))

backgrounds = [pygame.transform.scale(pygame.image.load(f"level_themes/Kep0{i + 1}.jpg"), (WIDTH, HEIGHT)) for i in range(10)]
sounds = [pygame.mixer.Sound(f"level_music/zene{i + 1}.mp3") for i in range(10)]

LEVEL_COMPLETE_SOUND = pygame.mixer.Sound("music/zeneatvezeto.mp3")

STAR_WIDTH = 10
STAR_HEIGHT = 20
STAR_VEL = 3

FONT = pygame.font.SysFont("comicsans", 30)

# Deklaráld a start_time változót globális változóként a főprogram tetején
start_time = time.time()
star_add_increment = 10000

level_complete_sound_playing = False

def load_background(index):
    return pygame.transform.scale(pygame.image.load(f"level_themes/Kep0{index + 1}.jpg"), (WIDTH, HEIGHT))

ghosts = []
hopehelyek = []
hoemberek = []
santas = []

def draw_ghost():
    for ghost in ghosts:
        WIN.blit(GHOST_IMG, (ghost.x, ghost.y))

def draw_hoember():
    for hoember in hoemberek:
        WIN.blit(HOEMBER_IMG, (hoember.x, hoember.y))

def draw_santa():
    for santa in santas:
        WIN.blit(SANTA_IMG, (santa.x, santa.y))

def draw_hopehely():
    global HOPEHELY_IMG
    global rotate_index

    for hopehely in hopehelyek:
        # HOPEHELY_IMG = pygame.transform.rotate(HOPEHELY_IMG, rotate_index)
        WIN.blit(pygame.transform.rotate(HOPEHELY_IMG, rotate_index), (hopehely.x, hopehely.y))

caracter_SIZE_INCREMENT = 50

caracter_size = caracter_HEIGHT

hoember_SIZE_INCREMENT = 50
hoember_size = HOEMBER_HEIGHT

santa_SIZE_INCREMENT = 50
santa_size = SANTA_HEIGHT


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


def draw(caracter, elapsed_time, stars, background, ghosts, hoemberek, santas ,hopehelyek, caracter_size):
    WIN.blit(background, (0, 0))

    time_text = FONT.render(f"Time: {round(elapsed_time)}s", 1, "red")
    WIN.blit(time_text, (10, 10))

    # Rajzold ki a karakter képét a karakter pozícióján, figyelembe véve a méretét
    WIN.blit(pygame.transform.scale(CARACTER_IMG, (caracter.width, caracter.height)), (caracter.x, caracter.y))

    for star in stars:
        pygame.draw.rect(WIN, "white", star)

    draw_ghost()
    draw_hopehely()
    draw_hoember()
    draw_santa()

    pygame.display.update()

    for star in stars:
        pygame.draw.rect(WIN, "white", star)

    draw_ghost()

    pygame.display.update()


def show_level_complete():
    global level_complete_sound_playing
    global caracter_size
    WIN.fill((0, 0, 0))
    level_complete_text = FONT.render("Level Complete!", 1, "white")
    WIN.blit(level_complete_text, (WIDTH / 2 - level_complete_text.get_width() / 2, HEIGHT / 2 -
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
    caracter.width = caracter_WIDTH
    caracter.height = caracter_HEIGHT

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


    for num in range(1, 5):
        img_right = pygame.image.load(f'playerx/guy{num}.png')
        img_right = pygame.transform.scale(img_right, (40, 80))
        img_left = pygame.transform.flip(img_right, True, False)


        images_right.append(img_right)
        images_left.append(img_left)

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

    background_list = [load_background(i) for i in range(10)]
    current_background_index = 0
    current_background = background_list[current_background_index]

    # Zenék kezelése
    BG_SOUNDS[0].set_volume(0.3)
    BG_SOUNDS[0].play(-1)

    for i in range(1, len(BG_SOUNDS)):
        BG_SOUNDS[i].set_volume(0.3)

    LEVEL_COMPLETE_SOUND.set_volume(0.5)

    while run:
        star_count += clock.tick(60)
        elapsed_time = time.time() - start_time

        if star_count > star_add_increment:
            for _ in range(current_background_index + 1):  # Csillagok számának növelése
                ghost_x = random.randint(0, WIDTH - GHOST_WIDTH)
                ghost = pygame.Rect(ghost_x, -GHOST_HEIGHT, GHOST_WIDTH, GHOST_HEIGHT)
                ghosts.append(ghost)
                hopehely_x = random.randint(0, WIDTH - HOPEHELY_WIDTH)
                hopehely = pygame.Rect(hopehely_x, -HOPEHELY_HEIGHT, HOPEHELY_WIDTH, HOPEHELY_HEIGHT)
                hopehelyek.append(hopehely)
                star_x = random.randint(0, WIDTH - STAR_WIDTH)
                star = pygame.Rect(star_x, -STAR_HEIGHT, STAR_WIDTH, STAR_HEIGHT)
                stars.append(star)
                hoember_x = random.randint(0, WIDTH - HOEMBER_WIDTH)
                hoember = pygame.Rect(hoember_x, -HOEMBER_HEIGHT, HOEMBER_WIDTH, HOEMBER_HEIGHT)
                hoemberek.append(hoember)
                santa_x = WIDTH // 2 - SANTA_WIDTH // 2  # A képernyő közepén helyezze el a Santát
                santa = pygame.Rect(santa_x, 0, SANTA_WIDTH, SANTA_HEIGHT)  # A képernyő tetején jelenjen meg
                santas.append(santa)

            star_add_increment = max(200, star_add_increment - 50)
            star_count = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and caracter.x - caracter_VEL >= 0:
            caracter.x -= caracter_VEL
            # variables to move the caracter
            counter += 1
            direction = -1
        if keys[pygame.K_RIGHT] and caracter.x + caracter_VEL + caracter.width <= WIDTH:
            caracter.x += caracter_VEL
            counter += 1
            direction = 1

        # variables to move the caracter
        if keys[pygame.K_LEFT] == False and keys[pygame.K_RIGHT] == False:
            counter = 0
            index = 0
            if direction == 1:
                CARACTER_IMG = images_right[index]
            if direction == -1:
                CARACTER_IMG = images_left[index]

        # stuff for moving the caracter, ad the picture to show
        if counter > walk_cooldown:
            counter = 0
            index += 1
            if index >= len(images_right):
                index = 0
            if direction == 1:
                CARACTER_IMG = images_right[index]
            if direction == -1:
                CARACTER_IMG = images_left[index]

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

        if rotate_index >= 360:
            rotate_index = 0
        else:
            rotate_index = rotate_index + 1


        handle_ghosts_collision()
        handle_hopehely_collision()
        handle_hoemberek_collision()
        handle_santas_collision()

        if hit:
            lost_text = FONT.render("You Lost!", 1, "white")
            WIN.blit(lost_text, (WIDTH / 2 - lost_text.get_width() / 2, HEIGHT / 2 - lost_text.get_height() / 2))
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
        WIN.fill((0, 0, 0))
        won_text = FONT.render("Congratulations! You won the game!", 1, "white")
        WIN.blit(won_text, (WIDTH / 2 - won_text.get_width() / 2, HEIGHT / 2 - won_text.get_height() / 2))
        pygame.display.update()
        pygame.time.delay(5000)

        # Állítsd vissza a karakter eredeti méreteit
        caracter.width = caracter_WIDTH
        caracter.height = caracter_HEIGHT

        # Kezdeti pozíció a képernyő alján, középen
        caracter.x = (WIDTH - caracter_WIDTH) // 2
        caracter.y = HEIGHT - caracter_HEIGHT

    pygame.quit()

if __name__ == "__main__":
    global caracter
    caracter = pygame.Rect(200, HEIGHT - caracter_HEIGHT, caracter_WIDTH, caracter_HEIGHT)
    main1()