import turtle
turtle.Screen().bgcolor("yellow")
turtle.Screen().setup(500,300)
polygon=turtle.Turtle()
sidelength=0.1
number_of_sides=10**3
angle=360/number_of_sides
for i in range(number_of_sides):
    polygon.forward(sidelength)
    polygon.right(angle)
turtle.done()

