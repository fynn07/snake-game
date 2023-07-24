from turtle import Turtle
import random 

class Eat(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("red")
        self.shapesize(0.5, 0.5)
        self.speed("fastest")
        self.move_random()
    
    def move_random(self):
        rand_x = random.randrange(-240, 240, 10)
        rand_y = random.randrange(-240, 240, 10)
        self.setpos(rand_x, rand_y)
    
    def clear(self):
        self.hideturtle()