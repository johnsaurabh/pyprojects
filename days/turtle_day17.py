from turtle import Turtle, Screen
import random


tim=Turtle()
tim.shape("turtle")
#i=1
#while i<=6:
    #tim.forward(100)
    #im.right(72)
    #i=i+1

x=0
for x in range(0,7):
    sides=x+3

    angle = 360 / sides
    for i in range(sides):

        tim.forward(100)
        tim.right(angle)










myscreen=Screen()
myscreen.exitonclick()