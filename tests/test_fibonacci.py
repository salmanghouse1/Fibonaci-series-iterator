import fibonacci
import pytest


@pytest.mark.parametrize('test_input,expected', [
    (0, [0]),
    (1, [0, 1]),
    (2, [0, 1, 1]),
    (4, [0, 1, 1, 2, 3]),
    (10, [
        0,
        1,
        1,
        2,
        3,
        5,
        8,
        13,
        21,
        34,
        55,
        ]),
    (-1, []),
    ])
def test_known_values(test_input, expected):
    assert list(fibonacci.Fibonacci(test_input)) == expected


def test_Value_Error():
    with pytest.raises(ValueError):
        fibonacci.Fibonacci('A')
