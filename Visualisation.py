from pygame.locals import *
import time
from Const import *

# blk stands for block
# the height of each of the blocks is supposed to be the same as their width
# on the left side of the screen is left space for future additions of buttons and other features

# starting coordinates for columns and rows ( for the first block )
X_BLK_START = 80
Y_BLK_START = 0

# number of blocks
BLK_NUM = len(LABYRINTH[0])

# block size
BLK_SIZE = WINDOW_HEIGHT // BLK_NUM

# end of the block, depending on their row and column position
# this one is for the end of the first block
X_BLK_END = X_BLK_START + BLK_SIZE
Y_BLK_END = Y_BLK_START + BLK_SIZE


def draw_labyrinth():
    # blocks are being drawn in rows, not columns
    for i in range(len(LABYRINTH[0])):
        for j in range(len(LABYRINTH[0])):
            rect = pygame.Rect(X_BLK_START + (BLK_SIZE * j), Y_BLK_START + (BLK_SIZE * i), BLK_SIZE - 2, BLK_SIZE - 2)
            # wall
            if MAP1[i][j] == '#':
                pygame.draw.rect(DISPLAY_SURFACE, BROWN, rect)
                # - 2 -> used to make space between blocks
                # first line goes from top left corner to the middle of right side of the block
                # second line goes from the middle of the right side to the bottom left corner
                # third line goes from top right corner to the middle of the left side
                # fourth line goes from the middle of the left side to the bottom right corner
                # X_COORDS is X coordinate of left side of the particular block
                # Y_COORDS is Y coordinate of top side of the particular block
                X_COORDS = X_BLK_START + (BLK_SIZE * j)
                Y_COORDS = Y_BLK_START + (BLK_SIZE * i)

                pygame.draw.line(DISPLAY_SURFACE, BLACK, (X_COORDS, Y_COORDS),
                                 (X_COORDS + BLK_SIZE - 2, Y_COORDS + (BLK_SIZE // 2) - 2), 1)
                pygame.draw.line(DISPLAY_SURFACE, BLACK, (X_COORDS + BLK_SIZE - 2, Y_COORDS + (BLK_SIZE // 2) - 2),
                                 (X_COORDS, Y_COORDS + BLK_SIZE - 2), 1)
                pygame.draw.line(DISPLAY_SURFACE, BLACK, (X_COORDS + BLK_SIZE - 2, Y_COORDS),
                                 (X_COORDS, Y_COORDS + (BLK_SIZE // 2) - 2), 1)
                pygame.draw.line(DISPLAY_SURFACE, BLACK, (X_COORDS, Y_COORDS + (BLK_SIZE // 2)),
                                 (X_COORDS + BLK_SIZE - 2, Y_COORDS + BLK_SIZE - 2), 1)
            # road
            if MAP1[i][j] == '_':
                pygame.draw.rect(DISPLAY_SURFACE, GREEN, rect)
            # start (player spawn) and the end
            if MAP1[i][j] == 'X' or MAP1[i][j] == 'S':
                pygame.draw.rect(DISPLAY_SURFACE, BLUE, rect)
                if MAP1[i][j] == 'X':
                    pygame.draw.circle(DISPLAY_SURFACE, WHITE, ((X_BLK_START + (BLK_SIZE * j) + (BLK_SIZE - 2) // 2),
                                                                Y_BLK_START + (BLK_SIZE * i) + ((BLK_SIZE - 2) // 2)),
                                       (BLK_SIZE - 2) // 2)
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
    Draw score and number.
    :return None
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
    Show current player position while in game
    the first rect creation is to overwrite the previous c_position_rect
    :return: None
    """
    pygame.draw.rect(DISPLAY_SURFACE, BLACK, (0, 0, 80, 80))
    position = PLAYER.get_position()
    position = str(position)
    c_position = BTN_FONT2.render(position, True, WHITE)
    c_position_rect = c_position.get_rect()
    c_position_rect.center = (40, 40)
    DISPLAY_SURFACE.blit(c_position, c_position_rect)
    return c_position_rect
