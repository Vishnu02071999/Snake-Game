from turtle import *
import time
from Snake import *
from Food import Food
from Scoreboard import *

screen = Screen()
screen.setup(height=600, width=600)
screen.title("Snake game")
screen.bgcolor("Black")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

snake.create_snake()
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 17:

        # print("yum yum")
        food.refresh()
        snake.extend()
        score.increase_score()
    if snake.head.xcor() > 290 or snake.head.ycor() > 290 or snake.head.ycor() < -290 or snake.head.xcor() < -290:
        score.reset()
        snake.reset()



        for segment in snake.segments:
            if segment == snake.head:
                pass
            elif snake.head.distance(segment) < 10:
                score.reset()
                snake.reset()




screen.exitonclick()
