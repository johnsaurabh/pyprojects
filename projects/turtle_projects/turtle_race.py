import turtle as t
import random
turtle_names= ["tim","holly","jim","monty","manny","tommy"]
colors=["red","orange","yellow","green","blue","purple"]
screen=t.Screen()
is_race_on=False
screen.setup(width=500,height=400)
user_bet=screen.textinput(title="Make your bet", prompt="Who will win the race? Name a color")
#a=-240
b=160
for i in range (len(turtle_names)):
    turtle_names[i]=t.Turtle(shape="turtle")
    turtle_names[i].color(colors[i])
    turtle_names[i].penup()
    turtle_names[i].goto(x=-230, y=b)
    b-=60
if user_bet:
    is_race_on=True
while is_race_on:

    for turtle in turtle_names:
        if turtle.xcor()>230:
            is_race_on=False
            winning_color=turtle.pencolor()
            if user_bet==winning_color:
                print(f"You won! {winning_color} won the race")
            else:
                print(f"You lose! {winning_color} won the race")

        turtle.forward(random.randint(0,10))













screen.exitonclick()