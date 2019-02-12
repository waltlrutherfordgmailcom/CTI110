# This program determines the difference between the area of 2 rectangles.
# Date: 2/12/2019
# CTI-110 P2HW1 - Pounds to Kilograms Converter
# Walter, Rutherford

#Get the length of the first rectangle
#Get the width of the first rectangle
#Define the area of the first rectange
#Get the length of the second rectangle
#Get the width of the second rectangle
#Define the area of the second rectangle
#Display the differance between Rectangles one and two using Logical operators.

Length_of_rectangle_1 = int(input('What is the length of the first rectangle in inches?'))

Width_of_rectangle_1 = int(input('What is the the width in inches?'))

Area_1= Length_of_rectangle_1 * Width_of_rectangle_1


Length_of_rectangle_2 = int(input('\nWhat is the length of the second rectangle in inches?'))

Width_of_rectangle_2 = int(input('What is the the width in inches?'))

Area_2=Length_of_rectangle_2 * Width_of_rectangle_2


if Area_2 > Area_1:
    print("The second rectangle has the bigger area!")

elif Area_2 < Area_1:
        print("The first rectangle has the bigger area!")
else:
    if Area_2 == Area_1:
        print("\nThe area of both rectangles is equal!")
    










         

        
    
