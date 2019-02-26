#This program displays a table of lbs to kgs, with a step value of 10. 



# Create function
# display labels
# Creat for loop
# Disolay pounds and kilograms




# Function
def Pounds_Conversian():

    # Print labels
    print ('Pounds\tKilograms')
    print('_____________________')

    # For loop 100 to 300 in incraments of 10. 
    for Pounds in range(100,301,10):

                # Variable equation for kilograms
                Kilograms = Pounds / 2.2046

                # Printed results
                print('\n',Pounds,'\t',format(Kilograms,'.4f'))

Pounds_Conversian()
        
            










        




