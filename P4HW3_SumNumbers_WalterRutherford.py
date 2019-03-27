# This program asks the user to enter a series of positive numbers for a sum.
# 3/6/2019
# CTI-110 P4HW3 - Sum of Numbers
# Walter Rutherford

# Define function.
# Define variables.
# Display introduction.
# Create while loop.
# Get the Integer.
# Display Total.

# Beginning of function.
def Sum_function ():

    # Defined variables for max, Total, Number, and variable for while loop (Start_over = 'y').
    Total= 0
    Number = 0

    # Displayed introduction.
    print('\nThis program calculates the sum of all positive numbers.If a negative number is entered, the series will end, and the program will exit.')
    

    # Nested while loop.
    while Number > -1:

        # Equation for total.
        Total += Number

        # Input number type.
        Number = int (input('\nEnter a  number:'))
            
    # printed total
    print('\nThe total is',Total)

        


# End of function.
Sum_function()       


                               

        

        

        

        

    

    
    
    

    
    
