import curses
from random import randint
from typing import List, Optional

from board import Board
from point import Point
from shapes import Shape, IShape, JShape, LShape, OShape, SShape, TShape, ZShape

shapes = [IShape, JShape, LShape, OShape, SShape, TShape, ZShape]


def get_new_shape():
    return shapes[randint(0, len(shapes) - 1)]()


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

        if key == ord('w'):
            #TODO: need to handle rotation colision proper
            if not shape.rotated and board.collision_right(shape):
                continue

            shape.rotate()

        # Display the Tetris game board and shape
        stdscr.addstr(0, 0, ' === SHELL TETRIS ===')
        stdscr.addstr(2, 0, board.draw(shape))

        if board.collision_down(shape):
            board.update(shape)
            shape = get_new_shape()
            stdscr.refresh()
            continue

        shape.move_one_line()
        stdscr.refresh()


if __name__ == '__main__':
    curses.wrapper(main)
