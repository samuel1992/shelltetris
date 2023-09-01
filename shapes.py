from typing import Optional, Tuple

from point import Point


class Shape:
    coordinates = (
        (0, 0, '.'),
        (0, 0, '.'),
        (0, 0, '.'),
        (0, 0, '.')
    )
    rotated = False

    def __init__(self, points: Optional[Tuple[Point]] = None):
        self.points = points  or (
            Point(*self.coordinates[0]),
            Point(*self.coordinates[1]),
            Point(*self.coordinates[2]),
            Point(*self.coordinates[3])
        )

    def move_one_line(self):
        for point in self.points:
            point.line += 1

    def move_right(self):
        for point in self.points:
            point.column += 1

    def move_left(self):
        for point in self.points:
            point.column -= 1

    def rotate(self):
        """
        Each default shape implements the calculation to rotate to right
        it should be able to know how many points its needed to rotate
        in case of a successfull rotation we return 0
        in case of not having the amount necessary to rotate we return the missing points amount
        ex:
            is needed 3 empty points to rotate right, we have 2 empty points, then return 1
        """
        raise NotImplementedError

    def __eq__(self, other) -> bool:
        for point in self.points:
            if point not in other.points:
                return False

        return True


class IShape(Shape):
    """
     0 1 2 3 4 5 6 7 8 9
   0 . . . . # . . . . .
   1 . . . . # . . . . .
   2 . . . . # . . . . .
   3 . . . . # . . . . .
    """
    coordinates = (
        (0, 4, '#'),
        (1, 4, '#'),
        (2, 4, '#'),
        (3, 4, '#')
    )

    def rotate(self):
        if self.rotated:
            self.points[0].line -= 3
            self.points[0].column -= 3

            self.points[1].line -= 2
            self.points[1].column -= 2

            self.points[2].line -= 1
            self.points[2].column -= 1

            self.rotated = False

            return

        self.points[0].line += 3
        self.points[0].column += 3

        self.points[1].line += 2
        self.points[1].column += 2

        self.points[2].line += 1
        self.points[2].column += 1

        self.rotated = True


class JShape(Shape):
    """
     0 1 2 3 4 5 6 7 8 9
   0 . . . . # # . . . .
   1 . . . . # . . . . .
   2 . . . . # . . . . .
   3 . . . . . . . . . .
    """
    coordinates = (
        (0, 4, '#'),
        (0, 5, '#'),
        (1, 4, '#'),
        (2, 4, '#')
    )


class LShape(Shape):
    """
     0 1 2 3 4 5 6 7 8 9
   0 . . . . # # . . . .
   1 . . . . . # . . . .
   2 . . . . . # . . . .
   3 . . . . . . . . . .
    """
    coordinates = (
        (0, 4, '#'),
        (0, 5, '#'),
        (1, 5, '#'),
        (2, 5, '#')
    )


class OShape(Shape):
    """
     0 1 2 3 4 5 6 7 8 9
   0 . . . . # # . . . .
   1 . . . . # # . . . .
   2 . . . . . . . . . .
   3 . . . . . . . . . .
    """
    coordinates = (
        (0, 4, '#'),
        (0, 5, '#'),
        (1, 4, '#'),
        (1, 5, '#')
    )


class SShape(Shape):
    """
     0 1 2 3 4 5 6 7 8 9
   0 . . . . # # . . . .
   1 . . . # # . . . . .
   2 . . . . . . . . . .
   3 . . . . . . . . . .
    """
    coordinates = (
        (0, 4, '#'),
        (0, 5, '#'),
        (1, 3, '#'),
        (1, 4, '#')
    )


class TShape(Shape):
    """
     0 1 2 3 4 5 6 7 8 9
   0 . . . # # # . . . .
   1 . . . . # . . . . .
   2 . . . . . . . . . .
   3 . . . . . . . . . .
    """
    coordinates = (
        (0, 3, '#'),
        (0, 4, '#'),
        (0, 5, '#'),
        (1, 4, '#')
    )


class ZShape(Shape):
    """
     0 1 2 3 4 5 6 7 8 9
   0 . . . # # . . . . .
   1 . . . . # # . . . .
   2 . . . . . . . . . .
   3 . . . . . . . . . .
    """
    coordinates = (
        (0, 3, '#'),
        (0, 4, '#'),
        (1, 4, '#'),
        (1, 5, '#')
    )
