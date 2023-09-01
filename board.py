from typing import List, Optional
from point import Point
from shape import Shape


class Board:
    width = 10
    height = 20

    def __init__(self):
        self.matrix: List[List] = []
        self._build_matrix()

    def _build_matrix(self):
        for x in range(self.height):
            line = []
            for y in range(self.width):
                point = Point(x, y)
                line.append(point)

            self.matrix.append(line)

    def replace_point(self, point: Point):
        for x in range(self.height):
            for y in range(self.width):
                if self.matrix[x][y] == point:
                    self.matrix[x][y] = point

    def collision_down(self, shape: Shape) -> bool:
        return (
            any(p.next_line == self.height for p in shape.points)
            or any(self.matrix[p.next_line][p.column].object == '#' for p in shape.points)
        )

    def collision_left(self, shape: Shape) -> bool:
        return (
            any(p.column == 0 for p in shape.points)
            or any(self.matrix[p.line][p.column - 1].object == '#' for p in shape.points)
        )

    def collision_right(self, shape: Shape) -> bool:
        return (
            any(p.column + 1 == self.width for p in shape.points)
            or any(self.matrix[p.line][p.column + 1].object == '#' for p in shape.points)
        )

    def update(self, shape: Shape):
        for point in shape.points:
            self.matrix[point.line][point.column] = point

    def draw(self, shape: Optional[Shape] = None):
        string = ''
        for line in self.matrix:
            for point in line:
                if shape is not None:
                    point = next(filter(lambda p: p == point, shape.points), point)

                string += point.object + ' '

            string += '\n'

        return string



