import random
from turtle import Turtle
import time
class Food(Turtle):
    def __init__(self):
        super().__init__()
        #self.f=t.Turtle(shape="circle")
        self.shape("circle")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("red")
        self.create_food()

    def create_food(self):
        self.penup()
        x_new= random.randint(-250, 250)
        y_new=random.randint(-250,250)
        self.speed("fastest")
        self.goto(x_new,y_new)

