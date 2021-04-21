# MAZE-GAME

### `Const`:
Includes several constant that are used in other files.

### `Labyrinth`:
There is defined `class Labyrinth`
```python 
def __init__(self, labyrinth: list[list[str]]):
    # Declares and initializes attr `laybirinth` to the value of the same 
    # name parameter `labyrinth`
    ...

def __getitem__(self, item: int):
    # Makes instances of this class subscriptable
    ...
```

### `Main`:
Core of the whole game
```python
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
from typing import Union
import Labyrinth

def __init__(self, labyrinth: Labyrinth, row_position: int, col_position: int):
    # Initializes player position in the labyrinth
    ...

def __convert_position(self, row_position: int = None, col_position: int = None) -> int:
    # Converts 2d position to 1d position
    ...

def __predecessors_list(self, labyrinth: list[list[str]]) -> dict[int, Union[int, list[int]]]:
    # BSF algorithm that search for the shortest path to end
    # I tried to reduce time complexity by changing 2d position in list to 1d position represented by one number
    # Returns dictionary containing it
    ...

def __path_to_end(self, labyrinth: list[list[str]], dest: int) -> list[list[int]]:
    # Finds all 2d positions player must visit in order to exit the maze
    ...

def next_position(self, labyrinth: list[list[str]], dest: int) -> list[int]:
    # Returns next position player must visit in order to exit the maze
    ...
```
### `Visualisation`:
Displays the labyrinth to user
```python
def draw_labyrinth():
    # Draw background (labyrinth) to window surface
    ...
```