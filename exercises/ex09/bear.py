"""File to define Bear class."""


class Bear:
    """Class that tracks the hunger and age of a bear."""
    def __init__(self):
        """Initializes bear hunger and age to 0."""
        self.age = 0
        self.hunger_score = 0
    
    def one_day(self):
        """Adds age and substracts hunger score by 1 respectively."""
        self.age += 1
        self.hunger_score -= 1

    def eat(self, num_fish: int):
        """Hunger score increases by the amount of fish eaten."""
        self.hunger_score += num_fish