"""Utils - Daniel Jouran."""

author: str = "730434721"


def all(ints: list[int], target: int) -> bool:
    """Given a list of integers, makes sure if all the numbers are the same as the given integer."""
    index: int = 0
    if len(ints) == 0:
        return False
    while index < len(ints):
        if ints[index] != target:
            return False
        index += 1
    return True


def max(ints: list[int]) -> int:
    """Finds the largest integer within the list."""
    if len(ints) == 0:
        raise ValueError("max() arg is an empty List")
    index: int = 0 
    maximum: int = ints[index]
    while index < len(ints):
        if maximum < ints[index]:
            maximum = ints[index]
        index += 1
    return maximum


def is_equal(ints1: list[int], ints2: list[int]) -> bool:
    """Determines if the two lists are identical."""
    index: int = 0
    if len(ints1) != len(ints2):
        return False
    while index < len(ints1) and index < len(ints2):
        if ints1[index] != ints2[index]:
            return False
        index += 1
    return True
