import random
from art import logo

def play_game():
    print(logo)
    print("Welcome to the number guessing game!")
    print("I'm thinking of a number between 1 and 100")

    # Set difficulty
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    total_guesses = 10 if difficulty == "easy" else 5

    choice = random.randint(1, 100)

    current_guess_count = 0
    is_game_over = False

    while not is_game_over:
        guess_input = input(f"Make a guess (1-100). You have {total_guesses - current_guess_count} attempts left: \n").strip()

        try:
            guess = int(guess_input)
        except ValueError:
            print("Invalid input. Please enter a whole number between 1 and 100.")
            continue

        if not (1 <= guess <= 100):
            print("Out of range. Enter a number from 1 to 100.")
            continue

        # If validation successful, increment the guess count
        current_guess_count += 1
        
        if guess == choice:
            print(f"🎉 Congratulations! You guessed it in {current_guess_count} tries! ")
            is_game_over = True
        elif guess > choice:
            print("Too high, try again!")
        elif guess < choice:
            print("Too low, try again!")
        
        # Check if out of attempts
        if current_guess_count >= total_guesses and not is_game_over:
            print(f"💀 Game Over! You've used all {total_guesses} guesses. The number was {choice}.")
            is_game_over = True

    # Play again?
    replay = input("Do you want to play again? Type 'y' or 'n': ").lower()
    if replay == "y":
        play_game()
    else:
        print("Thanks for playing! Goodbye!")

play_game()
