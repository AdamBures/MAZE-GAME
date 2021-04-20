from typing import Union


class Player:

    def __init__(self, row_position: int, col_position: int):
        self.row_position = row_position
        self.col_position = col_position


    def __predecessors_list(self, labyrinth: list[list[str]]) -> dict[int, Union[int, list[int]]]:
        """
        Set all position in 2d list in predecessors dictionary to -1, then to certain key add tuple of its predecessor
        until end of maze is found
        :param labyrinth: 2d list representing maze
        :return: Predecessor dictionary. Value -1 means it has no predecessor, it was not needed to be found or it is
                 a wall so it cannot have a predecessor
        """
        predecessors = {}
        states = {}
        for row in range(0, len(labyrinth)):
            for col in range(0, len(labyrinth[0])):
                predecessors[row * len(labyrinth[0]) + col] = -1
                states[row * len(labyrinth[0]) + col] = False


        states[self.row_position * len(labyrinth[0]) + self.col_position] = True

        row_move = [0, 0, -1, 1]
        col_move = [1, -1, 0, 0]

        row_queue = [self.row_position]
        col_queue = [self.col_position]

        while row_queue:
            current_row = row_queue.pop(0)
            current_col = col_queue.pop(0)

            for i in range(0, 4):
                next_row = current_row + row_move[i]
                next_col = current_col + col_move[i]

                if labyrinth[next_row][next_col] == "#":
                    continue

                if states[next_row * len(labyrinth[0]) + next_col]:
                    continue

                predecessors[next_row * len(labyrinth[0]) + next_col] = [current_row, current_col]

                if labyrinth[next_row][next_col] == "X":
                    break

                states[next_row * len(labyrinth[0]) + next_col] = True

                row_queue.append(next_row)
                col_queue.append(next_col)

        return predecessors

    def __path_to_end(self, labyrinth: list[list[str]], dest: int) -> list[list[int]]:
        """
        Find the path that leads from player position to end of a given maze
        :param labyrinth: 2d list representing maze
        :param dest: Integer position of end of a given maze
        :return: List containing all position player must go to exit the maze
        """
        predecessors = self.__predecessors_list(labyrinth)
        path = []
        v = dest

        path.append([v // 10, v % 10])

        while predecessors[v] != -1:
            path.append(predecessors[v])
            v = predecessors[v][0] * len(labyrinth[0]) + predecessors[v][1]

        return path[::-1]

    def next_position(self, labyrinth: list[list[str]], dest: int) -> list[int]:
        """
        Find a next position of a player
        :param labyrinth: 2d list representing maze
        :param dest: Integer position of end of a given maze
        :return: Nex position of a player
        """
        return self.__path_to_end(labyrinth, dest)[1]

