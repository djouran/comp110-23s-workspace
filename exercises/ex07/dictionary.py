"""EX07 - Dictionaries."""

__author__ = "730434721"


def invert(d: dict[str, str]) -> dict[str, str]:
    """Inverts the keys and values of a dictionary."""
    inverted_d = {}
    for key, value in d.items():
        if value in inverted_d:
            raise KeyError(f"Cannot invert dictionary with duplicate values: {value}")
        inverted_d[value] = key
    return inverted_d


def favorite_color(colors: dict[str, str]) -> str:
    """Returns the most common color in the dictionary."""
    color_counts = {}
    for color in colors.values():
        if color not in color_counts:
            color_counts[color] = 0
        color_counts[color] += 1
    max_count = max(color_counts.values())
    most_common = [color for color, count in color_counts.items() if count == max_count]
    for color in colors.values():
        if color in most_common:
            return color


def count(values: list[str]) -> dict[str, int]:
    """Counts the frequency of each item in the input list."""
    result = {}
    for item in values:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
    return result