from Const import *
from Labyrinth import WALL, FLOOR, START, EXIT

# blk stands for block
# the height of each of the blocks is supposed to be the same as their width
# on the left side of the screen is left space for future additions of buttons and other features

# starting coordinates for columns and rows ( for the first block )
X_BLK_START = 80
Y_BLK_START = 0

# number of blocks
BLK_NUM = len(LABYRINTH[0])

# block size
BLK_SIZE = WINDOW_HEIGHT / BLK_NUM

# resizing images (tiles)
RESIZE_IMG = BLK_SIZE / 16
im_Wall = pygame.transform.rotozoom(im_Wall, 0, RESIZE_IMG)
im_Floor = pygame.transform.rotozoom(im_Floor, 0, RESIZE_IMG)
im_end = pygame.transform.rotozoom(im_end, 0, RESIZE_IMG)
im_start = pygame.transform.rotozoom(im_start, 0, RESIZE_IMG / 2)

imp_player = pygame.transform.rotozoom(imp_player, 0, RESIZE_IMG)

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
    for i in range(len(LABYRINTH[0])):
        for j in range(len(LABYRINTH[0])):
            rect = pygame.Rect(X_BLK_START + (BLK_SIZE * j), Y_BLK_START + (BLK_SIZE * i), BLK_SIZE, BLK_SIZE)

            # X_COORDS is X coordinate of left side of the particular block
            # Y_COORDS is Y coordinate of top side of the particular block
            X_COORDS = X_BLK_START + (BLK_SIZE * j)
            Y_COORDS = Y_BLK_START + (BLK_SIZE * i)

            # wall
            if LABYRINTH[i][j] == WALL:
                DISPLAY_SURFACE.blit(im_Wall, (X_COORDS, Y_COORDS))
            # road
            if LABYRINTH[i][j] == FLOOR:
                DISPLAY_SURFACE.blit(im_Floor, (X_COORDS, Y_COORDS))
            # start (player spawn) and the end
            if LABYRINTH[i][j] == START:
                DISPLAY_SURFACE.blit(im_start, (X_COORDS, Y_COORDS))
            if LABYRINTH[i][j] == EXIT:
                DISPLAY_SURFACE.blit(im_end, (X_COORDS, Y_COORDS))
            pygame.display.update()


def draw_menu_btn() -> pygame.Rect:
    """
    Draw menu button to surface and return rectangle (check for collide points in game loop)
    :return: Rectangle object
    """
    btn_menu = BTN_FONT2.render("Menu", True, WHITE)
    btn_menu_rect = btn_menu.get_rect()
    btn_menu_rect.center = (40, WINDOW_HEIGHT / 2)
    DISPLAY_SURFACE.blit(btn_menu, btn_menu_rect)

    return btn_menu_rect


def draw_score() -> None:
    """
    Draw score and number
    :return: None
    """
    score_menu = SCORE_FONT.render("Score", True, WHITE)
    score_rect = score_menu.get_rect()
    score_rect.center = (40, (WINDOW_HEIGHT / 2) + 50)
    DISPLAY_SURFACE.blit(score_menu, score_rect)
    number_menu = SCORE_FONT.render(f"{NUMBER}", True, WHITE)
    number_rect = number_menu.get_rect()
    number_rect.center = (40, (WINDOW_HEIGHT / 2) + 80)
    DISPLAY_SURFACE.blit(number_menu, number_rect)


def current_position_vis() -> None:
    """
    Show current player position while in the game
    the first rect creation is to overwrite the previous c_position_rect
    :return: None
    """
    pygame.draw.rect(DISPLAY_SURFACE, BLACK, (0, 0, 80, 80))
    position = PLAYER.get_current_position()
    position = str(position)
    c_position = BTN_FONT2.render(position, True, WHITE)
    c_position_rect = c_position.get_rect()
    c_position_rect.center = (40, 40)
    DISPLAY_SURFACE.blit(c_position, c_position_rect)
    return c_position_rect


def player_pos_change() -> None:
    """
    Pos_y and pos_x holds the position of block on which player stands
    real_pos_x and real_pos_y transforms the player position to real coordinates for drawing the image of player
    draw_labyrinth deletes the old images of player in labyrinth from previous position
    :return: Image of player on screen
    """
    pos_y, pos_x = PLAYER.get_current_position()
    real_pos_x = X_BLK_START + (BLK_SIZE * pos_x)
    real_pos_y = Y_BLK_START + (BLK_SIZE * pos_y)
    draw_labyrinth()
    DISPLAY_SURFACE.blit(imp_player, (real_pos_x, real_pos_y))
