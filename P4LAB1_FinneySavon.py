# Savon Finney

# P4LAB1

# 3/17/2026

#  Making a drawing using loops for a house

import turtle



# Create the turtle drawing object

Theater = turtle.Screen()

Gamera = turtle.Turtle()

Theater.bgcolor("Light Blue")

Gamera.color("Green", "Dark Red")

Gamera.begin_fill()

# Creating a for loop to draw the house(4 times because it is a square)

for Walk in range(4):
    
    Gamera.forward(300)
    Gamera.right(90)
    
    
Gamera.end_fill()
turtle.done

# Drawing the roof for the house

Gamera.color("Blue", "Yellow")

Gamera.begin_fill()

for Walk in range(3):
    
    Gamera.forward(300)
    Gamera.left(120)
    
    
    

Gamera.end_fill()
turtle.done



Theater.mainloop()


