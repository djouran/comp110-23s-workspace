"""Tests util.py."""

__author__ = "730434721"


from exercises.ex05.utils import only_evens, sub, concat


def test_edge_evens() -> None:
    """Tests edge cases for `only_evens`."""
    assert only_evens([1, 2, 4, 5]) == [2, 4]


def test_edge_concat() -> None:
    """Tests edge cases for `concat`."""
    assert concat([1, 2], [1, 3]) == [1, 2, 1, 3]


def test_edge_sub() -> None:
    """Tests edge cases for `sub`."""
    assert sub([1, 2, 3, 4], 1, 5) == [2, 3]


def test_use_sub1() -> None:
    """Tests cases using `sub`."""
    assert sub([1, 2, 3, 5, 7], 1, 3) == [2, 3]


def test_use_sub2() -> None:
    """Tests cases using `sub`."""
    assert sub([1, 2, 3], 0, 2) == [1, 2]


def test_use_concat1() -> None:
    """Tests cases using `concat`."""
    assert concat([1, 2, 4, 5], [1, 3]) == [1, 2, 4, 5, 1, 3]


def test_use_concat2() -> None:
    """Tests cases using `concat`."""
    assert concat([6, 9], [4, 2, 0]) == [6, 9, 4, 2, 0]


def test_use_evens1() -> None:
    """Tests cases using `only_evens`."""
    assert only_evens([1, 2, 4, 5, 6, 9, 11]) == [2, 4, 6]


def test_use_evens2() -> None:
    """Tests cases using `only_evens`."""
    assert only_evens([100, 200, 222]) == [100, 200, 222]