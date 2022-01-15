import turtle as t
import random
tim=t.Turtle()
i=0
tim.speed("fastest")
t.colormode(255)
t.width(10)
def setcolor():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    set_color= (r,g,b)
    return set_color
while i<360:
    tim.circle(80,360)
    tim.color(setcolor())
    tim.left(i)
   # tim.circle(40,360)
    i+=1





screen=t.Screen()
screen.exitonclick()
