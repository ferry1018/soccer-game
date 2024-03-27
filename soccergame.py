import time  # Importing the time module to incorporate delays
import random  # Importing the random module for random selection


# Function to print messages with a delay
def print_pause(*messages):
    # Iterating over each message
    for message in messages:
        print(message)  # Printing the message
        time.sleep(1.5)  # Delaying execution by 1.5 seconds


# Function to simulate taking a penalty
def take_penalty():
    # Print statement
    print_pause("You step up to take the decisive penalty kick.")
    # List of possible outcomes
    outcomes = ["score", "miss", "hit_post", "saved"]
    outcome = random.choice(outcomes)  # Randomly selecting an outcome
    # Handling different outcomes
    if outcome == "score":
        print_pause("You shoot, and it's a GOAL! "
                    "Your country wins the World Cup! ",
                    "You're hailed as a national hero!")
    elif outcome == "miss":
        print_pause("You shoot, but the ball goes wide! ",
                    "Your country loses the World Cup... ",
                    "Despite everyone's efforts to console you, "
                    "you can't help but feel disappointed.")
    elif outcome == "hit_post":
        print_pause("You shoot, but the ball hits the post! ",
                    "Your country loses the World Cup... ",
                    "You're heartbroken at the missed opportunity.")
    else:
        print_pause("You shoot, but the goalkeeper makes an incredible save! ",
                    "Your country loses the World Cup... ",
                    "The goalkeeper is being praised for their heroics.")


# Function to simulate passing the penalty to a teammate
def pass_penalty():
    print_pause("You decide to pass the penalty to your teammate.")
    outcomes = ["score", "miss", "hit_post", "saved"]
    outcome = random.choice(outcomes)
    if outcome == "score":
        print_pause("Your teammate shoots, and it's a GOAL! "
                    "Your country wins the World Cup! ",
                    "Your teammate is celebrated as the hero.")
    elif outcome == "miss":
        print_pause("Your teammate shoots, but the ball goes wide! ",
                    "Your country loses the World Cup... ",
                    "People see you as a coward who chickened out.")
    elif outcome == "hit_post":
        print_pause("Your teammate shoots, but the ball hits the post! ",
                    "Your country loses the World Cup... ",
                    "People blame you for passing the penalty.")
    else:
        print_pause("Your teammate shoots, "
                    "but the goalkeeper makes an incredible save! ",
                    "Your country loses the World Cup... ",
                    "People criticize your decision to pass the penalty.")


# Function to play the penalty shootout game
def play_game():
    print_pause("It's the final of the Soccer World Cup, "
                "and your country has never won before.",
                "You have been picked to play the last penalty",
                "You have a chance to make history today "
                "if you score this decisive penalty.")

    while True:
        choice = input("What do you want to do? "
                       "Enter 1 to take the penalty, "
                       "or 2 to pass it to your teammate: ")
        if choice == '1':
            take_penalty()  # Calling take_penalty function
            break
        elif choice == '2':
            pass_penalty()  # Calling pass_penalty function
            break
        else:
            # Error message for invalid input
            print("Invalid input. Please enter 1 or 2.")

    while True:
        play_again = input("GAME OVER!\n"
                           "Would you like to play again? (y/n): ")
        if play_again.lower() == 'y':
            print_pause("Starting a new game...")  # Print statement
            # Recursive call to play_game function to start a new game
            play_game()
            break
        elif play_again.lower() == 'n':
            print_pause("Thanks for playing!")  # Print statement
            break
        else:
            # Error message for invalid input
            print("Invalid input. Please enter 'y' or 'n.'")


if __name__ == "__main__":
    play_game()  # Calling the play_game function to start the game
