"""File to define Fish class."""


class Fish:
    """Tracks the age of a fish."""
    def __init__(self):
        """Initializes age as 0."""
        self.age = 0
    
    def one_day(self):
        """Adds age of fish by 1."""
        self.age += 1