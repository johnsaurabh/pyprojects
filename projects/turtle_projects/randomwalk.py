import turtle as t
import random

tim = t.Turtle()
t.colormode(255)


def setcolor():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    set_color= (r,g,b)
    return set_color


angles= [0,90,180,270]
tim.width(15)
tim.speed("fastest")
for _ in range(200):

    tim.color(setcolor())

    tim.forward(30)
    tim.setheading(random.choice(angles))





screen = t.Screen()
screen.exitonclick()
