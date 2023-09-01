from board import Board
from shapes import Shape, IShape, JShape, LShape, OShape, SShape, TShape, ZShape  
from point import Point


class TestBoard:
    def test_draw_an_empty_board(self):
        expected = (
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
            '. . . . . . . . . . \n'
            '. . . . . . . . . . \n'
        )
        board = Board()

        assert board.draw() == expected


    def test_update_board_matrix(self):
        expected = (
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
            '# . . . . . . . . . \n'
            '# . . . . . . . . . \n'
            '# . . . . . . . . . \n'
            '# . . . . . . . . . \n'
        )
        shape = Shape([
            Point(16, 0, '#'),
            Point(17, 0, '#'),
            Point(18, 0, '#'),
            Point(19, 0, '#')
        ])
        board = Board()
        board.update(shape)

        assert board.draw() == expected


    def test_draw_a_board_with_a_shape(self):
        expected = (
            '# . . . . . . . . . \n'
            '# . . . . . . . . . \n'
            '# . . . . . . . . . \n'
            '# . . . . . . . . . \n'
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
        shape = Shape([
            Point(0, 0, '#'),
            Point(1, 0, '#'),
            Point(2, 0, '#'),
            Point(3, 0, '#')
        ])

        assert board.draw(shape) == expected


    def test_shape_colision_with_left_border(self):
        board = Board()
        shape = Shape([
            Point(0, 0, '#'),
            Point(1, 0, '#'),
            Point(2, 0, '#'),
            Point(3, 0, '#')
        ])

        assert board.collision_left(shape)


    def test_shape_colision_with_right_border(self):
        board = Board()
        shape = Shape([
            Point(0, board.width - 1, '#'),
            Point(1, board.width - 1, '#'),
            Point(2, board.width - 1, '#'),
            Point(3, board.width - 1, '#')
        ])

        assert board.collision_right(shape)


    def test_shape_colision_with_bottom_border(self):
        board = Board()
        shape = Shape([
            Point(16, 0, '#'),
            Point(17, 0, '#'),
            Point(18, 0, '#'),
            Point(19, 0, '#')
        ])

        assert board.collision_down(shape)


    def test_rotate_shape_to_the_right(self):
        """
         . . . . # . . . . .
         . . . . # . . . . .
         . . . . # . . . . .
         . . . . # . . . . .
        """
        board = Board()

        shape = Shape([
            Point(0, 0, '#'),
            Point(1, 0, '#'),
            Point(2, 0, '#'),
            Point(3, 0, '#')
        ])

        """
         . . . . . . . . . .
         . # # # # . . . . .
         . . . . . . . . . .
         . . . . . . . . . .
        """
        expected_shape = Shape([
            Point(0, 0, '#'),
            Point(1, 0, '#'),
            Point(2, 0, '#'),
            Point(3, 0, '#')
        ])


class TestShapes:
    def test_Ishape(self):
        expected = (
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
        board = Board()
        shape = IShape()

        assert board.draw(shape) == expected

    def test_Jshape(self):
        expected = (
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
        board = Board()
        shape = JShape()

        assert board.draw(shape) == expected

    def test_Lshape(self):
        expected = (
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
        board = Board()
        shape = LShape()

        assert board.draw(shape) == expected

    def test_Oshape(self):
        expected = (
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

        assert board.draw(shape) == expected

    def test_Sshape(self):
        expected = (
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
            '. . . . . . . . . . \n'
        )
        board = Board()
        shape = SShape()

        assert board.draw(shape) == expected

    def test_Tshape(self):
        expected = (
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
            '. . . . . . . . . . \n'
        )
        board = Board()
        shape = TShape()

        assert board.draw(shape) == expected

    def test_Zshape(self):
        expected = (
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
            '. . . . . . . . . . \n'
        )
        board = Board()
        shape = ZShape()

        assert board.draw(shape) == expected

    def test_custom_shape(self):
        expected = (
            '. . . # . . . . . . \n'
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
            '. . . . . . . . . . \n'
        )
        board = Board()
        shape = Shape([
            Point(0, 3, '#'),
        ])

        assert board.draw(shape) == expected

    def test_rotate_Ishape_to_right(self):
        expected = (
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

        shape.rotate()

        assert board.draw(shape) == expected

        expected = (
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

        shape.rotate()

        assert board.draw(shape) == expected
