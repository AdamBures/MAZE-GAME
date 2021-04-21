class Labyrinth:

    def __init__(self, labyrinth: list[list[str]]):
        self.labyrinth = labyrinth


    def __getitem__(self, item: int):
        """
        Make instance of this class to be subscriptable.
        :param item: Position in list
        :return: Value of object in "item" position
        """
        return self.labyrinth[item]
