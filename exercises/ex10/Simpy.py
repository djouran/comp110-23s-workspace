"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730434721"


class Simpy:
    """Class that has many functions that have different functionalities."""
    values: list[float]

    def __init__(self, simpy_value: list[float]):
        """Default magic method to fill objects."""
        self.values = simpy_value

    def __str__(self) -> str:
        """Magic method for strings."""
        return f"Simpy({str(self.values)})"

    def fill(self, value: float, count: int) -> None:
        """Fill's the object."""
        self.values = [value] * count

    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Arranges the object."""
        assert step != 0.0
        values = []
        if step > 0:
            while start < stop:
                values.append(start)
                start += step
        else:
            while start > stop:
                values.append(start)
                start += step
        self.values = values


    def sum(self) -> float:
        """Returns a sum."""
        return sum(self.values)

    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Return new Simpy object."""
        my_object: list[float] = []
        if isinstance(rhs, float):
            for item in self.values:
                my_object.append(item + rhs)
        else:
            assert len(self.values) == len(rhs.values)
            for i in range(0, len(self.values)):
                my_object.append(rhs.values[i] + self.values[i])
        return Simpy(my_object)

    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Takes an object or float and exponentiates it."""
        my_object: list[float] = []
        if isinstance(rhs, float):
            for item in self.values:
                my_object.append(item**rhs)
        else:
            assert len(self.values) == len(rhs.values)
            for item in range(0, len(self.values)):
                my_object.append(self.values[item] ** rhs.values[item])
        return Simpy(my_object)

    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Parses through objects to find whether or not it is equal to each other."""
        my_object: list[bool] = []
        if isinstance(rhs, float):
            return [x == rhs for x in self.values]
        else:
            assert len(self.values) == len(rhs.values)
            for item in range(0, len(self.values)):
                if self.values[item] == rhs.values[item]:
                    my_object.append(True)
                else:
                    my_object.append(False)
        return my_object

    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Parses through objects and returns whether or not the other is larger."""
        my_object: list[bool] = []
        if isinstance(rhs, float):
            return [x > rhs for x in self.values]
        else:
            assert len(self.values) == len(rhs.values)
            for item in range(0, len(self.values)):
                if self.values[item] > rhs.values[item]:
                    my_object.append(True)
                else:
                    my_object.append(False)
        return my_object

    def __getitem__(self, rhs: int) -> float:
        """Overrides indexing."""
        return self.values[rhs]

    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Filters through."""
        if isinstance(rhs, int):
            return self.values[rhs]
        else:
            return Simpy([val for i, val in enumerate(self.values) if rhs[i]])
