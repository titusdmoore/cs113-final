#   @file final.py 
#
#   @description This is a simple program that runs a simple guessing game.
#   The user is prompted to guess a number between 1 and 10. The program will
#   continue to prompt the user until they guess the correct number, providing hints.
# 
#   @author Titus Moore <titusmoore.dev>
#   @contact <titusdmoore@gmail.com>
#   @repo https://github.com/titusdmoore/cs113-final
#   @date 2024

import random

def main():
    display_title()

    # Game loop logic
    wants_to_play = True
    while wants_to_play:
        # From the instructions, it seems like we should not prompt the user to play the first time
        play_game()

        # Prompt the user to see if they want to play again
        play_again = input("Would you want to play again? (yes/no)> ")

        if play_again.lower() != "yes":
            wants_to_play = False

        # I like my whitespace, don't judge me
        print()

    print("Thanks for playing!")



# Function to display the title of the game, as well as the instructions.
# Thid function does not take any arguments, and does not return any values.
def display_title():
    print("+-----------------------------+\n|    Guess the Number Game    |\n+-----------------------------+\n")
    print("I am thinking of a number between 1 and 10. Can you guess it?\n")

# Function that handles the main game loop.
# This function does not take any arguments, and does not return any values.
def play_game():
    # Generate a random number between 1 and 10
    game_value = random.randint(1, 10)

    while True:
        # Local variable to store the user's guess
        user_guess = 0

        try:
            # Try parseInt to ensure that the user input is a valid number
            user_guess = int(input("Guess a number between 1 and 10> "))
        except ValueError:
            print("Please enter a valid number.")

            # We have encountered invalid input, so we should skip parsing the answer and re-prompt the user
            continue 

        # Sanity check to ensure that the user_guess is 1-10
        if user_guess < 1 or user_guess > 10:
            print("Please enter a number between 1 and 10.")
            continue

        if user_guess == game_value:
            print("\nCongratulations! You guessed the correct number.\n")

            # As currently imlemented, the game will end after the user guesses the correct number, so we should leave the function
            return
        elif user_guess > game_value:
            print("Your guess is too high.")
        else:
            print("Your guess is too low.")


# Call main at the bottom, so that we have all of our defined functions
main()

