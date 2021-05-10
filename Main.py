import pygame
from pygame.locals import *

import Const
import Visualisation
from Const import TITLE_FONT, WHITE, WINDOW_WIDTH, WINDOW_HEIGHT, BTN_FONT, BG_COLOR, FPS, FPS_CLOCK

pygame.init()

mouse_coordinates = (0, 0)


def terminate_window():
    pygame.quit()
    exit()


def show_menu():
    global mouse_coordinates
    # Title
    title_surface = TITLE_FONT.render('Maze Game!', True, WHITE)
    title_rect = title_surface.get_rect()
    title_rect.center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 3)

    # Button
    btn_start = BTN_FONT.render("Start!", True, WHITE)
    btn_exit = BTN_FONT.render("Exit!", True, WHITE)

    btn_start_rect = btn_start.get_rect()
    btn_exit_rect = btn_exit.get_rect()

    btn_start_rect.center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)
    btn_exit_rect.center = (WINDOW_WIDTH / 2, 2 * WINDOW_HEIGHT / 3)

    # draw window
    Const.DISPLAY_SURFACE.fill(BG_COLOR)
    Const.DISPLAY_SURFACE.blit(title_surface, title_rect)
    Const.DISPLAY_SURFACE.blit(btn_start, btn_start_rect)
    Const.DISPLAY_SURFACE.blit(btn_exit, btn_exit_rect)

    mouse_coordinates = None

    flag = True
    while flag:
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
                flag = False
            elif btn_exit_rect.collidepoint(mouse_coordinates[0], mouse_coordinates[1]):
                terminate_window()

        # redraw game state
        pygame.display.update()
        FPS_CLOCK.tick(FPS)


def run_game():
    global mouse_coordinates
    Const.DISPLAY_SURFACE.fill(BG_COLOR)
    Visualisation.draw_labyrinth()
    Visualisation.player_pos_change()
    Visualisation.current_position_vis()
    btn_menu_rect = Visualisation.draw_menu_btn()
    # main loop
    flag = True
    while flag:
        Visualisation.draw_score()
        mouse_clicked = False

        for event in pygame.event.get():

            # change mouse coordinates
            if event.type == MOUSEMOTION:
                mouse_coordinates = event.pos
            elif event.type == MOUSEBUTTONUP:
                mouse_coordinates = event.pos
                mouse_clicked = True

            # return to menu or quit
            # todo: maybe we will need to store progress somewhere
            if event.type == KEYUP and event.key == K_ESCAPE:
                flag = False
            if btn_menu_rect.collidepoint(mouse_coordinates[0], mouse_coordinates[1]) and mouse_clicked:
                flag = False
            if event.type == QUIT:
                terminate_window()
            if Const.PLAYER.get_current_position() == Const.LABYRINTH.get_exit_position() and \
                    event.type == KEYUP and event.key == K_RETURN:
                flag = False


            # movement
            elif event.type == KEYUP:
                if event.key == K_UP or event.key == K_w:
                    Const.PLAYER.change_position(-1, 0)
                    Visualisation.current_position_vis()
                elif event.key == K_DOWN or event.key == K_s:
                    Const.PLAYER.change_position(1, 0)
                    Visualisation.current_position_vis()
                elif event.key == K_LEFT or event.key == K_a:
                    Const.PLAYER.change_position(0, -1)
                    Visualisation.current_position_vis()
                elif event.key == K_RIGHT or event.key == K_d:
                    Const.PLAYER.change_position(0, 1)
                    Visualisation.current_position_vis()

                Visualisation.player_pos_change()

        pygame.display.update()
        FPS_CLOCK.tick(FPS)


def main():
    while True:
        show_menu()
        run_game()
        Const.restart()


if __name__ == '__main__':
    main()
