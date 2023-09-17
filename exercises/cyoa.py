"""EX06 - The game of LIFE."""

__author__ = "730434721"

import random


profession: str = ""
points: int = 0
player: str = ""
emoji: str = "\U0001F389"


def greet() -> None:
    """Procedure that greets player into the game."""
    global player
    print(f"Welcome! You have entered the game of LIFE! You will be taken on a journey that will give you choices of what you would like to do for your virtual life! Each decision will have rewards or consequences. These outcomes will be determined with the NET WORTH you will end with. The higher the net worth the better, unless you like being broke. Now, let's start your life! {emoji}")
    player = input("What is your name? ")


def country() -> None:
    """Country you want to live in."""
    global points
    country = input(f"{player}, what country would you like to live in? You have 3 choices, China, Russia, and the US. (Case Sensitive) ")
    if country == "China":
        points += 2
    if country == "Russia":
        points += 3
    if country == "US":
        points += 10


def choicePoints(profession: str) -> int:
    """Based on choice, different outcomes based on randomness."""
    global points
    profession = input("Here is your second and final choice! You can either go to college, be an entrepreneur, or criminal. What is your choice? (lowercase) ")
    if profession == "criminal":
        if random.random() < 0.1:
            points += 20
            return points
        else:
            points -= 100
            return points
    if profession == "entrepreneur":
        outcome = random.random()
        if outcome < 0.3:
            points -= 5
            return points
        if outcome < 0.7:
            points += 5
            return points
        else:
            points += 20
            return points
    if profession == "college":
        outcome = random.random()
        if outcome < 0.5:
            points += 10
            return points
        else:
            points += 3
            return points


def main() -> None:
    """The Main Function that starts and ends the adventure."""
    greet()
    country()
    total_points = points
    while True:
        print(f"Your total points: {total_points}")
        choice = input("Do you want to continue playing? (y/n) ")
        if choice == "n":
            print(f"Thanks for playing {player}! Your final score is {total_points}. {emoji}")
            break
        elif choice == "y":
            print(f"You have ended up with {str(choicePoints(profession))} points. You have reached the end of your adventur! Thanks for playing! {emoji}")
            break
        else:
            print("Invalid choice. Please enter 'y' to continue playing or 'n' to stop playing.")
   

if __name__ == "__main__":
    main()
