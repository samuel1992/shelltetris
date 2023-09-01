from main import Point


def test_compare_two_points():
    point_a = Point(0, 1)
    point_b = Point(0, 1)

    assert point_a == point_b


def test_compare_point_with_typle():
    point = Point(0, 1)

    assert point == (0, 1)
