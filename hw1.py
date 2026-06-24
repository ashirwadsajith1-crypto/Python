import turtle
turtle.Screen().bgcolor("yellow")
turtle.Screen().setup(500,300)
polygon=turtle.Turtle()
sidelength=5
number_of_sides=4
angle=90
for i in range(number_of_sides):
    polygon.forward(sidelength)
    polygon.right(angle)
turtle.done()