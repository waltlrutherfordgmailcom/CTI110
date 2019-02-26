# This program displays a table of lbs to kgs, with a step value of 10. 
# 2/26/2019
# CTI-110 P4HW2 - Pounds to Kilos Table
# Rutherford, Walter


# Create function
# Display labels
# Creat for loop
# Disolay pounds and kilograms




# Beginning of function
def Pounds_Conversian():

    # Print labels
    print ('Pounds\t Kilograms')
    print('_____________________')

    # For loop 100 to 300 in incraments of 10. 
    for Pounds in range(100,301,10):

                # Variable equation for kilograms
                Kilograms = Pounds / 2.2046

                # Printed results
                print('\n',Pounds,'\t',format(Kilograms,'.4f'))

# End of function
Pounds_Conversian()
        
            










        




