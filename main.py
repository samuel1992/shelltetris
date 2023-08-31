import os
import time
from typing import List, Tuple, Optional


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
            self.a.next_line == height or
            self.b.next_line == height or
            self.c.next_line == height or
            self.d.next_line == height
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

    def draw(self, piece: Optional[Piece] = None):
        string = ''
        for line in self.matrix:
            for point in line:
                if (
                    piece is not None and
                    (
                        piece.a == point or
                        piece.b == point or
                        piece.c == point or
                        piece.d == point
                    )
                ):
                    string += '# '
                else:
                    string += point.object

            string += '\n'

        return string


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


if __name__ == '__main__':
    pieces = [
        Piece(
            Point(0, 4),
            Point(1, 4),
            Point(2, 4),
            Point(3, 4)
        ),
        Piece(
            Point(0, 4),
            Point(1, 4),
            Point(0, 5),
            Point(1, 5)
        ),
        Piece(
            Point(0, 4),
            Point(1, 4),
            Point(1, 5),
            Point(2, 5)
        ),
        Piece(
            Point(0, 4),
            Point(1, 3),
            Point(1, 4),
            Point(1, 5)
        )
    ]
    board = Board()

    piece_count = 0

    while True:
        piece = pieces[piece_count]
        clear_screen()

        print(f'PIECE ROUND: {piece.round}')
        print()
        print(board.draw(piece))

        if not piece.colide(board.height):
            piece.move_one_line()
        else:
            piece_count += 1
            if piece_count == len(pieces):
                piece_count = 0

        piece.round += 1
        time.sleep(0.5)
