import turtle

# Create canvas instance
my_turtle = turtle.Turtle()

# Start at certain coordinate
my_turtle.penup()
my_turtle.goto(50, 75)

# Draw the line
my_turtle.pendown()
my_turtle.forward(100)
my_turtle.left(90)
my_turtle.forward(200)
my_turtle.left(90)
my_turtle.forward(100)
my_turtle.left(90)
my_turtle.forward(200)

turtle.done()
