# MAZE-GAME

### `Const`:
Includes several constants that are used in other files.

### `Labyrinth`:
There is defined `class Labyrinth`
```python
from typing import List

def __init__(self, labyrinth: List[List[str]]):
    # Declares and initializes attr `labyrinth` to the value of the same 
    # name parameter `labyrinth`
    ...

def __getitem__(self, item: int):
    # Makes instances of this class subscriptable
    ...
    
def __len__(self):
    # Returns len of the attr `labyrinth`
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
from typing import Union, Tuple, Dict, List
import Labyrinth

def __init__(self, labyrinth: Labyrinth, row_position: int, col_position: int):
    # Initializes player position in the labyrinth
    ...

@staticmethod
def find_player_position(labyrinth: Labyrinth) -> Tuple[int, int]:
    # Finds player's current position
    ...

def get_position(self):
    # Returns position of a player
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
def draw_labyrinth():
    # Draw background (labyrinth) to window surface
    ...

def draw_menu_btn():
    # Draw menu btn to surface
    # Returns btn rectangle
    ...
```