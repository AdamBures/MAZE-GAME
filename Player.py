from typing import Union, List, Dict, Tuple, Optional

import Labyrinth

ROW_MOVE = [0, 0, -1, 1]
COL_MOVE = [1, -1, 0, 0]
ALL_ROW_MOVE = ROW_MOVE[:] + [-1, 1, 1, -1]
ALL_COL_MOVE = COL_MOVE[:] + [-1, 1, -1, 1]


class Player:

    def __init__(self, labyrinth: Labyrinth, row_position: Optional[int] = None, col_position: Optional[int] = None):
        self.__labyrinth = labyrinth
        self.__row_position = row_position
        self.__col_position = col_position
        self.__previous_row_position = None
        self.__previous_col_position = None
        self.__visible = []

        if row_position is None or col_position is None:
            self.__get_random_player_position()

        self.__add_visible()

    @staticmethod
    def find_player_position(labyrinth: Labyrinth) -> Tuple[int, int]:
        """
        Finds player position in labyrinth
        :param labyrinth: 2d string list
        :return: Tuple containing row and col position
        """
        for row in range(0, len(labyrinth)):
            for col in range(0, len(labyrinth[0])):
                if labyrinth[row][col] == Labyrinth.START:
                    return row, col

        # todo: handle exception, if there is no field holding 'S' then something is wrong
        return -1, -1

    @staticmethod
    def find_exit_position(labyrinth: Labyrinth) -> Tuple[int, int]:
        """
        Finds exit position in labyrinth
        :param labyrinth: 2d string list
        :return: Tuple containing row and col position
        """
        for row in range(0, len(labyrinth)):
            for col in range(0, len(labyrinth[0])):
                if labyrinth[row][col] == Labyrinth.EXIT:
                    return row, col

        # todo: handle exception, if there is no field holding 'X' then something is wrong
        return -1, -1

    def __add_visible(self) -> None:
        """
        Add position of the cells, player is currently seeing, to visible list
        :return: None
        """
        for i in range(0, 7):
            visible_row = self.__row_position + ALL_ROW_MOVE[i]
            visible_col = self.__col_position + ALL_COL_MOVE[i]
            if [visible_row, visible_col] not in self.__visible:
                self.__visible.append([visible_row, visible_col])

    def get_visible(self) -> List[List[int]]:
        """
        Returns fields that player has been to and one field to each direction around them
        :return: List containing position of visible fields
        """
        return self.__visible

    def __get_random_player_position(self) -> Tuple[int, int]:
        """
        Gets random player position which will be at least length of labyrinth
        :return: Tuple of position in the labyrinth
        """
        no_player_position = True
        while no_player_position:
            for row in range(0, self.__labyrinth.labyrinth_height):
                for col in range(0, self.__labyrinth.labyrinth_width):
                    if self.__labyrinth[row][col] == Labyrinth.FLOOR and no_player_position:
                        self.__row_position = row
                        self.__col_position = col

                        if len(self.__path_to_end()) > self.__labyrinth.labyrinth_width and \
                                len(self.__path_to_end()) > self.__labyrinth.labyrinth_height:
                            self.__labyrinth[row][col] = Labyrinth.START
                            no_player_position = False

        return self.__row_position, self.__col_position

    def get_current_position(self) -> Tuple[int, int]:
        """
        Gets encapsulated position of a player
        :return: Current position of a player
        """
        return self.__row_position, self.__col_position

    def get_previous_position(self) -> Tuple[int, int]:
        """
        Gets encapsulated previous position of a player
        :return: Previous position of a player
        """
        return self.__previous_row_position, self.__previous_col_position

    def change_position(self, add_row: int = 0, add_col: int = 0) -> None:
        """
        Change position of the player
        :param add_row: Row which will be added to its origin position
        :param add_col: Col which will be added to its origin position
        :return: None
        """
        self.__previous_row_position = self.__row_position
        self.__previous_col_position = self.__col_position

        next_row = self.__row_position + add_row
        next_col = self.__col_position + add_col
        if len(self.__labyrinth[0]) > next_row >= 0:
            if len(self.__labyrinth) > next_col >= 0:
                if self.__labyrinth[next_row][next_col] == '_' or self.__labyrinth[next_row][next_col] == 'S':
                    # change player's position
                    self.__row_position += add_row
                    self.__col_position += add_col

                    self.__add_visible()

            # todo: what happens when player steps on exit (field 'X')?

    def __convert_position(self, row_position: int = None, col_position: int = None) -> int:
        """
        Convert 2d position to 1d position
        :param row_position: Row position in 2d list
        :param col_position: Col position in 2d list
        :return: Converted position
        """
        if row_position is None or col_position is None:
            return self.__row_position * len(self.__labyrinth[0]) + self.__col_position

        return row_position * len(self.__labyrinth[0]) + col_position

    def __predecessors_list(self) -> Dict[int, Union[int, List[int]]]:
        """
        Set all position in 2d list in predecessors dictionary to -1, then to certain key add tuple of its predecessor
        until end of maze is found
        :return: Predecessor dictionary. Value -1 means it has no predecessor, it was not needed to be found or it is
                 a wall so it cannot have a predecessor
        """
        predecessors = {}
        states = {}
        for row in range(0, len(self.__labyrinth)):
            for col in range(0, len(self.__labyrinth[0])):
                predecessors[self.__convert_position(row, col)] = -1
                states[self.__convert_position(row, col)] = False

        states[self.__convert_position()] = True

        row_queue = [self.__row_position]
        col_queue = [self.__col_position]

        while row_queue:
            current_row = row_queue.pop(0)
            current_col = col_queue.pop(0)

            for i in range(0, 4):
                next_row = current_row + ROW_MOVE[i]
                next_col = current_col + COL_MOVE[i]

                if self.__labyrinth[next_row][next_col] == "#":
                    continue

                if states[next_row * len(self.__labyrinth[0]) + next_col]:
                    continue

                predecessors[self.__convert_position(next_row, next_col)] = [current_row, current_col]

                if self.__labyrinth[next_row][next_col] == "X":
                    break

                states[self.__convert_position(next_row, next_col)] = True

                row_queue.append(next_row)
                col_queue.append(next_col)

        return predecessors

    def __path_to_end(self) -> List[List[int]]:
        """
        Find the path that leads from player position to end of a given maze
        :return: List containing all position player must go to exit the maze
        """
        predecessors = self.__predecessors_list()
        path = []

        row_exit, col_exit = Player.find_exit_position(self.__labyrinth)
        dest = self.__convert_position(row_exit, col_exit)

        v = dest

        path.append([v // 10, v % 10])

        while predecessors[v] != -1:
            path.append(predecessors[v])
            v = self.__convert_position(predecessors[v][0], predecessors[v][1])

        return path[::-1]

    def next_position(self) -> List[int]:
        """
        Find a next position of a player
        :return: Nex position of a player
        """
        return self.__path_to_end()[1]
