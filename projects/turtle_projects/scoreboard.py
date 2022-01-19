from turtle import Turtle
import random
FONT=("Arial", 24, "normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.penup()
        self.color("white")
        #self.write(f"The score is {self.score}",False, font=FONT)
        self.hideturtle()
        self.goto(0,260)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"The score is {self.score}",align="center", font=FONT)
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align= "center", font=FONT)

    def increase_score(self):
        self.score+=1
        self.clear()
        self.update_scoreboard()

