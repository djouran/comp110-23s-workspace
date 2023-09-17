"""File to define River class."""


__author__ = "730434721"


from exercises.ex09.fish import Fish
from exercises.ex09.bear import Bear


class River:
    """Tracks the removal and repopulation of bears and fish."""

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for x in range(0, num_fish):
            self.fish.append(Fish())
        for x in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Checks the ages of bears and fish in order to filter overage ones out of the lists."""
        self.fish = [fish for fish in self.fish if fish.age <= 3]
        self.bears = [bear for bear in self.bears if bear.age <= 5]

    def remove_fish(self, amount: int):
        """Removes fish based on the amount of fish eaten."""
        for i in range(amount):
            del self.fish[0]

    def bears_eating(self):
        """Sets the condition of how many fish are eaten by a bear."""
        for bear in self.bears:
            if len(self.fish) >= 5:
                fish_to_remove = 3
                self.remove_fish(fish_to_remove)
                bear.eat(fish_to_remove)

    def check_hunger(self):
        """Check's the hunger of the bears."""
        surviving_bears = []
        for bear in self.bears:
            if bear.hunger_score >= 0:
                surviving_bears.append(bear)
        self.bears = surviving_bears

    def view_river(self):
        """Prints script to show amount of fish and bears are alive."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")

    def repopulate_fish(self):
        """Number of fish repopulates based on how many fish are available."""
        num_fish = len(self.fish)
        i: int = 0
        while i < (num_fish // 2) * 4:
            self.fish.append(Fish())
            i += 1

    def repopulate_bears(self):
        """Repopulates bears based on the amount of bears are available."""
        num_bears = len(self.bears)
        i: int = 0
        while i < (num_bears // 2):
            self.bears.append(Bear())
            i += 1

    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        """Print's out amount of bears and fish after a week."""
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
