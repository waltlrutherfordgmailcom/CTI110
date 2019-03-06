# This program asks the user to enter a series of positive numbers for a sum.
# 3/6/2019
# CTI-110 P4HW3 - Sum of Numbers
# Walter Rutherford

#Define function.
#Define Variables.
#Create Loop for continuence.
#Create counting range.
#Get an integer.
#Create if statements.
#Display total.
#Get continuence yes or no.


# Beginning of function.
def Sum_function ():

    # Defined variables for max, Total, Number, and variable for while loop (Start_over = 'y').
    max = 5
    Total= 0
    Number = 0
    Start_Over = 'y'
     
    # While loop (Start_Over is equal to "y"). 
    while Start_Over== 'y':

        # Displayed introduction.
        print ('\nThis program calculates the sum of 5 positive numbers. If a negative number')
        print('is entered, the series will end, and the program will exit.')

        # Assigned rules for the number count (for and if statments).
        for counter in range (max):
            Number = int (input('\nEnter a  number:'))
            if Number > -1:
                Total += Number
                max = max
            
            
            elif Number < 0:
                exit()
    

        # Display of Total
        print('\nThe total is',Total)

        # Re-define Start_Over with "input" to determine continuation of while loop.
        Start_Over = input ('\nIf you would like to continue press "y", if not press "n": ')


# End of function
Sum_function()       


                               

        

        

        

        

    

    
    
    

    
    
