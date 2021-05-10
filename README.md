# MAZE-GAME

### `Const`:
Includes several constants that are used in other files.
```python
import pygame
from Labyrinth import Labyrinth
from Player import Player


def restart() -> None:
    # Restarts the game
    ...
```

### `Labyrinth`:
There is defined `class Labyrinth`
```python
from random import random, choice, seed
from time import time
from typing import List, Tuple, Optional


def __init__(self, labyrinth_height: int, labyrinth_width: int, 
             labyrinth: Optional[List[List[str]]]):
    # Initializes labyrinth. If parameter `labyrinth` is not set, 
    # labyrinth will be automatically generate by `generate_maze` method
    ...

def __getitem__(self, item: int):
    # Makes instances of this class subscriptable
    ...
    
def __len__(self):
    # Returns len of the attr `labyrinth`
    ...

def __init_visible_cells(self) -> List[List[int]]:
    # Initialize list for cells that are visible to a player
    ...

def __init_maze(self) -> None:
    # Initializes "empty" labyrinth. Mark all cells in that labyrinth as EMPTY cells
    ...

def __generate_random_position(self) -> Tuple[int, int]:
    # Generates random position in labyrinth which is not on the edge of it
    ...

def __count_adjacent_cells(self, wall: List[int]) -> int:
    # Counts how many field around `wall` parameter are CELLs (cell in a 
    # labyrinth where player can step)
    ...

def __mark_next_walls(self, walls: List[List[int]], current_wall: List[int]) -> None:
    # Find all adjacent cells which are not CELLs and mark them as WALLs
    ...

def __update_walls_list(self, walls: List[List[int]], wall: List[int]) -> None:
    # If there are no more than 2 adjacent CELLs (see `__count_adjacent_cells` method) 
    # then update walls in labyrinth and walls list.
    ...
    
def __mark_remaining_walls(self) -> None:
    # When generating a labyrinth is at the end, all cells that are still EMPTY
    # will be marked as WALLs
    ...

def __set_exit(self) -> None:
    # Chooses random possible exit from a maze
    ...

def __generate_maze(self) -> None:
    # Generates random labyrinth with Randomized Prim's Algorithm
    ...

def __linux_cells_types(self) -> List[List[str]]:
    # Creates a list containing specific number characterizing how many adjacent walls
    # are around, and how many of them
    # Uses something like linux privileges for counting
    ...


@staticmethod
def __cells_types(key: int) -> str:
    # Returns type of wall in the labyrinth
    ...

def get_exit_position(self) -> Tuple[int, int]:
    # Returns exit position of the labyrinth
    ...
```

### `Main`:
Core of the whole game
```python
import pygame
import Const
import Visualisation
from pygame.locals import *
from Const import TITLE_FONT, WHITE, WINDOW_WIDTH, WINDOW_HEIGHT, BTN_FONT, BG_COLOR, \
    FPS, FPS_CLOCK, MAZE_NUMBER


def terminate_window():
    # Closes the game
    ...

def show_menu():
    # Displays the menu
    ...

def run_game():
    # Runs the game
    ...

def main():
    # Runs the program
    ...
```
### `Player`:
There is defined `class Player`
```python
from typing import Union, List, Dict, Tuple, Optional
import Labyrinth


def __init__(self, labyrinth: Labyrinth, row_position: int, col_position: int):
    # Initializes player position in the labyrinth
    ...

@staticmethod
def find_player_position(labyrinth: Labyrinth) -> Tuple[int, int]:
    # Finds player's current position
    ...

@staticmethod
def find_exit_position(labyrinth: Labyrinth) -> Tuple[int, int]:
    # Finds exit position in labyrinth
    ...

def __update_visible(self) -> List[List[int]]:
    # Add position of the cells, player is currently seeing, to visible list
    ...

def get_visible(self) -> List[List[int]]:
    # Returns fields that player has been to and one field to each direction around them
    ...

def __get_random_player_position(self) -> Tuple[int, int]:
    # Gets random player's position which will be at least length of a labyrinth 
    # far away from exit
    ...

def get_current_position(self) -> Tuple[int, int]:
    # Returns current position of a player
    ...

def get_previous_position(self) -> Tuple[int, int]:
    # Returns previous position of a player
    ...

def change_position(self) -> Tuple[int, int]:
    # Changes position of the player
    ...

def __convert_position(self, row_position: int = None, col_position: int = None) -> int:
    # Converts 2d position to 1d position
    ...

def __predecessors_list(self, labyrinth: List[List[str]]) -> Dict[int, Union[int, List[int]]]:
    # BSF algorithm that search for the shortest path to end
    # I tried to reduce time complexity by changing 2d position in List to 1d position 
    # represented by one number
    # Returns dictionary containing it
    ...

def __path_to_end(self, labyrinth: List[List[str]], dest: int) -> List[List[int]]:
    # Finds all 2d positions player must visit in order to exit the maze
    ...

def next_position(self, labyrinth: List[List[str]], dest: int) -> List[int]:
    # Returns next position player must visit in order to exit the maze
    ...
```
### `Visualisation`:
Displays the labyrinth to user
```python
import pygame
import Const
from Const import WHITE, WINDOW_HEIGHT, image_end, image_door, image_floor, \
    image_player, BTN_FONT2, SCORE_FONT, NUMBER, BLACK, GREY, image_player_left
from Labyrinth import WALL, FLOOR, START, EXIT


def draw_labyrinth() -> None:
    # Draws background (labyrinth) to window surface
    ...

def draw_menu_btn() -> pygame.Rect:
    # Draws menu btn to surface
    # Returns btn rectangle
    ...

def draw_score() -> None:
    # Displays score to surface
    ...

def current_position_vis() -> None:
    # Shows current player's position
    ...

def player_pos_change() -> None:
    # While I am writing this update to Readme
    # I have no idea what this function does
    ...
```