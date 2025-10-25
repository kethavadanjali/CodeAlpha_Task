import random

def choose_word():
    # 5 predefined words change 
    words = ["python", "planet", "garden", "coding", "friend"]
    return random.choice(words)

def display_word(secret, guessed_letters):
    # return a string showing guessed letters and underscores for unknowns
    return " ".join([ch if ch in guessed_letters else "_" for ch in secret])

def get_valid_guess(guessed_letters):
    while True:
        guess = input("Guess a letter: ").strip().lower()
        if len(guess) != 1:
            print("Please enter exactly one letter.")
            continue
        if not guess.isalpha():
            print("Please enter a letter (a-z).")
            continue
        if guess in guessed_letters:
            print(f"You already guessed '{guess}'. Try a different letter.")
            continue
        return guess

def play_hangman():
    secret = choose_word()
    guessed_letters = set()
    incorrect_guesses = 0
    max_incorrect = 6

    print("Welcome to Hangman!")
    # main game loop
    while True:
        print("\n" + "-"*30)
        current = display_word(secret, guessed_letters)
        print("Word: ", current)
        print("Guessed letters:", " ".join(sorted(guessed_letters)) if guessed_letters else "None")
        print(f"Incorrect guesses left: {max_incorrect - incorrect_guesses}")

        # check if player has already won
        if all(ch in guessed_letters for ch in secret):
            print("\nCongratulations — you guessed the word:", secret)
            break

        # check if out of attempts
        if incorrect_guesses >= max_incorrect:
            print("\nSorry, you've run out of guesses.")
            print("The correct word was:", secret)
            break

        # get a valid new guess
        guess = get_valid_guess(guessed_letters | set())  # pass current guesses for validation
        # add to guessed set
        guessed_letters.add(guess)

        if guess in secret:
            print(f"Good job — '{guess}' is in the word!")
        else:
            print(f"Sorry — '{guess}' is NOT in the word.")
            incorrect_guesses += 1

    print("-"*30)

def main():
    while True:
        play_hangman()
        again = input("Play again? (y/n): ").strip().lower()
        if again != "y":
            print("Thanks for playing! Goodbye.")
            break

if __name__ == "__main__":
    main()
