from game_logic import get_random_word, display_game_state, play_game


if __name__ == "__main__":
    play_game()
    while "y" in input("Do you want to play again?\n").lower():
        play_game()
