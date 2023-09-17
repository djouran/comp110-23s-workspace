"""EX05 Tests."""

__author__ = "730434721"


def only_evens(even: list[int]) -> list[int]:
    """Given a list of integers, only returns even numbers."""
    even_list = [x for x in even if x % 2 == 0]
    return even_list


def concat(list1: list[int], list2: list[int]) -> list[int]:
    """Combines the first list and the second list."""
    combined_list = list1 + list2
    return combined_list


def sub(a_list: list[int], start: int, end: int) -> list[int]:
    """Given a list with a starting and ending index, prints out the list within the subset of those indices."""
    if start < 0:
        start = 0
    if end >= len(a_list):
        end = (len(a_list) - 1)
    if len(a_list) == 0 or start >= len(a_list) or end <= 0:
        return []
    final_list: list[int] = []
    while start < end:
        final_list.append(a_list[start])
        start += 1
    return final_list