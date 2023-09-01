from typing import Tuple

from point import Point


class Shape:
    base_width = 4
    base_height = 4

    def __init__(self, points: Tuple[Point]):
        self.points = points

    def move_one_line(self):
        for point in self.points:
            point.line += 1

    def move_right(self):
        for point in self.points:
            point.column += 1

    def move_left(self):
        for point in self.points:
            point.column -= 1

    def __eq__(self, other) -> bool:
        for point in self.points:
            if point not in other.points:
                return False

        return True
