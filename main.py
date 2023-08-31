import os
import time
from typing import List, Tuple


class Point:
    def __init__(self, line: int, column: int, object: str = '.'):
        self.line = line
        self.column = column
        self.object = object + ' '

    @property
    def next_line(self):
        return self.line + 1

    def __eq__(self, other):
        if isinstance(other, tuple):
            return (self.line, self.column) == other

        if isinstance(other, self.__class__):
            return (self.line, self.column) == (other.line, other.column)

        return False


class Piece:
    base_width = 4
    base_height = 4

    def __init__(self, a: Point, b: Point, c: Point, d: Point):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.round = 0

    def move_one_line(self):
        self.a.line += 1
        self.b.line += 1
        self.c.line += 1
        self.d.line += 1

    def colide(self, height: int):
        return (
            self.a.next_line == height
            or self.b.next_line == height
            or self.c.next_line == height
            or self.d.next_line == height
        )

    def move_right(self) -> 'Piece':
        self.a.column += 1
        self.b.column += 1
        self.c.column += 1
        self.d.column += 1
        return self

    def move_left(self):
        self.a.column -= 1
        self.b.column -= 1
        self.c.column -= 1
        self.d.column -= 1
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

    def draw(self):
        string = ''
        for line in self.matrix:
            for point in line:
                string += point.object
            string += '\n'

        return string


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def draw_board(piece: Piece):
    print(f'PIECE ROUND {piece.round}')
    print()

#     for line in range(HEIGHT):
#         for column in range(WIDTH):
#             if (
#                     piece.a == (column, line) or
#                     piece.b == (column, line) or
#                     piece.c == (column, line) or
#                     piece.d == (column, line)
#             ):
#                 print('#', end=' ')
#             else:
#         print()


if __name__ == '__main__':
    pieces = [
        Piece(
            Point(7, 0),
            Point(7, 1),
            Point(7, 2),
            Point(7, 3)
        ),
        Piece(
            Point(7, 0),
            Point(7, 1),
            Point(8, 0),
            Point(8, 1)
        ),
        Piece(
            Point(7, 0),
            Point(7, 1),
            Point(8, 1),
            Point(8, 2)
        ),
        Piece(
            Point(7, 0),
            Point(6, 1),
            Point(7, 1),
            Point(8, 1)
        )
    ]
    piece_count = 0
    while True:
        piece = pieces[piece_count]
        clear_screen()
        draw_board(piece)

        if piece.round != 0 and not piece.colide(HEIGHT):
            piece.move_one_line()

        if piece.colide(HEIGHT):
            piece_count += 1

            if piece_count == len(pieces):
                piece_count = 0

        piece.round += 1
        time.sleep(0.2)
