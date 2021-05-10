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

WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
DISPLAY_SURFACE = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

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

TITLE_FONT = pygame.font.Font('freesansbold.ttf', 80)
BTN_FONT = pygame.font.Font('freesansbold.ttf', 40)
BTN_FONT2 = pygame.font.Font('freesansbold.ttf', 30)
SCORE_FONT = pygame.font.Font('freesansbold.ttf', 25)

NUMBER = 0
FPS = 30
FPS_CLOCK = pygame.time.Clock()

# here you can change the type of tile for floor/wall,..
image_end = pygame.image.load('PicturesFolder/floor_ladder.png')
image_floor = pygame.image.load("PicturesFolder/floors/floor.png")
image_door = pygame.image.load("PicturesFolder/doors/door.png")
image_player = pygame.image.load("PicturesFolder/players/goblins/goblin48.png")

# todo: this picture cannot be used due to its small size -> need 48x48 pixels for sprite now
WALK_RIGHT = [pygame.image.load('PicturesFolder/Imp/R0.png'), pygame.image.load('PicturesFolder/Imp/R1.png'),
              pygame.image.load('PicturesFolder/Imp/R2.png'), pygame.image.load('PicturesFolder/Imp/R3.png')]
WALK_LEFT = [pygame.image.load('PicturesFolder/Imp/L0.png'), pygame.image.load('PicturesFolder/Imp/L1.png'),
             pygame.image.load('PicturesFolder/Imp/L2.png'), pygame.image.load('PicturesFolder/Imp/L3.png')]
