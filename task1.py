import random

words = ["apple", "ball", "cat", "dog", "book"]
word = random.choice(words)

guessed = ""
chances = 6

while chances > 0:
    display = ""

    for letter in word:
        if letter in guessed:
            display += letter
        else:
            display += "_"

    print("Word:", display)

    if display == word:
        print("You Win!")
        break

    guess = input("Enter a letter: ")
    guessed += guess

    if guess not in word:
        chances -= 1
        print("Wrong Guess!")
        print("Chances Left:", chances)

if chances == 0:
    print("Game Over!")
    print("The word was:", word)
