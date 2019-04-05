
# This program runs as a guessing game between 1 and 100.
# 4/4/2019
# CTI-110 P5HW1 - Random Number
# Walter Rutherford

# Creat function for first game.
# Generate random number.
# Get user input.
# display the result.
# Create function for the second game.
# Generate random number.
# Get user input.
# Display the result. 


import random

def rand1():
    # First the computer picks a number.
    random.seed(10)
    number = random.randint(1,101 )
    guessed = True
    guesses = 1

    # Then the user guesses.
    while guessed:
        print("\n                Welcome to the guessing game!")
        print("         ______________________________________________")
        guess = int(input("Enter a random number between 1 and 100: "))
        if guess > number:
            print("Too high, try again!")
            guesses += 1
        elif guess < number:
            print("Too low try again") 
            guesses += 1

        # If the use guesses the correct number the function switches to generate a new set of numbers.
        elif guess == number:
            print("\nCongrats you won! Your number of guesses is ", guesses,".")
            print("\nNew game beginning......")
            guessed = False  
            guessed_true()
            
        
        
# Secondary function.                
def guessed_true():
    random.seed(20)

    # The computer pics new set of random numbers.
    number = random.randint(1,101 )
    guessed = True
    guesses = 1

    # The user guesses again.
    while guessed:
        print("\n                Welcome to the guessing game!")
        print("         ______________________________________________")
        guess = int(input("Enter a random number between 1 and 100: "))
        
        if guess > number:
            print("Too high, try again!")
            guesses += 1
        elif guess < number:
            print("Too low, try again!") 
            guesses += 1

        # If the user guesses the correct number the game starts over on rand1().
        elif guess == number:
            print("\nCongrats you won! Your number of guesses is ", guesses,".")
            print("\nNew game beginning......")
            guessed = False
            rand1()
            
rand1()





   




   
    
        


          
