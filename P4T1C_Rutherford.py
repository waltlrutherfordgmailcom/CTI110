# This program draws a snowflake using a nested loop.
# 3/14/2019
# CTI-110 Bonus Lab:P4T1C - Snowflake 
# Walter Rutherford

import turtle
t = turtle.Turtle()

def stick ():
    for x in range (3):
        for x in range (1):
            t.forward (30)
            t.right(45)
            t.forward(30)
            t.backward(30)
            t.left(45)
        t.left(45)
        t.forward (30)
        t.backward (30)
        t.right (45)

for x in range (8):
    t.backward (90)
    t.right (45)
    stick ()
        
        


        
    
