from Visualisation import *

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
                run_game()
            elif btn_exit_rect.collidepoint(mouse_coordinates[0], mouse_coordinates[1]):
                terminate_window()

        # redraw game state
        pygame.display.update()
        FPS_CLOCK.tick(FPS)


def run_game():
    global mouse_coordinates
    # draw labyrinth (???) ->
    DISPLAY_SURFACE.fill(BG_COLOR)
    draw_labyrinth()
    btn_menu_rect = draw_menu_btn()

    # main loop
    while True:
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
                main()
            if btn_menu_rect.collidepoint(mouse_coordinates[0], mouse_coordinates[1]) and mouse_clicked:
                main()
            if event.type == QUIT:
                terminate_window()

            # movement
            elif event.type == KEYUP:
                if event.key == K_UP or event.key == K_w:
                    PLAYER.change_position(-1, 0)
                elif event.key == K_DOWN or event.key == K_s:
                    PLAYER.change_position(1, 0)
                elif event.key == K_LEFT or event.key == K_a:
                    PLAYER.change_position(0, -1)
                elif event.key == K_RIGHT or event.key == K_d:
                    PLAYER.change_position(0, 1)

        # todo: if position of player has changed, redraw his origin and forward position
        pygame.display.update()
        FPS_CLOCK.tick(FPS)


def main():
    show_menu()
    while True:
        run_game()


if __name__ == '__main__':
    main()
