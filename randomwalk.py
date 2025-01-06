import turtle as t
import random

tim = t.Turtle()

tim.pensize(15)
tim.speed("fastest")

angles = [0, 90, 180, 270]

for _ in range(200):
    tim.color(random.random(), random.random(), random.random())
    tim.forward(30)
    tim.setheading(random.choice(angles))

t.exitonclick()