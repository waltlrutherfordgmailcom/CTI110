# Meal and tip calculater: Creating a program that calculates the total
# amount of a meal purchased at a restaurant.
# 2/02/2019
# CTI-110 P2HW2 - Meal Tip Calculator
# Walter Rutherford

#Get the total amount of the meal.
#Calculate %15 of the total.
#Calculate total including first percentage.
#Display Both amounts.
#Calculate %18 of the total.
#Calculate total including second percentage.
#Display Both amounts.
#Calculate %18 of the total.
#Calculate total including second percentage.
#Display Both amounts.



# 1.Create input for the amount charged.
Amount_Charged= float(input('What is the cost of the meal?\n'))


# 2.Display introduction to tip amount by percentage.
print('Tip the server the following amounts according to the percentage:\n')




# 3.Find the tip amount by multiplying the amount of the meal by .15.
Tip_Amount= Amount_Charged* .15

# 4.Calculate total cost owed by adding meal coast and tip amount.
Total= Amount_Charged + Tip_Amount

# 5.Display the total amount owed including the tip amount.
print ('The total amount due with a %15 tip is: $',Total,'0')

# 6.Display the tip amount.
print('The value of the %15 tip is:  $', Tip_Amount,'0\n')




# 7.Find the tip amount by multiplying the amount of the meal by .18.
Tip_Amount= Amount_Charged* .18

# 8.Calculate total cost owed by adding meal coast and tip amount.
Total= Amount_Charged + Tip_Amount

# 9.Display the total amount owed including the tip amount
print ('The total amount due with a %18 tip is: $',Total,'0')

# 10.Display the tip amount.
print('The value of the %18 tip is:  $', Tip_Amount,'\n')



# 11.Find the tip amount by multiplying the amount of the meal by .20.
Tip_Amount= Amount_Charged* .20

# 12.Calculate total cost owed by adding meal coast and tip amount.
Total= Amount_Charged + Tip_Amount

# 13.Display the total amount owed including the tip amount. 
print ('The total amount due with a %20 tip is: $',Total,'0')

# 14.Display the tip amount.
print('The value of the %20 tip is:  $', Tip_Amount,'0\n')
















