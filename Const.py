import pygame

from Labyrinth import Labyrinth
from Player import Player

pygame.init()

# [1, 2] and [1, 6] wall
MAP1 = [['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
        ['#', 'S', '_', '_', '_', '_', '_', '_', '_', 'X'],
        ['#', '_', '#', '_', '#', '_', '#', '_', '#', '#'],
        ['#', '_', '#', '_', '#', '_', '#', '_', '_', '#'],
        ['#', '_', '_', '_', '_', '_', '_', '#', '_', '#'],
        ['#', '_', '#', '#', '#', '_', '#', '#', '_', '#'],
        ['#', '_', '_', '#', '_', '#', '_', '_', '_', '#'],
        ['#', '#', '_', '_', '#', '_', '_', '#', '#', '#'],
        ['#', '_', '_', '_', '_', '_', '_', '_', '_', '#'],
        ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#']]

ROW_MOVE = [0, 0, -1, 1]
COL_MOVE = [1, -1, 0, 0]
MAZE_NUMBER = 5

WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
DISPLAY_SURFACE = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

MENU_LABYRINTH = Labyrinth(10, 15)
LABYRINTH = Labyrinth(10, 10)
PLAYER = Player(LABYRINTH)

WHITE = (255, 255, 255)
BG_COLOR = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BROWN = (255, 97, 3)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
GREY = (128, 128, 128)

TITLE_FONT = pygame.font.Font('freesansbold.ttf', 60)
BTN_FONT = pygame.font.Font('freesansbold.ttf', 40)
BTN_FONT2 = pygame.font.Font('freesansbold.ttf', 30)
SCORE_FONT = pygame.font.Font('freesansbold.ttf', 25)
END_FONT = pygame.font.Font('freesansbold.ttf', 35)
TIME_FONT = pygame.font.Font('freesansbold.ttf', 30)

NUMBER = 0
FPS = 30
FPS_CLOCK = pygame.time.Clock()

# here you can change the type of tile for floor/wall,..
image_end = pygame.image.load('PicturesFolder/ladder/ladder48.png')
image_floor = pygame.image.load("PicturesFolder/floors/floor.png")
image_door = pygame.image.load("PicturesFolder/doors/door.png")
image_player = pygame.image.load("PicturesFolder/players/goblins/goblin48.png")
image_player_left = pygame.transform.flip(image_player, True, False)

SECRET_IMAGE = pygame.image.load(r"PicturesFolder\secret image.jpg")


def restart() -> None:
    """
    Restart the game
    :return: None
    """
    global LABYRINTH, MENU_LABYRINTH, PLAYER
    MENU_LABYRINTH = Labyrinth(10, 15)
    LABYRINTH = Labyrinth(10, 10)
    PLAYER = Player(LABYRINTH)
