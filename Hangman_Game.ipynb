import random

# List of 5 predefined words
words = ["python", "apple", "computer", "banana", "school"]

# Randomly choose a word
word = random.choice(words)

# Create hidden word display
guessed_word = ["_"] * len(word)

# Store guessed letters
guessed_letters = []

# Maximum incorrect guesses
max_attempts = 6
wrong_guesses = 0

print("🎮 Welcome to Hangman!")
print("Guess the word one letter at a time.")

while wrong_guesses < max_attempts and "_" in guessed_word:
    print("\nWord:", " ".join(guessed_word))
    print("Wrong guesses left:", max_attempts - wrong_guesses)

    guess = input("Enter a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single alphabet letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("✅ Correct!")

        # Reveal the guessed letter(s)
        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess
    else:
        print("❌ Wrong guess!")
        wrong_guesses += 1

# Game result
if "_" not in guessed_word:
    print("\n🎉 Congratulations! You guessed the word:", word)
else:
    print("\n💀 Game Over!")
    print("The word was:", word)