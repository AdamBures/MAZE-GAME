from typing import Union, List, Dict, Tuple

import Labyrinth


class Player:

    def __init__(self, labyrinth: Labyrinth, row_position: int, col_position: int):
        self.__row_position = row_position
        self.__col_position = col_position
        self.__labyrinth = labyrinth

    @staticmethod
    def find_player_position(labyrinth: Labyrinth) -> Tuple[int, int]:
        """
        Find player position in labyrinth
        :param labyrinth: 2d string list
        :return: Tuple containing row and col position
        """
        for row in range(0, len(labyrinth)):
            for col in range(0, len(labyrinth[0])):
                if labyrinth[row][col] == 'S':
                    return row, col

        # todo: handle exception, if there is no field holding 'S' then something is wrong
        return -1, -1

    def get_position(self):
        """
        :return: Current position of a player
        """
        return self.__row_position, self.__col_position

    def change_position(self, add_row: int = 0, add_col: int = 0) -> None:
        """
        Change position of the player
        :param add_row: Row which will be added to its origin position
        :param add_col: Col which will be added to its origin position
        :return: None
        """
        next_row = self.__row_position + add_row
        next_col = self.__col_position + add_col
        if len(self.__labyrinth[0]) > next_row >= 0:
            if len(self.__labyrinth) > next_col >= 0:
                if self.__labyrinth[next_row][next_col] == '_':
                    self.__row_position += add_row
                    self.__col_position += add_col
            # todo: what happens when player steps on exit (field 'S')?

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

        row_move = [0, 0, -1, 1]
        col_move = [1, -1, 0, 0]

        row_queue = [self.__row_position]
        col_queue = [self.__col_position]

        while row_queue:
            current_row = row_queue.pop(0)
            current_col = col_queue.pop(0)

            for i in range(0, 4):
                next_row = current_row + row_move[i]
                next_col = current_col + col_move[i]

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

    def __path_to_end(self, dest: int) -> List[List[int]]:
        """
        Find the path that leads from player position to end of a given maze
        :param dest: Integer position of end of a given maze
        :return: List containing all position player must go to exit the maze
        """
        predecessors = self.__predecessors_list()
        path = []
        v = dest

        path.append([v // 10, v % 10])

        while predecessors[v] != -1:
            path.append(predecessors[v])
            v = self.__convert_position(predecessors[v][0], predecessors[v][1])

        return path[::-1]

    def next_position(self, dest: int) -> List[int]:
        """
        Find a next position of a player
        :param dest: Integer position of end of a given maze
        :return: Nex position of a player
        """
        return self.__path_to_end(dest)[1]
