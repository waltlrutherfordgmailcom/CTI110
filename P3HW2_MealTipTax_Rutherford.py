# Meal and tip calculater: Creating a program that calculates the total
# amount of a meal purchased at a restaurant by tip, tax, and total. 
# 2/12/2019
# CTI-110 P3HW2 - Meal, Tip, and Tax Calculator
# Walter Rutherford

# Get the charge for the meal
# Get the tip percentage they would like to consider (15% or 18% or 20%)
# Create sales tax equation
# Create equations depeneding on percentage.
# Create conditions.
# Creat equation for Total
# Display results



# Create input for the amount charged.
Amount_Charged= float(input('What is the cost of the meal?\n'))


# Create input for the percentage being used.
Tip_Percentage= int( input('What tip percentage would you like to apply %15,%18, or %20?\n'))

# Create equation for Sales tax. 
Sales_Tax= Amount_Charged * .07

# Create equation for %15.
Condition_1 = Amount_Charged *.15
# Create equation for %18.
Condition_2 = Amount_Charged *.18
# Create equation for %20.
Condition_3 = Amount_Charged *.20

# Create condition for %15:If tip enetered is %15 apply condition 1 and add
# sales tax, tip amount and meal cost to dosplay total.
if Tip_Percentage is 15:
    Tip_Amount= Condition_1
    print('Your tip amount is $', Condition_1,'0 with a %7 sales tax of $',Sales_Tax)
    Total= Amount_Charged + Tip_Amount + Sales_Tax
    print ('Your total amount due is:$',Total,'0')

# Create condition for %18:If tip enetered is %18 apply condition 2 and add
# sales tax, tip amount and meal cost to dosplay total.
elif Tip_Percentage is 18:
    Tip_Amount= Condition_2
    print('Your tip amount is $', Condition_2,'0 with a %7 sales tax of $', Sales_Tax)
    Total= Amount_Charged + Tip_Amount + Sales_Tax
    print ('Your total amount due is:$',Total,'0')

# Create condition for %20:If tip enetered is %20 apply condition 3 and add
# sales tax, tip amount and meal cost to dosplay total.  
elif Tip_Percentage is 20:
    Tip_Amount= Condition_3
    print('Your tip amount is $', Condition_2,'0 with a %7 sales tax of $',Sales_Tax)
    Total= Amount_Charged + Tip_Amount + Sales_Tax
    print ('Your total amount due is:$',Total,'0')

# Creat condition for input outside of original parameters. 
else:
    print('Error!!! Choose from given choices')













        

















