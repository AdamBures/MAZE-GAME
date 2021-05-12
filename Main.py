import pygame
from pygame.locals import *

import Const
import Visualisation
from Const import TITLE_FONT, WHITE, WINDOW_WIDTH, WINDOW_HEIGHT, BTN_FONT, BG_COLOR, FPS, FPS_CLOCK, MAZE_NUMBER

pygame.init()

mouse_coordinates = (0, 0)


def terminate_window():
    pygame.quit()
    exit()


def show_menu():
    global mouse_coordinates
    Visualisation.draw_labyrinth(Const.MENU_LABYRINTH, 0)
    # Title
    title_surface = TITLE_FONT.render('A(maze)ing Game!', True, WHITE)
    title_rect = title_surface.get_rect()
    title_rect.center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 3)

    # Button
    btn_start = BTN_FONT.render("Start", True, WHITE)
    btn_exit = BTN_FONT.render("Exit", True, WHITE)

    btn_start_rect = btn_start.get_rect()
    btn_exit_rect = btn_exit.get_rect()

    btn_start_rect.center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT * 1.15 / 2)
    btn_exit_rect.center = (WINDOW_WIDTH / 2, 2 * WINDOW_HEIGHT * 1.15 / 3)

    # draw window
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
                Const.restart()
            elif btn_exit_rect.collidepoint(mouse_coordinates[0], mouse_coordinates[1]):
                terminate_window()

        # redraw game state
        pygame.display.update()
        FPS_CLOCK.tick(FPS)


def run_game():
    global mouse_coordinates
    Const.DISPLAY_SURFACE.fill(BG_COLOR)
    Visualisation.draw_labyrinth(Const.LABYRINTH)
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

def end_screen():
    #Rendering the finished text, continue text and secret image 
    end_surface = END_FONT.render("YOU FINISHED 5 LEVELS", True, WHITE)
    continue_surface = END_FONT.render("Press enter to continue...", True, WHITE)
    secret_image = pygame.image.load(r"PicturesFolder\secret image.jpg")
    
    #Creates rectangles of all 3 mentioned surfaces
    end_rect = end_surface.get_rect()
    secret_rect = secret_image.get_rect()
    continue_rect = continue_surface.get_rect()
    
    #Centering these 3 rectangles
    end_rect.center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 5)
    secret_rect.center =  (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)
    continue_rect.center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 1.25)

    #Gameloop
    flag = True
    while flag:
        #Filling and bliting the variables
        Const.DISPLAY_SURFACE.fill(BLACK)
        Const.DISPLAY_SURFACE.blit(end_surface, end_rect)
        Const.DISPLAY_SURFACE.blit(secret_image, secret_rect)
        Const.DISPLAY_SURFACE.blit(continue_surface, continue_rect)
        #Event loop
        for event in pygame.event.get():
            #Terminating the window
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                terminate_window()
            #Showing the menu
            if event.type == KEYUP and event.key == K_RETURN:
                show_menu()
                break
        #Updating the display and setting FPS
        pygame.display.update()
        FPS_CLOCK.tick(FPS)

def main():
    while True:
        show_menu()
        maze_counter = 0
        while True:
            run_game()
            maze_counter += 1
            Const.restart()

            if maze_counter == MAZE_NUMBER:
                break


if __name__ == '__main__':
    main()
