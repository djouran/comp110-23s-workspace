"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730434721"

word: str = input("Enter a 5-character word: ")
if len(word) != 5:
    print("Error: Word must contain 5 characters")
    exit()
character: str = input("Enter a single character: ")
if len(character) != 1:
    print("Error: Character must be a single character")
    exit()
instances: int = 0
print("Searching for " + character + " in " + word)
if character in word:
    if word.rfind(character) == 0:
        instances += 1
        print(character + " found at index " + str(word.rfind(character)))
        print(str(instances) + " instance of " + character + " found in " + word)
    if word.rfind(character) == 1 and word.find(character) == 0:
        instances += 1
        print(character + " found at index " + str(word.rfind(character)))
        print(str(instances) + " instances of " + character + " found in " + word)
    if word.rfind(character) == 2 and word.find(character) == 0:
        instances += 2
        print(character + " found at index " + str(word.rfind(character) - 1))
        print(character + " found at index " + str(word.rfind(character)))
        print(str(instances) + " instances of " + character + " found in " + word)
    if word.rfind(character) == 3 and word.find(character) == 0:
        instances += 3
        print(character + " found at index " + str(word.rfind(character) - 3))
        print(character + " found at index " + str(word.rfind(character) - 2))
        print(character + " found at index " + str(word.rfind(character) - 1))
        print(character + " found at index " + str(word.rfind(character)))
        print(str(instances) + " instances of " + character + " found in " + word)
    if word.rfind(character) == 4 and word.find(character) == 0:
        instances += 5
        print(character + " found at index " + str(word.rfind(character) - 4))
        print(character + " found at index " + str(word.rfind(character) - 3))
        print(character + " found at index " + str(word.rfind(character) - 2))
        print(character + " found at index " + str(word.rfind(character) - 1))
        print(character + " found at index " + str(word.rfind(character)))
        print(str(instances) + " instances of " + character + " found in " + word)
    if word.find(character) == word.rfind(character):
        instances += 1
        print(character + " found at index " + str(word.rfind(character)))
        print(str(instances) + " instance of " + character + " found in " + word)
    if word.find(character) == 1 and word.rfind(character) == 2:
        instances += 2
        print(character + " found at index " + str(word.rfind(character) - 1))
        print(character + " found at index " + str(word.rfind(character)))
        print(str(instances) + " instances of " + character + " found in " + word)
    if word.find(character) == 1 and word.rfind(character) == 3:
        instances += 3
        print(character + " found at index " + str(word.rfind(character) - 2))
        print(character + " found at index " + str(word.rfind(character) - 1))
        print(character + " found at index " + str(word.rfind(character)))
        print(str(instances) + " instances of " + character + " found in " + word)
    if word.find(character) == 1 and word.rfind(character) == 4:
        instances += 4
        print(character + " found at index " + str(word.rfind(character) - 3))
        print(character + " found at index " + str(word.rfind(character) - 2))
        print(character + " found at index " + str(word.rfind(character) - 1))
        print(character + " found at index " + str(word.rfind(character)))
        print(str(instances) + " instances of " + character + " found in " + word)
    if word.find(character) == 2 and word.rfind(character) == 3:
        instances += 2
        print(character + " found at index " + str(word.rfind(character) - 1))
        print(character + " found at index " + str(word.rfind(character)))
        print(str(instances) + " instances of " + character + " found in " + word)
    if word.find(character) == 2 and word.rfind(character) == 4:
        instances += 3
        print(character + " found at index " + str(word.rfind(character) - 2))
        print(character + " found at index " + str(word.rfind(character) - 1))
        print(character + " found at index " + str(word.rfind(character)))
        print(str(instances) + " instances of " + character + " found in " + word)
    if word.find(character) == 3 and word.rfind(character) == 4:
        instances += 2
        print(character + " found at index " + str(word.rfind(character) - 1))
        print(character + " found at index " + str(word.rfind(character)))
        print(str(instances) + " instances of " + character + " found in " + word)
else:   
    print("No instances of " + character + " found in " + word)



