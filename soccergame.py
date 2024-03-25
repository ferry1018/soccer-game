import time
import random

def print_pause(*messages):
    for message in messages:
        print(message)
        time.sleep(1.5)

def take_penalty():
    print_pause("You step up to take the decisive penalty kick.")
    outcomes = ["score", "miss", "hit_post", "saved"]
    outcome = random.choice(outcomes)
    if outcome == "score":
        print_pause("You shoot, and it's a GOAL! Your country wins the World Cup!", "You're hailed as a national hero!")
    elif outcome == "miss":
        print_pause("You shoot, but the ball goes wide!", "Your country loses the World Cup...", "Despite everyone's efforts to console you, you can't help but feel disappointed.")
    elif outcome == "hit_post":
        print_pause("You shoot, but the ball hits the post!", "Your country loses the World Cup...", "You're heartbroken at the missed opportunity.")
    else:
        print_pause("You shoot, but the goalkeeper makes an incredible save!", "Your country loses the World Cup...", "The goalkeeper is being praised for their heroics.")

def pass_penalty():
    print_pause("You decide to pass the penalty to your teammate.")
    outcomes = ["score", "miss", "hit_post", "saved"]
    outcome = random.choice(outcomes)
    if outcome == "score":
        print_pause("Your teammate shoots, and it's a GOAL! Your country wins the World Cup!", "Your teammate is celebrated as the hero.")
    elif outcome == "miss":
        print_pause("Your teammate shoots, but the ball goes wide!", "Your country loses the World Cup...", "People see you as a coward who chickened out.")
    elif outcome == "hit_post":
        print_pause("Your teammate shoots, but the ball hits the post!", "Your country loses the World Cup...", "People blame you for passing the penalty.")
    else:
        print_pause("Your teammate shoots, but the goalkeeper makes an incredible save!", "Your country loses the World Cup...", "People criticize your decision to pass the penalty.")

def play_game():
    print_pause("It's the final of the Soccer World Cup, and your country has never won before.",
                "You have been picked to play the last penalty",
                "You have a chance to make history today if you score this decisive penalty.")
    while True:
        choice = input("What do you want to do? Enter 1 to take the penalty, or 2 to pass it to your teammate: ")
        if choice == '1':
            take_penalty()
            break
        elif choice == '2':
            pass_penalty()
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
