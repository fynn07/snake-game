from turtle import Screen
from turtle import Turtle
from playsound import playsound
from scoreboard import Score
from snake import Snake
from food import Eat
import time

def reset():
    snake.createSnake()
    scoreboard.score = 0
    scoreboard.scoreit()
    food.showturtle()
    
#Specifications
screen = Screen()
screen.setup(width=500, height=500)
screen.bgcolor("black")
screen.title("Snake! by Fynn")
screen.tracer(0)

playsound('Snake\soundtracks\music_track.mp3', False)
snake = Snake()
food = Eat()
scoreboard = Score()
speed_snake = 0.06

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

#Main
game_is_on = True
holder = False
while game_is_on: 

    if holder:
        speed_snake = 0.06
        snake.clearsnake()
        food.clear()
        scoreboard.gameover()
        screen.listen()
        screen.onkey(reset, "1")
        holder = False   
       
    time.sleep(speed_snake)
    snake.move()  
    screen.update()

    if snake.wallcollision():
        holder = True

    if snake.tailcollision():
        holder = True

    if snake.head.distance(food) < 15:
        n = playsound('Snake\soundtracks\sound_effect_1.mp3', False)
        snake.grow()
        food.move_random()
        if scoreboard.score <= 15:
            speed_snake -= 0.002
        else:
            speed_snake -= 0.0005
        scoreboard.score += 1
        scoreboard.scoreit() 
    
screen.exitonclick()
