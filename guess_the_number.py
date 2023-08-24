### Imports
import random, time, os



# Variables
game_status = True


### Functions
def _start():
    """The start function will determine the difficulty of the game"""
    # Use input to get the games difficulty
    game_difficulty = input("What difficulty do you want to play?\n1. Easy (1-10)\n2. Medium (1-100)\n3. Hard: (1-1000)\ndifficulty: ")
    # Ensure game_difficulty is lowercase (lower()) and replace spaces with an empty string for an easier and safer comparison
    game_difficulty = game_difficulty.lower().replace(" ", "")
    # Checking the users input and passing the difficulty as a parameter
    if game_difficulty == "1" or game_difficulty == "easy":
        the_game(10)
    elif game_difficulty == "2" or game_difficulty == "medium":
        the_game(100)
    elif game_difficulty == "3" or game_difficulty == "hard":
        the_game(1000)
    else:
        print("Invalid response. Please try again with either 'Easy', 'Medium' or 'Hard'.")


def the_game(end_num):
    # Keeps the game playing while the game_status is True
    while True:
        # This clears the console, is not needed, but keeps the games console clear of previous games & the difficulty setup.
        os.system("cls")
        # Generates the random number based on difficulty
        number = random.randint(1, end_num)
        # Input for the user to guess the number 
        guess = input(f"Guess the number, 1-{end_num}...\nGuess: ")
        # removes whitespace and ensures all characters are lowercase checking if the input was end
        guess = guess.replace(" ", "").lower()
        #saying "end" will break the loop there-go ending the game
        if guess == "end":
            break
        else:
            # The loop will forever go on until the user enters a number 
            while True:
                # Attempts to break the loop if guess is "end"
                #otherwise it will try to make guess an integer
                try:
                    if guess.replace(" ", "").lower() == "end":
                        break
                    else:
                        guess=int(guess)
                        break
                #if guess cant be converted to an integer and it is not "end", an error will be thrown and the user will need to re-enter the number.
                except:
                    print(f"Invalid response. Please enter 'end' or an integer between 1-{end_num}.")
                    time.sleep(1)
                    os.system("cls")
                    guess = input(f"Guess the number, 1-{end_num}...\nGuess: ")
                    guess = guess.replace(" ", "").lower()
        if guess == "end":
            break
        if guess == number:
            print("Congratulations, you mentioned the correct number!")

        else:
            print(f"Incorrect number! The number was {number}...")

        # Waits 2 seconds before restarting
        time.sleep(2)
        



_start()
