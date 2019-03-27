# This program draws a shape using a nested loops.
# 3/14/2019
# CTI-110 P4HW4 - Nested Loops
# Walter Rutherford

def turtle():
    import turtle
    t = turtle.Turtle()
    t.pencolor('orange')
    t.speed(5)
    for x in range (10): 

        for i in range (2):
            t.forward(60)
            t.right(60)
            t.forward(100)
            t.right(120)
        t.right(36)
        if x %2 == 0:

            t.pencolor('blue')

        else:
            t.pencolor('orange')

    t.right(90)
    t.penup()

    t.forward (107)
    t.pendown ()
    t.forward (70)

    t.right (90)
    t.forward (100)
    t.left(90)
    t.forward (50)
    t.left (90)
    t.forward(100)
    t.forward (100)
    t.left(90)
    t.forward (50)
    t.left (90)
    t.forward (100)
turtle()






