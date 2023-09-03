from board import Board
from shapes import (IShape, JShape, LShape, OShape, Shape, SShape, TShape,
                    ZShape)


class TestShapeRotation:
    """
    More as an integration test to see if the shape is going to be rotated once its draw by the board.
    """

    def test_rotate_IShape(self):
        initial_shape = (
            '. . . . # . . . . . \n'
            '. . . . # . . . . . \n'
            '. . . . # . . . . . \n'
            '. . . . # . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
        )
        rotated_shape = (
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . # # # # . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
        )
        board = Board()
        shape = IShape()

        assert board.draw(shape) == initial_shape

        shape.rotate()
        assert board.draw(shape) == rotated_shape

        shape.rotate()
        assert board.draw(shape) == initial_shape

    def test_rotate_JShape(self):
        initial_shape = (
            '. . . . # # . . . . \n'
            '. . . . # . . . . . \n'
            '. . . . # . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
        )
        rotated_shape = (
            '. . . . . . . . . . \n'
            '. . . . # # # . . . \n'
            '. . . . . . # . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
        )
        board = Board()
        shape = JShape()

        assert board.draw(shape) == initial_shape

        shape.rotate()
        assert board.draw(shape) == rotated_shape

        shape.rotate()
        assert board.draw(shape) == initial_shape

    def test_rotate_LShape(self):
        initial_shape = (
            '. . . . # # . . . . \n'
            '. . . . . # . . . . \n'
            '. . . . . # . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
        )
        rotated_shape = (
            '. . . . . . . . . . \n'
            '. . . . . . . # . . \n'
            '. . . . . # # # . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
        )

        board = Board()
        shape = LShape()

        assert board.draw(shape) == initial_shape

        shape.rotate()
        assert board.draw(shape) == rotated_shape

        shape.rotate()
        assert board.draw(shape) == initial_shape

    def test_rotate_OShape(self):
        initial_shape = (
            '. . . . # # . . . . \n'
            '. . . . # # . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
        )

        board = Board()
        shape = OShape()

        assert board.draw(shape) == initial_shape

        shape.rotate()
        assert board.draw(shape) == initial_shape

        shape.rotate()
        assert board.draw(shape) == initial_shape

    def test_rotate_SShape(self):
        initial_shape = (
            '. . . . . . . . . . \n'
            '. . . . # # . . . . \n'
            '. . . # # . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
        )
        rotated_shape = (
            '. . . # . . . . . . \n'
            '. . . # # . . . . . \n'
            '. . . . # . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
        )

        board = Board()
        shape = SShape()

        assert board.draw(shape) == initial_shape

        shape.rotate()
        assert board.draw(shape) == rotated_shape

        shape.rotate()
        assert board.draw(shape) == initial_shape

    def test_rotate_TShape(self):
        initial_shape = (
            '. . . . . . . . . . \n'
            '. . . # # # . . . . \n'
            '. . . . # . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
        )
        rotated_shape = (
            '. . . . . # . . . . \n'
            '. . . . # # . . . . \n'
            '. . . . . # . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
        )

        board = Board()
        shape = TShape()

        assert board.draw(shape) == initial_shape

        shape.rotate()
        assert board.draw(shape) == rotated_shape

        shape.rotate()
        assert board.draw(shape) == initial_shape

    def test_rotate_ZShape(self):
        initial_shape = (
            '. . . . . . . . . . \n'
            '. . . # # . . . . . \n'
            '. . . . # # . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
        )
        rotated_shape = (
            '. . . . . # . . . . \n'
            '. . . . # # . . . . \n'
            '. . . . # . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
        )

        board = Board()
        shape = ZShape()

        assert board.draw(shape) == initial_shape

        shape.rotate()
        assert board.draw(shape) == rotated_shape

        shape.rotate()
        assert board.draw(shape) == initial_shape
