# Hangman Game

# Word input by the 1st player
word = input("Player 1, enter a word for Player 2 to guess: ").lower()

# Initialize variables
guesses = []
max_attempts = 7
attempt_count = 0
word_to_guess = list(word)
current_guess = ['_'] * len(word)

# Print initial dashes for the word
for letter in current_guess:
    print('_', end=' ')
print()

# Main game loop
while '_' in current_guess and attempt_count < max_attempts:
    # Display previous guesses
    if guesses:
        print("Previous guesses: ", end="")
        for guess in guesses:
            print(guess, end=" ")
        print()

    # Get guess from player 2
    guess = input("Player 2, enter your guess: ").lower()

    # Check if guess is valid
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue

    # Check if guess has already been made
    if guess in guesses:
        print("You've already guessed that letter.")
        continue

    # Add guess to the list of guesses
    guesses.append(guess)

    # Check if guess is correct
    if guess in word_to_guess:
        print("Correct!")
        # Update the current guess with the correct letter
        for i in range(len(word_to_guess)):
            if word_to_guess[i] == guess:
                current_guess[i] = guess
    else:
        print("Incorrect!")
        attempt_count += 1
        # Print the hangman body
        print(f"Attempts left: {max_attempts - attempt_count}")
        if attempt_count == 1:
            print("   O   ")
        elif attempt_count == 2:
            print("   O   ")
            print("   |   ")
        elif attempt_count == 3:
            print("   O   ")
            print("  /|   ")
        elif attempt_count == 4:
            print("   O   ")
            print("  /|\\  ")
        elif attempt_count == 5:
            print("   O   ")
            print("  /|\\  ")
            print("  /    ")
        elif attempt_count == 6:
            print("   O   ")
            print("  /|\\  ")
            print("  / \\  ")

    # Print current progress of the word
    for letter in current_guess:
        print(letter, end=" ")
    print()

# End of game loop
if '_' not in current_guess:
    print("Congratulations! You guessed the word:", word)
else:
    print("Out of attempts! The word was:", word)
