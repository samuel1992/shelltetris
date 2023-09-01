import curses
from random import randint
from typing import List, Optional

from board import Board
from point import Point
from shape import Shape

shapes = [
    (
        Point(0, 4, '#'),
        Point(1, 4, '#'),
        Point(2, 4, '#'),
        Point(3, 4, '#')
    ),
    (
        Point(0, 4, '#'),
        Point(1, 4, '#'),
        Point(0, 5, '#'),
        Point(1, 5, '#')
    ),
    (
        Point(0, 4, '#'),
        Point(1, 4, '#'),
        Point(1, 5, '#'),
        Point(2, 5, '#')
    ),
    (
        Point(0, 4, '#'),
        Point(1, 3, '#'),
        Point(1, 4, '#'),
        Point(1, 5, '#')
    ),
    (
        Point(0, 5, '#'),
        Point(1, 5, '#'),
        Point(1, 4, '#'),
        Point(2, 4, '#')
    ),
    (
        Point(0, 5, '#'),
        Point(1, 5, '#'),
        Point(1, 4, '#'),
        Point(2, 4, '#')
    )
]

def get_new_shape():
    return Shape(shapes[randint(0, len(shapes) - 1)])

def main(stdscr):
    board = Board()

    curses.curs_set(0)
    stdscr.nodelay(1)
    stdscr.timeout(500)  # Set the delay for getch to 500 milliseconds
    stdscr.clear()

    shape = get_new_shape()

    while True:
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
            board.update(shape)
            shape = get_new_shape()

        stdscr.refresh()


if __name__ == '__main__':
    curses.wrapper(main)
