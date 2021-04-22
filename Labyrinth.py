from typing import List


class Labyrinth:

    def __init__(self, labyrinth: List[List[str]]):
        """
        :param labyrinth: list of chars
        :type labyrinth: list
        :param index: index at which to pick a list and then pick char from *labyrinth*
        :type index: string
        """
        self.labyrinth = labyrinth
        self.labyrinth_width = len(labyrinth[0])
        self.labyrinth_height = len(labyrinth)

    def __getitem__(self, item: int):
        """
        Make instance of this class subscriptable.
        :param item: Position in list
        :return: Value of object in "item" position
        """
        return self.labyrinth[item]

    def __len__(self):
        return len(self.labyrinth)
