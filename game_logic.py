import random
from ascii_art import STAGES


# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]


def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def display_game_state(mistakes, secret_word, guessed_letters):
    # Display the snowman stage for the current number of mistakes.
    print(STAGES[mistakes])
    # Build a display version of the secret word.
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print("Word: ", display_word)
    print("\n")


def play_game():
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0

    print("Welcome to Snowman Meltdown!")
    while True:
        # For now, display the initial game state.
        display_game_state(mistakes, secret_word, guessed_letters)

        # Prompt user for one guess (logic to be enhanced later)
        guess = input("Guess a letter: ").lower()
        if len(guess) == 1 and guess.isalpha() and guess in secret_word:
            guessed_letters.append(guess)
        else:
            mistakes += 1
        print("You guessed:", guess)
        if mistakes >= len(STAGES):
            print("You lost, the snowman melt")
            break
        if len(guessed_letters) == len(set(secret_word)):
            print("You won, the snowman did not melt")
            break
