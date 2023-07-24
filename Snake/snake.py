from turtle import Turtle
from food import Eat
import numpy

STARTING_POSITIONS = [(0, 0), (-10, 0), (-20, 0)]

class Snake:
    def __init__(self):
        super().__init__()
        self.snake_array = []
        self.createSnake()
        
    def createSnake(self):
        self.snake_array = []
        for positions in STARTING_POSITIONS:
            block = Turtle()
            block.goto(positions)
            block.penup()
            block.color("white")
            block.shape("square")
            block.shapesize(1, 1, 1)
            
            self.snake_array.append(block)
        self.head = self.snake_array[0]
    
    def grow(self):
        for i in range(2):
            block = Turtle()
            block.penup()
            block.color("white")
            block.shape("square")
            block.shapesize(1, 1, 1)   
            self.snake_array.extend([block])
        self.move()
        self.head.forward(-10)
        
    def clearsnake(self):
        for i in range(0, len(self.snake_array)):
            self.snake_array[i].hideturtle()

    def wallcollision(self):
        xcor = self.head.xcor()
        ycor = self.head.ycor()
        if xcor <= -250 or xcor >= 250 or ycor <= -250 or ycor >= 250:
            return True
        return False
        


    def tailcollision(self):
        for i in range(1, len(self.snake_array)):
            if self.head.distance(self.snake_array[i]) <= 1:
                return True
        return False

             
    def move(self):
        for seg_num in range((len(self.snake_array) - 1), 0, -1):
            new_x = self.snake_array[seg_num - 1].xcor()
            new_y = self.snake_array[seg_num - 1].ycor()
            self.snake_array[seg_num].goto(new_x, new_y)
        self.snake_array[0].forward(10)

    
    def up(self):   
        if self.snake_array[0].heading() == 0:
            self.snake_array[0].left(90)
        elif self.snake_array[0].heading() == 180:
            self.snake_array[0].right(90)
    
    def down(self):
        if self.snake_array[0].heading() == 0:
            self.snake_array[0].right(90)
        elif self.snake_array[0].heading() == 180:
            self.snake_array[0].left(90)

    def left(self):
        if self.snake_array[0].heading() == 90:
            self.snake_array[0].left(90)
        elif self.snake_array[0].heading() == 270:
            self.snake_array[0].right(90)
    
    def right(self):
        if self.snake_array[0].heading() == 90:
            self.snake_array[0].right(90)
        elif self.snake_array[0].heading() == 270:
            self.snake_array[0].left(90)
        
        

        
    
        


