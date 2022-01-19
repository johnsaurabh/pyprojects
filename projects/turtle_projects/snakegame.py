
import random
import turtle as t
import time
from snake import Snake
from snakefood import Food
from scoreboard import Scoreboard
screen= t.Screen()
screen.tracer(0)
screen.bgcolor("black")
screen.setup(width= 600, height= 600)
screen.title("My snake game")

snake=Snake()

#snake.create_snake()
screen.update()

screen.tracer(0)
#is_game_on=False


is_game_on=True
s_food=Food()
s_scoreboard=Scoreboard()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left, "Left")

screen.onkey(snake.right, "Right")

while is_game_on:

    screen.update()
    time.sleep(0.1)
    if snake.head.distance(s_food)<15:
        s_food.create_food()
        s_scoreboard.increase_score()
        snake.grow_snake()
    if snake.head.xcor()<-290 or snake.head.xcor()> 290 or snake.head.ycor()> 290 or snake.head.ycor()< -290:
        is_game_on=False
        s_scoreboard.game_over()
    for x in snake.segments[1:]:

        if snake.head.distance(x)<10:
            is_game_on = False
            s_scoreboard.game_over()

    snake.move_snake()



screen.exitonclick()