from Labyrinth import *
import pygame

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

WHITE = (255, 255, 255)
BG_COLOR = (0, 0, 0)