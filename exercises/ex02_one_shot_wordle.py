"""ex02_one_shot_wordle.py - The Wordle."""

__author__ = "730434721"
secret: str = "python"
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
guess_again: str = input("What is your 6-letter guess? ")
while guess_again != secret:
    if len(guess_again) != 6:
        guess_again = input("That was not 6 letters! Try again: ")
    else:
        emoji = ""
        index = 0
        while index < 6:
            if guess_again[index] == secret[index]:
                emoji += GREEN_BOX
            else:
                in_word = False
                alt_index = 0
                while alt_index < 6 and not in_word:
                    if guess_again[index] == secret[alt_index]:
                        in_word = True
                        emoji += YELLOW_BOX
                    alt_index += 1
                if not in_word:
                    emoji += WHITE_BOX
            index += 1
        print(emoji)
        if guess_again != secret:
            print("Not quite. Play again soon!")
            break
print(GREEN_BOX + GREEN_BOX + GREEN_BOX + GREEN_BOX + GREEN_BOX + GREEN_BOX)
print("Woo! You got it!")