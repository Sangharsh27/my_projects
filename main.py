from turtle import Turtle, Screen
import random


def colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colours = (r, g, b)
    return colours


tim = Turtle()


tim.pensize(30)
Screen().colormode(255)
i = 0
tim.penup()
tim.shape("turtle")
tim.speed("fastest")


tim.setposition(-200, -200)
while tim.xcor() != 300 and tim.ycor() != 300:
    i = 0
    tim.setheading(0)
    for i in range(10):
        j = random.randint(0, 9)
        tim.dot(25, colour())

        tim.forward(50)
        tim.color(colour())

        i += 1
        

        if tim.xcor() == 300:
            tim.left(90)
            tim.fd(50)

            tim.setposition(-200, tim.ycor())

Screen().exitonclick()
