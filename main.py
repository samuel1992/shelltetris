import os
import time
from typing import List, Optional, Tuple


class Point:
    def __init__(self, line: int, column: int, object: str = '.'):
        self.line = line
        self.column = column
        self.object = object + ' '

    @property
    def next_line(self):
        return self.line + 1

    @property
    def at_next_line(self):
        return self.__class__(self.next_line, self.column, self.object)

    def __eq__(self, other):
        if isinstance(other, tuple):
            return (self.line, self.column) == other

        if isinstance(other, self.__class__):
            return (self.line, self.column) == (other.line, other.column)

        return False


class Shape:
    base_width = 4
    base_height = 4

    def __init__(self, points: List[Point]):
        self.points = points
        self.round = 0

    def move_one_line(self):
        for point in self.points:
            point.line += 1

    def move_right(self) -> 'Shape':
        for point in self.points:
            point.column += 1
        return self

    def move_left(self) -> 'Shape':
        for point in self.points:
            point.column -= 1
        return self

    def draw(self):
        pass


class Board:
    def __init__(self, ocupied_spaces: List[Point] = []):
        self.width = 10
        self.height = 20
        self.ocupied_spaces = ocupied_spaces

        self.matrix: List[List] = []
        self._build_matrix()
        self._fill_ocupied_spaces()

    def _fill_ocupied_spaces(self):
        assert len(self.matrix) != 0, 'Matrix must be built'

        for point in self.ocupied_spaces:
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

    def colision(self, shape: Shape) -> bool:
        return (
            any(p.next_line == self.height for p in shape.points)
            or any(p.at_next_line in self.ocupied_spaces for p in shape.points)
        )

    def draw(self, shape: Optional[Shape] = None):
        self._fill_ocupied_spaces()
        string = ''
        for line in self.matrix:
            for point in line:
                if shape is not None and any(p == point for p in shape.points):
                    string += '# '
                else:
                    string += point.object

            string += '\n'

        return string


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


if __name__ == '__main__':
    shapes = [
        Shape([
            Point(0, 4, '#'),
            Point(1, 4, '#'),
            Point(2, 4, '#'),
            Point(3, 4, '#')
        ]),
        Shape([
            Point(0, 4, '#'),
            Point(1, 4, '#'),
            Point(0, 5, '#'),
            Point(1, 5, '#')
        ]),
        Shape([
            Point(0, 4, '#'),
            Point(1, 4, '#'),
            Point(1, 5, '#'),
            Point(2, 5, '#')
        ]),
        Shape([
            Point(0, 4, '#'),
            Point(1, 3, '#'),
            Point(1, 4, '#'),
            Point(1, 5, '#')
        ])
    ]
    board = Board()

    shape_count = 0

    while True:
        shape = shapes[shape_count]
        clear_screen()

        print(f'shape ROUND: {shape.round}')
        print()
        print(board.draw(shape))

        if not board.colision(shape):
            shape.move_one_line()
        else:
            board.ocupied_spaces.extend(shape.points)
            shape_count += 1
            if shape_count == len(shapes):
                shape_count = 0

        shape.round += 1
        time.sleep(0.5)
