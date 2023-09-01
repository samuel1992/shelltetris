from main import Board, Shape, Point


def test_draw_an_empty_board():
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


def test_replace_a_point_in_matrix():
    expected = (
        '. # . . . . . . . . \n'
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
    point = Point(0, 1, '#')

    board.replace_point(point)

    assert board.draw() == expected


def test_draw_matrix_with_occupied_spaces():
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
    points = [
        Point(16, 0, '#'),
        Point(17, 0, '#'),
        Point(18, 0, '#'),
        Point(19, 0, '#')
    ]
    board = Board(occupied_spaces=points)

    assert board.draw() == expected


def test_draw_a_board_with_a_shape():
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


def test_shape_colision_with_left_border():
    board = Board()
    shape = Shape([
        Point(0, 0, '#'),
        Point(1, 0, '#'),
        Point(2, 0, '#'),
        Point(3, 0, '#')
    ])

    assert board.collision_left(shape)

def test_shape_colision_with_right_border():
    board = Board()
    shape = Shape([
        Point(0, board.width - 1, '#'),
        Point(1, board.width - 1, '#'),
        Point(2, board.width - 1, '#'),
        Point(3, board.width - 1, '#')
    ])

    assert board.collision_right(shape)

def test_shape_colision_with_bottom_border():
    board = Board()
    shape = Shape([
        Point(16, 0, '#'),
        Point(17, 0, '#'),
        Point(18, 0, '#'),
        Point(19, 0, '#')
    ])

    assert board.collision_down(shape)
