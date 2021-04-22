from pygame.locals import *

from Const import *

# blk znamená blok
# vykreslenie blokov som nastavil zatiaľ tak aby mali rovnakú veľkosť a šírku
# v ľavej časti obrazovky nechávam miesto na vykreslovanie skóre, tlačítok ako hint, end, menu,...

# začiatočné súradnice ku ktorým sa ešte bude pridávať hodnota podľa toho v ktorom stĺpci a riadku sú
X_BLK_START = 80
Y_BLK_START = 0

# počet blokov
BLK_NUM = len(LABYRINTH[0])

# veľkosť bloku
BLK_SIZE = WINDOW_HEIGHT // BLK_NUM

# koniec bloku, znovu sa k tomu bude pridávať hodnota podľa toho kde sa nachádzajú v riadku a stĺpci
# tieto hodnoty sú vlastne ako keby pre prvý blok
X_BLK_END = X_BLK_START + BLK_SIZE
Y_BLK_END = Y_BLK_START + BLK_SIZE


def draw_labyrinth():
    # bloky sa vykreslujú po riadkoch, nie po stĺpcoch
    for i in range(len(LABYRINTH[0])):
        for j in range(len(LABYRINTH[0])):
            rect = pygame.Rect(X_BLK_START + (BLK_SIZE * j), Y_BLK_START + (BLK_SIZE * i), BLK_SIZE - 2, BLK_SIZE - 2)
            # stena
            if MAP1[i][j] == '#':
                pygame.draw.rect(DISPLAY_SURFACE, BROWN, rect)
                # - 2 vo výpočte zabezpečuje medzery medzi blokmi, aby boli ľahšie rozoznateľné
                # prvá čiara je z horného ľavého rohu do stredu pravej strany
                # druhá je zo stredu pravej strany do ľavého doľného rohu
                # tretia z horného pravého rohu do stredu ľavej strany
                # štvrtá zo stredu ľavej strany do pravého doľného rohu
                # X_COORDS je X-ová súradnica lavej steny daného bloku
                # Y_coords je Y-ová súradnica hornej steny daného bloku
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
            # priechod
            if MAP1[i][j] == '_':
                pygame.draw.rect(DISPLAY_SURFACE, GREEN, rect)
            # Začiatok a koniec
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


# Game loop
def main():
    while True:
        draw_labyrinth()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            pygame.display.update()


if __name__ == '__main__':
    main()
