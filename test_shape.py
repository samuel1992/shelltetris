from main import Shape, Point


def test_shape_move_one_line():
    expected_shape = Shape([
        Point(1, 0, '#'),
        Point(2, 0, '#'),
        Point(3, 0, '#'),
        Point(4, 0, '#')
    ])
    shape = Shape([
        Point(0, 0, '#'),
        Point(1, 0, '#'),
        Point(2, 0, '#'),
        Point(3, 0, '#')
    ])

    shape.move_one_line()

    assert shape == expected_shape


def test_shape_move_one_column_left():
    expected_shape = Shape([
        Point(0, 0, '#'),
        Point(1, 0, '#'),
        Point(2, 0, '#'),
        Point(3, 0, '#')
    ])
    shape = Shape([
        Point(0, 1, '#'),
        Point(1, 1, '#'),
        Point(2, 1, '#'),
        Point(3, 1, '#')
    ])

    shape.move_left()

    assert shape == expected_shape


def test_shape_move_one_column_right():
    expected_shape = Shape([
        Point(0, 1, '#'),
        Point(1, 1, '#'),
        Point(2, 1, '#'),
        Point(3, 1, '#')
    ])
    shape = Shape([
        Point(0, 0, '#'),
        Point(1, 0, '#'),
        Point(2, 0, '#'),
        Point(3, 0, '#')
    ])

    shape.move_right()

    assert shape == expected_shape
