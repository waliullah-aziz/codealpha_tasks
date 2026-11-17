# Hangman Game - CodeAlpha Python Internship, Task 2
# By Waliullah Aziz
# The computer picks a secret word. The player guesses one letter at a time.
# 6 wrong guesses are allowed. Guess the whole word before they run out!

import random

# The words the computer can pick from
words = ["python", "computer", "keyboard", "program", "internet",
         "student", "library", "teacher", "science", "window"]

secret = random.choice(words)   # pick one word, the player cannot see it
guessed = []                    # letters the player already tried
lives = 6                       # wrong guesses allowed

print("Welcome to Hangman!")
print("The word has", len(secret), "letters. You have", lives, "lives.")

while lives > 0:
    # Show the word: guessed letters open, others as _
    display = ""
    for letter in secret:
        if letter in guessed:
            display = display + letter + " "
        else:
            display = display + "_ "
    print("\nWord:", display)
    print("Lives left:", lives)

    # If no _ is left, the player found every letter
    if "_" not in display:
        print("You win! The word was:", secret)
        break

    guess = input("Guess a letter: ").lower()

    # Only one letter at a time, and not the same letter twice
    if len(guess) != 1 or not guess.isalpha():
        print("Please write only one letter.")
        continue
    if guess in guessed:
        print("You already tried that letter.")
        continue

    guessed.append(guess)

    if guess in secret:
        print("Good! That letter is in the word.")
    else:
        lives = lives - 1
        print("Sorry, that letter is not in the word.")

if lives == 0:
    print("\nGame over! The word was:", secret)
