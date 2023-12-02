import pygame
import sys
from button import Button
from main import *
from main import main1 as start_game

game_started = False
global caracter


pygame.init()

WIDTH, HEIGHT = 1920, 1080
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Menu")

BG0 = pygame.image.load("assets/Background.jpg")
BG0 = pygame.transform.scale(BG0, (WIDTH, HEIGHT))  # Háttérkép méretezése a képernyő méretére

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

def get_font(size):
    return pygame.font.Font("assets/font.ttf", size)

def play():
    global game_started
    global caracter
    global HEIGHT ,caracter_HEIGHT, caracter_WIDTH, caracter_HEIGHT
    running = True
    caracter = pygame.Rect(200, HEIGHT - caracter_HEIGHT, caracter_WIDTH, caracter_HEIGHT)
    main()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()





        background = pygame.Surface((WIDTH, HEIGHT))
        background.blit(BG0, (0, 0))  # Háttérkép kirajzolása

        PLAY_TEXT = get_font(45).render("This is the PLAY screen.", True, WHITE)
        PLAY_RECT = PLAY_TEXT.get_rect(center=(WIDTH // 2, HEIGHT // 4))
        background.blit(PLAY_TEXT, PLAY_RECT)

        PLAY_BACK = Button(image=None, pos=(WIDTH // 2, HEIGHT // 2),
                           text_input="BACK", font=get_font(75), base_color=WHITE, hovering_color=GREEN)

        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(background)

        SCREEN.blit(background, (0, 0))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    game_started = False  # Játék befejezése, visszatérés a főmenübe
                    return

def options():
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        background = pygame.Surface((WIDTH, HEIGHT))
        background.blit(BG0, (0, 0))  # Háttérkép kirajzolása

        OPTIONS_TEXT = get_font(45).render("This is the OPTIONS screen.", True, BLACK)
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(WIDTH // 2, HEIGHT // 4))
        background.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None, pos=(WIDTH // 2, HEIGHT // 2),
                             text_input="BACK", font=get_font(75), base_color=BLACK, hovering_color=GREEN)

        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()
        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(background)

        SCREEN.blit(background, (0, 0))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    return

# def start_game():
#     global game_started
#     game_started = True
#     pygame.mixer.stop()
#     main1()

def main_menu():
    global game_started
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        background = pygame.Surface((WIDTH, HEIGHT))
        background.blit(BG0, (0, 0))  # Háttérkép kirajzolása

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("MAIN MENU", True, (182, 143, 64))
        MENU_RECT = MENU_TEXT.get_rect(center=(WIDTH // 2, HEIGHT // 4))

        PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"),
                             pos=(WIDTH // 2, HEIGHT // 2 - 50),
                             text_input="PLAY", font=get_font(75), base_color=(215, 252, 212), hovering_color=WHITE)
        OPTIONS_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"),
                                pos=(WIDTH // 2, HEIGHT // 2 + 50),
                                text_input="OPTIONS", font=get_font(75), base_color=(215, 252, 212), hovering_color=WHITE)
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"),
                             pos=(WIDTH // 2, HEIGHT // 2 + 150),
                             text_input="QUIT", font=get_font(75), base_color=(215, 252, 212), hovering_color=WHITE)

        background.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(background)

        SCREEN.blit(background, (0, 0))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    start_game()
                    # play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

def check_game_status():
    global game_started
    if game_started:
        main()

# if __name__ == "__main__":
main_menu()


# def play():
#     check_game_status()
#
#     # Ha a főmenüből visszatérünk, akkor indítjuk el a játékot
#     play()