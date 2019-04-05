# This program converts feet to inches.
# 3/28/2019
# CTI-110 P5T2_FeetToInches 
# Walter Rutherford

# Get feet from user.
# Create feet to inches function with conversion
# Display conversion.


# Constant for the number of inches per foot. 
inches_per_foot = 12


# Main function.
def main():
    

    # Input for number of feet from user.
    feet = int(input("Enter a number of feet:  "))

    # Display of conversion to inches.
    print(feet,"feet equals",feet_to_inches(feet),"inches.")


# Feet to inches function converting feet to inches.
def feet_to_inches(feet):
    return feet * inches_per_foot

# Call to main function.
main()







