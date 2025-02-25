from turtle import Screen
from snake import Snake
import time
from food import Food
from scoreboard import Scoreboard

screen= Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake=Snake()
food=Food()
scoreboard=Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_is_on= True
while game_is_on:
    score=0
    screen.update()
    time.sleep(0.1)
    snake.move()
    #detect coolision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
    #Detected colision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor()>280 or snake.head.ycor() < -280: 
        game_is_on=False
        scoreboard.game_over()
    #detected colision with tail.'
    for segment in snake.segments[1:]:

        if snake.head.distance(segment) <  10:
            game_is_on=False
            scoreboard.game_over()
    #if head collides with any segment in the tail:
        #trigger game_over


        





screen.exitonclick()