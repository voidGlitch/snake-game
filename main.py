from turtle import Turtle,Screen, xcor
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard


screen =Screen()
screen.bgcolor("black")
screen.setup(width=600,height=600)
screen.title("snake Game")
screen.tracer(0) 


snake = Snake()
food = Food()
score = ScoreBoard()

screen.listen()
screen.onkey(snake.up , "Up")
screen.onkey(snake.down , "Down")
screen.onkey(snake.left , "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update() 
    time.sleep(0.1)  # delay the time for 1 sec and then resets the screen
    

    
    snake.move()
    #detect the collison with food
    if snake.head.distance(food) <15 :
        score.score()
        #extends after collison with food
        snake.extend()
        food.refresh()
        score.refresh()
        
    #detect the collison with wall
    if snake.head.xcor()>290 or snake.head.xcor()<-290 or snake.head.ycor()>290 or snake.head.ycor()<-290:
        game_is_on = False
        score.game_over()

    #detect the collison with its own body
    for segments in snake.segments[1:]:
    
        if snake.head.distance(segments) < 10:
            game_is_on=False
            score.game_over()
screen.exitonclick()