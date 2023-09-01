import curses
from typing import List, Optional


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
        return self.__class__(self.next_line, self.column)

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


def main(stdscr):
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

    curses.curs_set(0)
    stdscr.nodelay(1)
    stdscr.timeout(500)  # Set the delay for getch to 500 milliseconds
    shape_count = 0
    stdscr.clear()

    while True:
        shape = shapes[shape_count]

        # Get keyboard input
        key = stdscr.getch()

        # Check for key presses and exit if 'q' is pressed
        if key == ord('q'):
            break

        if key == ord('a'):
            if not board.collision_left(shape):
                shape.move_left()

        if key == ord('d'):
            if not board.collision_right(shape):
                shape.move_right()

        if key == ord('s'):
            if not board.collision_down(shape):
                shape.move_one_line()

        # Display the Tetris game board and shape
        stdscr.addstr(0, 0, ' === SHELL TETRIS ===')
        stdscr.addstr(2, 0, board.draw(shape))

        if not board.collision_down(shape):
            shape.move_one_line()
        else:
            board.occupied_spaces.extend(shape.points)
            shape_count += 1
            if shape_count == len(shapes):
                shape_count = 0

        shape.round += 1
        stdscr.refresh()


if __name__ == '__main__':
    curses.wrapper(main)
