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

WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
DISPLAY_SURFACE = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

LABYRINTH = Labyrinth(MAP1)
START_ROW, START_COL = Player.find_player_position(LABYRINTH)
PLAYER = Player(LABYRINTH, START_ROW, START_COL)

WHITE = (255, 255, 255)
BG_COLOR = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BROWN = (255, 97, 3)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

TITLE_FONT = pygame.font.Font('freesansbold.ttf', 80)
BTN_FONT = pygame.font.Font('freesansbold.ttf', 40)
BTN_FONT2 = pygame.font.Font('freesansbold.ttf', 30)
SCORE_FONT = pygame.font.Font('freesansbold.ttf', 25)

FPS = 30
FPS_CLOCK = pygame.time.Clock()
