import turtle as t
import random
tim=t.Turtle()
screen= t.Screen()
def mv_forward():
    tim.forward(10)
def mv_backward():
    tim.backward(10)

def mv_left():
    tim.left(10)

def mv_right():
    tim.right(10)

def draw_circle():
    tim.circle(60,20)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(key="w", fun=mv_forward)
screen.onkey(key="s", fun=mv_backward)
screen.onkey(key="a", fun=mv_left)
screen.onkey(key="d", fun= mv_right)
screen.onkey(key="r", fun=draw_circle)
screen.onkey(key="c", fun=clear)














screen.exitonclick()
