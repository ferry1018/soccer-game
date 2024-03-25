import time
import random

def print_pause(*messages):
    for message in messages:
        print(message)
        time.sleep(1.5)

def take_penalty():
    print_pause("You step up to take the decisive penalty kick.")
    outcome = random.choice(["score", "miss"])
    if outcome == "score":
        print_pause("You shoot, and it's a GOAL! Your country wins the World Cup!",
                    "You're hailed as a national hero!")
    else:
        print_pause("You shoot, but the goalkeeper saves it!",
                    "Your country loses the World Cup...",
                    "Despite everyone's efforts to console you, you can't help but feel disappointed.")

def pass_penalty():
    print_pause("You decide to pass the penalty to your teammate.")
    outcome = random.choice(["score", "miss"])
    if outcome == "score":
        print_pause("Your teammate shoots, and it's a GOAL! Your country wins the World Cup!",
                    "Your teammate is celebrated as the hero.")
    else:
        print_pause("Your teammate shoots, but the goalkeeper saves it!",
                    "Your country loses the World Cup...",
                    "People see you as a coward who chickened out.")

def play_game():
    print_pause("It's the final of the Soccer World Cup, and your country has never won before.\n"
                "You have been picked to play the last penalty",
                "You have a chance to make history today if you score this decisive penalty.")
    
    while True:
        choice = input("What do you want to do? Enter 1 to take the penalty, or 2 to pass it to your teammate: ")
        outcome = random.choice(["score", "miss"])  
        if choice == '1':
            if outcome == 'score':  
                print_pause("You step up to take the decisive penalty kick.",
                            "You shoot, and it's a GOAL! Your country wins the World Cup!",
                            "You're hailed as a national hero!")
            else:  
                print_pause("You step up to take the decisive penalty kick.",
                            "You shoot, but the goalkeeper saves it!",
                            "Your country loses the World Cup...",
                            "Despite everyone's efforts to console you, you can't help but feel disappointed.")
            break
        elif choice == '2':
            if outcome == 'score':  
                print_pause("You decide to pass the penalty to your teammate.",
                            "Your teammate shoots, and it's a GOAL! Your country wins the World Cup!",
                            "Your teammate is celebrated as the hero.")
            else:  
                print_pause("You decide to pass the penalty to your teammate.",
                            "Your teammate shoots, but the goalkeeper saves it!",
                            "Your country loses the World Cup...",
                            "People see you as a coward who chickened out.")
            break
        else:
            print("Invalid input. Please enter 1 or 2.")

    play_again = input("GAME OVER!\n"
        "Would you like to play again? (y/n): ")
    if play_again.lower() == 'y':
        print_pause("Starting a new game...")
        play_game()
    else:
        print_pause("Thanks for playing!")

play_game()
