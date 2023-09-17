"""The Real Wordle - Ex03."""
__author__ = "730434721"
word: str = ""
char: str = ""
def contains_char(word: str, char: str) -> bool:
        """Function that finds whether or not a character is within a string."""
        assert len(char) == 1
        if char in word:
            return True
        else:
            return False
guess: str = ""
secret: str = ""
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
def emojified(guess: str, secret: str) -> str:
        """Function prints colored boxes based on character being in word."""
        emoji: str = ""
        index: int = 0
        assert len(guess) == len(secret)
        while index < len(guess) and index < len(secret):
            if contains_char(secret, guess[index]):   
                if contains_char(secret[index], guess[index]):  
                    emoji += GREEN_BOX 
                else:
                    emoji += YELLOW_BOX
            else:
                emoji += WHITE_BOX
            index += 1    
        return emoji
length: int = 0
def input_guess(length: int) -> str:
        """Function asks user for a x character word."""
        word_guess: str = input("Enter a " + str(length) + " character word: ") 
        try_again: str = ""
        if len(word_guess) == length:
            return word_guess
        while len(try_again) != length:
            try_again = input("That wasn't " + str(length) + " chars! Try again: ")
        return try_again
def main() -> None:
        """The entrypoint of the program and main game loop."""
        turn: int = 1
        secret: str = "codes"
        length: int = 5
        while turn < 7:
            print("=== Turn " + str(turn) + "/6 ===")
            guess = input_guess(length)
            print(emojified(guess, secret))
            if guess == secret:
                print("You won in " + str(turn) + "/6 turns!")
                return
            turn += 1
        print("X/6 - Sorry, try again tomorrow!")
if __name__ == "__main__":
    main()



