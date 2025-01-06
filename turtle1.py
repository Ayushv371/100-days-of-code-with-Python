import turtle
import random


# Function to draw shapes connected from the same point
def draw_shape(side):
    angle = 360 / side
    turtle.color(random.random(), random.random(), random.random())
    for _ in range(side):
        turtle.forward(50)
        turtle.left(angle)


turtle.speed(3)

for sides in range(3, 11):
    draw_shape(sides)

turtle.exitonclick()
