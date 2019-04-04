# This program simulates a game of Rock, Paper, Scissors.
# 4/4/2019
# CTI-110 P5HW2 - Rock, Paper, Scissors Game.
# Walter Rutherford


# Get user input for selection.
# Create simulation with arguements.
# Dipslay the Result based on an opposing random intiger.



# call to import random function.
import random

# The main function "RPS"(Rock, Paper, Scissors).
def RPS():

    # Introduction requesting user input (user_choice), and computers choice (random.randit).
    computer = random.randint(1, 3)
    print("Welcome to a game of Rock, Paper, Scissors!")
    print("_____________________________________________")
    print("Select a number:")
    print("\n1.  Rock")
    print("2.  Paper")
    print("3.  Scissors")
    user_choice = int(input("\n    "))
    

    # Simulation of the game with if statements (Call to RPS() if a tie, and Error
    # when outside of parameters).
    if user_choice == 1 and computer == 3:
        print("\nYou win! (The computer chose scissors, and rock smashes scissors).")
        print("\n                    Thanks for playing!")
    elif user_choice == 3 and computer == 1:
        print("\nYou loose! (The computer chose rock, and rock smashes scissors).")
        print("\n                    Thanks for playing!")
    elif user_choice == 3 and computer == 2:
        print("\nYou win! (The computer chose paper, and scissors cut paper).")
        print("\n                    Thanks for playing!")
    elif user_choice == 2 and computer == 3:
        print("\nYou loose! (The computer chose paper, and scissors cut paper).")
        print("\n                    Thanks for playing!")
    elif user_choice == 2 and computer == 1:
        print("\nYou win!(The computer chose rock, and Paper wraps rock).")
        print("\n                    Thanks for playing!")
    elif user_choice == 1 and computer == 2:
        print("\nYou loose!(The computer chose paper, and Paper wraps rock).")
        print("\n                   Thanks for playing!")
    elif user_choice == computer:
            print("\nDraw! Play again...")
            RPS()
    else:
        if user_choice > 3:
            print("\nError!!please use a valid selection...\n")
            RPS()
        if user_choice < 1:
                print("\nError!!please use a valid selection...\n")
                RPS()

            
# Call to rock, paper, scissors function.
RPS()
          
