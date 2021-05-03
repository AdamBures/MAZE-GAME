from random import random, choice, seed
from time import time
from typing import List, Tuple, Optional

seed(time())

WALL = '#'

# types of wall ->
RIGHT_BOTTOM_WALL = 'wall_right_bottom'
LEFT_BOTTOM_WALL = 'wall_left_bottom'
RIGHT_UPPER_WALL = 'wall_right_up'
LEFT_UPPER_WALL = 'wall_left_up'
MIDDLE_BOTTOM_WALL = 'wall_middle_bottom'
MIDDLE_UPPER_WALL = 'wall_middle_up'
MIDDLE_RIGHT_WALL = 'wall_middle_right'
MIDDLE_LEFT_WALL = 'wall_middle_left'

FLOOR = '_'
EXIT = 'X'
START = 'S'
EMPTY = 'U'

ROW_MOVE = [0, 1, -1, 0]
COL_MOVE = [-1, 0, 0, 1]
ALL_ROW_MOVE = ROW_MOVE[:] + [-1, 1, 1, -1]
ALL_COL_MOVE = COL_MOVE[:] + [-1, 1, -1, 1]

# alike linux permissions, see https://www.pluralsight.com/blog/it-ops/linux-file-permissions
# their position cannot be changed!
# from left to right, they mean -> previous column, lower row, upper row, next column
ADJACENT_WALLS = (4, 2, 1, 8)


