from typing import List

class Labyrinth:
    """
    :param labyrinth: list of chars
    :type labyrinth: list
    :param index: index at which to pick a list and then pick char from *labyrinth*
    :type index: string
    """
    def __init__(self, labyrinth: List[List[str]]):
        self.labyrinth = labyrinth


    def __getitem__(self, item: int):
        """
        Make instance of this class to be subscriptable.
        :param item: Position in list
        :return: Value of object in "item" position
        """
        return self.labyrinth[item]
