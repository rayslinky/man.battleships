from enum import Enum
import operator

class InvalidOrientationError(ValueError):
    pass


class Orientation(Enum):
    VERTICAL = 'VERTICAL'
    HORIZONTAL = 'HORIZONTAL'


class Ship:

    def __init__(self):
        self.horizontal_offsets = []
        self.vertical_offsets = []

    def place(self, point, orientation):
        """ Returns a set of points corresponding to the positions the ship will occupy on the game board """
        if orientation == Orientation.HORIZONTAL:
            return set([tuple(map(operator.add, point, p)) for p in self.horizontal_offsets])
        elif orientation == Orientation.VERTICAL:
            return set([tuple(map(operator.add, point, p)) for p in self.vertical_offsets])
        else:
            raise InvalidOrientationError


class Battleship(Ship):
    """
    Looks like:
                -
    - - -  or   -
                -
    """

    def __init__(self):
        super().__init__()
        self.horizontal_offsets = [(0, 0), (1, 0), (2, 0)]
        self.vertical_offsets = [(0, 0), (0, 1), (0, 2)]


class Cruiser(Ship):
    """
    Looks like:
                 -
    - - - -  or  -
                 -
                 -
    """

    def __init__(self):
        super().__init__()
        self.horizontal_offsets = [(0, 0), (1, 0), (2, 0), (3, 0)]
        self.vertical_offsets = [(0, 0), (0, 1), (0, 2), (0, 3)]


class Destroyer(Ship):
    """
    Looks like:
    -   -      - - -
    - - -  or    -
    -   -      - - -

    """

    def __init__(self):
        super().__init__()
        self.horizontal_offsets = [(0, 0), (0, 1), (0, 2), (1, 1), (2, 1), (2, 0), (2, 2)]
        self.vertical_offsets = [(0, 0), (1, 0), (2, 0), (1, 1), (0, 2), (1, 2), (2, 2)]


class Submarine(Ship):
    """
    Looks like:

             -
    - -  or  -

    """

    def __init__(self):
        super().__init__()
        self.horizontal_offsets = [(0, 0), (0, 1)]
        self.vertical_offsets = [(0, 0), (1, 0)]


# Defines the array of ships that must be placed by a player before the game can begin
SHIP_ARRAY = [Battleship(), Battleship(), Battleship()]