class Labyrinth:

    def __init__(self, labyrinth_height: int, labyrinth_width: int,
                 labyrinth: Optional[List[List[str]]] = None):
        """
        Initialize maze. If parameter labyrinth is not set, labyrinth
        :param labyrinth_height: Height of a labyrinth
        :param labyrinth_width: Width of a labyrinth
        :param labyrinth: 2d list determining maze
        """
        self.labyrinth_width = labyrinth_width
        self.labyrinth_height = labyrinth_height

        if labyrinth is not None:
            self.labyrinth = labyrinth
        else:
            self.__generate_maze()

        self.adjacent_walls = self.__linux_cells_types()
        self.visible_cells = self.__init_visible_cells()

    def __getitem__(self, item: int):
        """
        Makes instance of this class subscriptable.
        :param item: Position in list
        :return: Value of object in "item" position
        """
        return self.labyrinth[item]

    def __len__(self):
        return len(self.labyrinth)


    def __init_visible_cells(self) -> List[List[int]]:
        visible_cells = []
        for _ in range(0, self.labyrinth_width):
            row = []
            for _ in range(0, self.labyrinth_height):
                row.append(0)
            visible_cells.append(row)

        return visible_cells

    def __init_maze(self) -> None:
        """
        Initializes "empty" labyrinth. Mark all cells EMPTY
        :return: None
        """
        self.labyrinth = []
        for rows in range(0, self.labyrinth_height):
            row = []
            for cols in range(0, self.labyrinth_width):
                row.append(EMPTY)

            self.labyrinth.append(row)

    def __generate_random_position(self) -> Tuple[int, int]:
        """
        Generates random position in labyrinth which is not on the edge
        :return: Tuple indicating position in 2d list
        """
        row = int(random() * self.labyrinth_height)
        col = int(random() * self.labyrinth_width)

        if row == 0:
            row += 1
        elif row == self.labyrinth_height - 1:
            row -= 1
        if col == 0:
            col += 1
        elif col == self.labyrinth_width - 1:
            col -= 1

        return row, col

    def __count_adjacent_cells(self, wall: List[int]) -> int:
        """
        Counts adjacent cells around the wall provided
        :param wall: Tuple indicating position of a wall in the labyrinth
        :return: How many FLOOR are adjacent to the wall
        """
        cells = 0

        if self.labyrinth[wall[0] - 1][wall[1]] == FLOOR:
            cells += 1
        if self.labyrinth[wall[0] + 1][wall[1]] == FLOOR:
            cells += 1
        if self.labyrinth[wall[0]][wall[1] - 1] == FLOOR:
            cells += 1
        if self.labyrinth[wall[0]][wall[1] + 1] == FLOOR:
            cells += 1

        return cells

    def __mark_next_walls(self, walls: List[List[int]], current_wall: List[int]) -> None:
        """
        Marks adjacent walls and it puts them to walls list
        :param walls: List containing all walls
        :param current_wall: Current wall we are processing
        :return: None
        """
        for i in range(0, 4):
            next_field = current_wall[0] + ROW_MOVE[i], current_wall[1] + COL_MOVE[i]
            if self.labyrinth[next_field[0]][next_field[1]] != FLOOR:
                self.labyrinth[current_wall[0] + ROW_MOVE[i]][current_wall[1] + COL_MOVE[i]] = WALL
                if next_field not in walls:
                    walls.append([current_wall[0] + ROW_MOVE[i], current_wall[1] + COL_MOVE[i]])

    def __update_walls_list(self, walls: List[List[int]], wall: List[int]) -> None:
        """
        If there are no more than 2 adjacent FLOORs then update walls in labyrinth and walls list.
        Then remove current wall from walls
        :param walls: List containing all walls
        :param wall: Current wall which is being processed
        :return: None
        """
        # count adjacent FLOOR and if there are no more than 2
        if self.__count_adjacent_cells(wall) < 2:
            # set the current wall to a passage -> FLOOR
            self.labyrinth[wall[0]][wall[1]] = FLOOR

            # repeat the starting process -> find adjacent walls, mark them in labyrinth and add them to
            # the list of walls
            self.__mark_next_walls(walls, wall)

        walls.remove(wall)

    def __mark_remaining_walls(self) -> None:
        """
        Mark remaining EMPTY to be WALL
        :return: None
        """
        for row in range(0, self.labyrinth_height):
            for col in range(0, self.labyrinth_width):
                if self.labyrinth[row][col] == EMPTY:
                    self.labyrinth[row][col] = WALL

    def __set_exit(self) -> None:
        """
        Choose random possible exit from a maze
        :return: None
        """
        possible_exit = []

        for col in range(0, self.labyrinth_width):
            if self.labyrinth[1][col] == FLOOR:
                possible_exit.append([0, col])
            if self.labyrinth[self.labyrinth_height - 1][col] == FLOOR:
                possible_exit.append([self.labyrinth_height - 1, col])

        for row in range(0, self.labyrinth_height):
            if self.labyrinth[row][1] == FLOOR:
                possible_exit.append([row, 0])
            if self.labyrinth[row][self.labyrinth_width - 1] == FLOOR:
                possible_exit.append([row][self.labyrinth_width - 1])

        exit_row, exit_col = choice(possible_exit)
        self.labyrinth[exit_row][exit_col] = EXIT

    def __generate_maze(self) -> None:
        """
        Generates random labyrinth with Randomized Prim's Algorithm
        :return: None
        """
        # if the labyrinth includes some data, mostly walls or cells, then initialize it again to be empty labyrinth
        self.__init_maze()

        # select random first cell in labyrinth and mark it as 'free way'
        starting_row, starting_col = self.__generate_random_position()
        self.labyrinth[starting_row][starting_col] = FLOOR

        # for each adjacent cell in possible move, mark it as a wall and put their position into a list
        walls = []
        for i in range(0, 4):
            self.labyrinth[starting_row + ROW_MOVE[i]][starting_col + COL_MOVE[i]] = WALL
            walls.append([starting_row + ROW_MOVE[i], starting_col + COL_MOVE[i]])

        # while there are some walls which were not proceeded
        while walls:
            # choose random wall from the list
            rand_wall = choice(walls)

            # check whether the wall is or is not in the first or the last column
            if rand_wall[1] != 0 and rand_wall[1] != self.labyrinth_width - 1:

                # check whether the sequence is 'EMPTY WALL FLOOR'
                if self.labyrinth[rand_wall[0]][rand_wall[1] - 1] == EMPTY and \
                        self.labyrinth[rand_wall[0]][rand_wall[1] + 1] == FLOOR:

                    # update walls and skip other steps
                    self.__update_walls_list(walls, rand_wall)
                    continue

                # check whether the sequence is 'FLOOR WALL EMPTY'
                elif self.labyrinth[rand_wall[0]][rand_wall[1] - 1] == FLOOR and \
                        self.labyrinth[rand_wall[0]][rand_wall[1] + 1] == EMPTY:

                    # update walls and skip other steps
                    self.__update_walls_list(walls, rand_wall)
                    continue

            # check whether the wall is or is not in the first or the last row
            if rand_wall[0] != 0 and rand_wall[0] != self.labyrinth_height - 1:

                # check whether the sequence is     EMPTY
                #                                   WALL
                #                                   FLOOR
                if self.labyrinth[rand_wall[0] - 1][rand_wall[1]] == EMPTY and \
                        self.labyrinth[rand_wall[0] + 1][rand_wall[1]] == FLOOR:

                    # update walls and skip other steps
                    self.__update_walls_list(walls, rand_wall)
                    continue

                # check whether the sequence is     FLOOR
                #                                   WALL
                #                                   EMPTY
                elif self.labyrinth[rand_wall[0] - 1][rand_wall[1]] == FLOOR and \
                        self.labyrinth[rand_wall[0] + 1][rand_wall[1]] == EMPTY:

                    # update walls and skip other steps
                    self.__update_walls_list(walls, rand_wall)
                    continue

            # if the wall is on the edge <-> no branch captures it, delete the wall anyway
            walls.remove(rand_wall)

        self.__mark_remaining_walls()
        self.__set_exit()


    def __linux_cells_types(self) -> List[List[str]]:
        """
        Each cell contains specific number characterizing how many and where are its adjacent walls
        :return: List containing all adjacent walls which can be accessed in the same way as cell in labyrinth
        """
        labyrinth_walls = []
        for row in range(0, self.labyrinth_height):
            row_walls = []
            for col in range(0, self.labyrinth_width):
                adjacency = 0
                for i in range(0, 4):
                    if 0 <= row + ROW_MOVE[i] < self.labyrinth_height and 0 <= col + COL_MOVE[i] < self.labyrinth_width:
                        if self.labyrinth[row + ROW_MOVE[i]][col + COL_MOVE[i]] == WALL:
                            adjacency += ADJACENT_WALLS[i]

                row_walls.append(Labyrinth.__cells_types(adjacency))
            labyrinth_walls.append(row_walls)


        return labyrinth_walls


        return types
