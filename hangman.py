import random

# List of words
words = ["python", "computer", "coding", "laptop", "program"]

# Choose a random word
secret_word = random.choice(words)

# Create blank display
display = []

for letter in secret_word:
    display.append("_")

print("Welcome to Hangman Game!")

lives = 6

while lives > 0:

    print("\nWord:", " ".join(display))

    guess = input("Enter a letter: ").lower()

    found = False

    for i in range(len(secret_word)):
        if secret_word[i] == guess:
            display[i] = guess
            found = True

    if found:
        print("Correct Guess!")
    else:
        lives -= 1
        print("Wrong Guess!")
        print("Lives Left:", lives)

    if "_" not in display:
        print("\nCongratulations! You Won.")
        print("The Word is:", secret_word)
        break

if lives == 0:
    print("\nGame Over!")
    print("The Correct Word was:", secret_word)