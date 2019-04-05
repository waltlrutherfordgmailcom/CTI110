# This program is a Bug collector that asks for the sum of bugs over a span of five days.
# 3/06/2019
# CTI-110 P4T2 - Bug Collector
# Walter rutherford

# Create a while loop.
# Create a for loop of days.
# Get number of bugs.
# Display total.

# Function defined as bug collection.
def bug_collection():

    # While loop. 
    Begin = 'y'
    while Begin == 'y':

        # Accumulater.
        Total = 0

        # For loop in range of days.
        for day in range(1,6):
            print ('\nEnter the amount of bugs collect on day', day,":")

            # Input for bugs collected.
            Bugs = int(input())

            # Variable for total.
            Total += Bugs

        # Print the total.
        print ('The total amount of bugs collected is:',Total)

        # Input for continuation of another 5 days.
        Begin = input('\nWould you like to add another 5 days ("y" for yes' +\
        ' and "n" for no):')

bug_collection()


        
    
    















































































































































































































