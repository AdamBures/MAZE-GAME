import pygame

import Const
from Const import WHITE, WINDOW_HEIGHT, image_end, image_door, image_floor, image_player, BTN_FONT2, SCORE_FONT, \
    NUMBER, BLACK
from Labyrinth import WALL, FLOOR, START, EXIT

# blk stands for block
# the height of each of the blocks is supposed to be the same as their width
# on the left side of the screen is left space for future additions of buttons and other features

# starting coordinates for columns and rows ( for the first block )
X_BLK_START = 80
Y_BLK_START = 0

# number of blocks
BLK_NUM = len(Const.LABYRINTH[0])

# block size
BLK_SIZE = Const.WINDOW_HEIGHT / BLK_NUM

# resizing images (tiles)
RESIZE_IMG = BLK_SIZE / 16
image_end = pygame.transform.rotozoom(image_end, 0, RESIZE_IMG)

# end of the block, depending on their row and column position
# this one is for the end of the first block
X_BLK_END = X_BLK_START + BLK_SIZE
Y_BLK_END = Y_BLK_START + BLK_SIZE


def draw_labyrinth() -> None:
    """
    Graphic design for the labyrinth walls, cells, start and exit block
    draws the whole labyrinth...
    :return: None
    """
    # blocks are being drawn in rows, not columns
    for i in range(len(Const.LABYRINTH)):
        for j in range(len(Const.LABYRINTH[0])):
            rect = pygame.Rect(X_BLK_START + (BLK_SIZE * j), Y_BLK_START + (BLK_SIZE * i), BLK_SIZE, BLK_SIZE)

            # X_COORDS is X coordinate of left side of the particular block
            # Y_COORDS is Y coordinate of top side of the particular block
            X_COORDS = X_BLK_START + (BLK_SIZE * j)
            Y_COORDS = Y_BLK_START + (BLK_SIZE * i)

            if Const.LABYRINTH[i][j] == WALL:
                image_wall = pygame.image.load(
                    "PicturesFolder/walls/walls48/" + str(Const.LABYRINTH.adjacent_walls[i][j] + ".png"))
                Const.DISPLAY_SURFACE.blit(image_wall, (X_COORDS, Y_COORDS))
            if Const.LABYRINTH[i][j] == FLOOR:
                Const.DISPLAY_SURFACE.blit(image_floor, (X_COORDS, Y_COORDS))
            if Const.LABYRINTH[i][j] == START:
                Const.DISPLAY_SURFACE.blit(image_door, (X_COORDS, Y_COORDS))
            if Const.LABYRINTH[i][j] == EXIT:
                Const.DISPLAY_SURFACE.blit(image_end, (X_COORDS, Y_COORDS))
            pygame.display.update()


def draw_menu_btn() -> pygame.Rect:
    """
    Draw menu button to surface and return rectangle (check for collide points in game loop)
    :return: Rectangle object
    """
    btn_menu = BTN_FONT2.render("Menu", True, WHITE)
    btn_menu_rect = btn_menu.get_rect()
    btn_menu_rect.center = (40, WINDOW_HEIGHT / 2)
    Const.DISPLAY_SURFACE.blit(btn_menu, btn_menu_rect)

    return btn_menu_rect


def draw_score() -> None:
    """
    Draw score and number
    :return: None
    """
    score_menu = SCORE_FONT.render("Score", True, WHITE)
    score_rect = score_menu.get_rect()
    score_rect.center = (40, (WINDOW_HEIGHT / 2) + 50)
    Const.DISPLAY_SURFACE.blit(score_menu, score_rect)
    number_menu = SCORE_FONT.render(f"{NUMBER}", True, WHITE)
    number_rect = number_menu.get_rect()
    number_rect.center = (40, (WINDOW_HEIGHT / 2) + 80)
    Const.DISPLAY_SURFACE.blit(number_menu, number_rect)


def current_position_vis() -> None:
    """
    Show current player position while in the game
    the first rect creation is to overwrite the previous c_position_rect
    :return: None
    """
    pygame.draw.rect(Const.DISPLAY_SURFACE, BLACK, (0, 0, 80, 80))
    position = Const.PLAYER.get_current_position()
    position = str(position)
    c_position = BTN_FONT2.render(position, True, WHITE)
    c_position_rect = c_position.get_rect()
    c_position_rect.center = (40, 40)
    Const.DISPLAY_SURFACE.blit(c_position, c_position_rect)
    return c_position_rect


def player_pos_change() -> None:
    """
    Pos_y and pos_x holds the position of block on which player stands
    real_pos_x and real_pos_y transforms the player position to real coordinates for drawing the image of player
    draw_labyrinth deletes the old images of player in labyrinth from previous position
    :return: Image of player on screen
    """
    pos_y, pos_x = Const.PLAYER.get_current_position()
    prev_pos_y, prev_pos_x = Const.PLAYER.get_previous_position()
    if prev_pos_y is not None:
        real_prev_pos_x = X_BLK_START + (BLK_SIZE * prev_pos_x)
        real_prev_pos_y = Y_BLK_START + (BLK_SIZE * prev_pos_y)
        if Const.LABYRINTH[prev_pos_y][prev_pos_x] == FLOOR:
            Const.DISPLAY_SURFACE.blit(image_floor, (real_prev_pos_x, real_prev_pos_y))
        if Const.LABYRINTH[prev_pos_y][prev_pos_x] == START:
            Const.DISPLAY_SURFACE.blit(image_door, (real_prev_pos_x, real_prev_pos_y))
        if Const.LABYRINTH[prev_pos_y][prev_pos_x] == EXIT:
            Const.DISPLAY_SURFACE.blit(image_end, (real_prev_pos_x, real_prev_pos_y))

    real_pos_x = X_BLK_START + (BLK_SIZE * pos_x)
    real_pos_y = Y_BLK_START + (BLK_SIZE * pos_y)

    Const.DISPLAY_SURFACE.blit(image_player, (real_pos_x, real_pos_y))
