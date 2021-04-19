from Const import *

import pygame
from pygame.locals import *
pygame.init()


def terminate_window():
    pygame.quit()
    exit()


def show_menu():

    # Title
    title_font = pygame.font.Font('freesansbold.ttf', 80)
    btn_font = pygame.font.Font('freesansbold.ttf', 40)
    title_surface = title_font.render('Maze Game!', True, WHITE)
    title_rect = title_surface.get_rect()
    title_rect.center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 3)

    # Button
    btn_start = btn_font.render("Start!", True, WHITE)
    btn_exit = btn_font.render("Exit!", True, WHITE)

    btn_start_rect = btn_start.get_rect()
    btn_exit_rect = btn_exit.get_rect()

    btn_start_rect.center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)
    btn_exit_rect.center = (WINDOW_WIDTH / 2, 2 * WINDOW_HEIGHT / 3)

    # draw window
    DISPLAY_SURFACE.fill(BG_COLOR)
    DISPLAY_SURFACE.blit(title_surface, title_rect)
    DISPLAY_SURFACE.blit(btn_start, btn_start_rect)
    DISPLAY_SURFACE.blit(btn_exit, btn_exit_rect)

    mouse_coordinates = None

    while True:
        mouse_clicked = False

        # check for user input
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                terminate_window()
            elif event.type == MOUSEMOTION:
                mouse_coordinates = event.pos
            elif event.type == MOUSEBUTTONUP:
                mouse_coordinates = event.pos
                mouse_clicked = True

        if mouse_clicked:
            if btn_start_rect.collidepoint(mouse_coordinates[0], mouse_coordinates[1]):
                break
            elif btn_exit_rect.collidepoint(mouse_coordinates[0], mouse_coordinates[1]):
                terminate_window()


        # redraw game state
        pygame.display.update()



def run_game():
    while True:
        pass


def main():
    show_menu()
    while True:

        run_game()



if __name__ == '__main__':
    main()
