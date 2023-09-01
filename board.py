from typing import List, Optional
from point import Point
from shape import Shape


class Board:
    width = 10
    height = 20

    def __init__(self, occupied_spaces: List[Point] = []):
        self.occupied_spaces = occupied_spaces

        self.matrix: List[List] = []
        self._build_matrix()
        self._fill_occupied_spaces()

    def _fill_occupied_spaces(self):
        assert len(self.matrix) != 0, 'Matrix must be built'

        for point in self.occupied_spaces:
            self.matrix[point.line][point.column] = point

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
            or any(p.at_next_line in self.occupied_spaces for p in shape.points)
        )

    def collision_left(self, shape: Shape) -> bool:
        return (
            any(p.column == 0 for p in shape.points)
            or any((p.line, p.column - 1) in self.occupied_spaces for p in shape.points)
        )

    def collision_right(self, shape: Shape) -> bool:
        return (
            any(p.column + 1 == self.width for p in shape.points)
            or any((p.line, p.column + 1) in self.occupied_spaces for p in shape.points)
        )

    def draw(self, shape: Optional[Shape] = None):
        self._fill_occupied_spaces()
        string = ''
        for line in self.matrix:
            for point in line:
                if shape is not None:
                    point = next(filter(lambda p: p == point, shape.points), point)

                string += point.object

            string += '\n'

        return string



