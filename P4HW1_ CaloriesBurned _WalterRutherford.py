# This program is a calorie counter for times of 20 min, 35 min, and 45 min.
# 2/25/2019
# CTI-110 P4HW1 - Calories Burned
# Walter Rutherford
 

# Define function.
# Create  for Loop.
# Display run time.
# Create call function.


# Function defined. 
def calorie_count():
    # For loop with three different times.
    for times in [20,35,45]:
        # Calorie count.
        calorie_count = 5 * times

        # Print statement with calories burned. 
        print("You can burn",calorie_count,"calories in", times, "minutes.")

# Call to function.
calorie_count()




