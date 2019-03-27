# This program is a calorie counter for times of 20 min, 35 min, and 45 min.
# 2/25/2019
# CTI-110 P4HW1 - Calories Burned
# Walter Rutherford
 

# Create function.
# Define Loop.
# Get run time( 20 minutes, 35 minutes, or 45 minutes).
# Display run time.
# Run Loop again with prompt.


# Function defined as calorie_count.
def calorie_count():

    # End of while Loop.
    Run_Again = 'y'or 'r'

    # Agreeing statement.
    while Run_Again == 'y'or 'r':

            # Input for run time.
            Minutes_Ran = int(input('\nEnter the total amount of time that you ran in minutes(choices include 20 minutes,35 minutes,or 45 minutes):  '))

            # Variable equation for calories burned.
            Calories_Burned = 5 * Minutes_Ran

            # If statement for 20 minutes.
            if Minutes_Ran == 20:

                    # Displayed total for 20 mins.
                    print ('\nYou have burned',5 * Minutes_Ran,'calories in 20 minutes!')

                    # Run loop again.
                    Run_Again= input('\nWould you like to enter another recorded time?( "y" for yes or "n" for no):  ')

            # If statement for 35 min.
            elif Minutes_Ran == 35:
                    # Displayed total for 35 mins.
                    print ('\nYou have burned',5 * Minutes_Ran,'calories in 35 minutes!')

                    # Run loop again.
                    Run_Again= input('\nWould you like to enter another recorded time?( "y" for yes or "n" for no):  ')

            # If statement for 45 min.
            elif Minutes_Ran == 45:
                    # Displayed total for 35 mins.
                    print ('\nYou have burned',5 * Minutes_Ran,'calories in 45 minutes!')

                    # Run loop again.
                    Run_Again= input('\nWould you like to enter another recorded time?( "y" for yes or "n" for no):  ')

            # Contrary rule.
            else:
                Run_Again= input ('\nPlease try again with one of the times specified by pressing "r" for return:')
                

# Beginning of function.            
calorie_count()









        




