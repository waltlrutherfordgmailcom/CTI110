# CTI-110 
# P3HW1 - Color Mixer program mixing three different colors 
# Walter Rutherford 
# Date: 2/12/2019


# Display introduction
# Get first primary color.
# Get second primary color.
# Create and display possible conditions for Blue and red.
# Create and display possible conditions for red and yellow.
# Create and display possible conditins for blue and yellow.
# Create and display condition for colors outside of the colors supplied.


# Print the intorduction for color combinations
print('Please enter a color combination using any three colors that are listed below:')

# Print the color choices.
print('\n              red            yellow              blue ')

# Create input for primary color number one.
Primary_color_1= input ('\nEnter the first primary color:')

# Create input for primary color two.
Primary_color_2= input ('\nEnter the second primary color:')




        
# Creat condition for the mixture of blue and red.
if Primary_color_1 == 'blue' and Primary_color_2 == 'red':
        print ('\n\n\n\n        The result is purple!')
# Create condition for red and blue.
elif Primary_color_1 == 'red' and Primary_color_2 == 'blue':
        print ('\n\n\n\n        The result is purple!')
# Create condition for red and yellow.
elif Primary_color_1 == 'red' and Primary_color_2 == 'yellow':
        print ('\n\n\n\n        The result is orange!')
# Create condition for yelow and red.
elif Primary_color_1 == 'yellow' and Primary_color_2 == 'red':
        print ('\n\n\n\n        The result is orange!')
# Create condition for blue and yellow.
elif Primary_color_1 == 'blue' and Primary_color_2 == 'yellow':
        print ('\n\n\n\n        The result is green!')
# Create condition for yellow and blue.
elif Primary_color_1 == 'yellow' and Primary_color_2 == 'blue':
        print ('\n\n\n\n        The result is green!')


# Creat condition for yellow both primary and secondary.
elif Primary_color_1 == 'yellow' and Primary_color_2 == 'yellow':
        print ('\n\n\n\n        The result is yellow!')
# Create condition for blue both primary and secondary.
elif Primary_color_1 == 'blue' and Primary_color_2 == 'blue':
        print ('\n\n\n\n        The result is blue!')
# Create condition for red both primary and secondary.
elif Primary_color_1 == 'red' and Primary_color_2 == 'red':
        print ('\n\n\n\n        The result is red!')

 
        
# Create final condition for any color outside of previous conditions
else:
        print("\n\n\n\n          Error!!! Enter colors specified!")






    


        
  

