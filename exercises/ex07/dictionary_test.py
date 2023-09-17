"""EX07 - THE TEST."""

__author__ = "730434721"


from exercises.ex07.dictionary import invert, favorite_color, count


def test_edge_invert() -> None:
    """Tests edge cases for invert()."""
    assert invert({}) == {}


def test_edge_favorite_color() -> None:
    """Tests edge cases for favorite_color()."""
    assert favorite_color({"Marc": "blue", "Julie": "red"}) == "blue"


def test_edge_count() -> None:
    """Tests edge cases for count()."""
    assert count([]) == {}


def test_case_invert1() -> None:
    """Tests cases using invert()."""
    assert invert({'a': 'z', 'b': 'y', 'c': 'x'}) == {'z': 'a', 'y': 'b', 'x': 'c'}


def test_case_invert2() -> None:
    """Tests cases using invert()."""
    assert invert({'a': 'z', 'b': 'y', 'c': 'x', 'd': 'j'}) == {'z': 'a', 'y': 'b', 'x': 'c', 'j': 'd'}


def test_case_favorite_color1() -> None:
    """Tests cases using favorite_color()."""
    assert favorite_color({"Marc": "blue", "Julie": "red", "Mark": "red"}) == "red"


def test_case_favorite_color2() -> None:
    """Tests cases using favorite_color()."""
    assert favorite_color({"Marc": "blue", "Julie": "red", "Mark": "red", "Daniel": "purple"}) == "red"


def test_case_count1() -> None:
    """Tests cases using count()."""
    assert count([1, 1, 3, 3]) == {'1': 2, '3': 2}


def test_case_count2() -> None:
    """Tests cases using count()."""
    assert count([1, 1, 1, 1]) == {'1': 4}