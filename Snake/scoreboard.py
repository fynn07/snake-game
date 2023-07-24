from turtle import Turtle
import time

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = 0
        self.hideturtle()
        self.penup()
        self.color("White")
        self.goto(0, 200)
        self.scoreit()    

    def scoreit(self):
        self.clear()
        self.goto(0, 200)
        self.write(f"Score = {self.score}", False, 'center', ('Arial', 23, 'bold'))
    
    def gameover(self):
        self.clear()
        self.setpos(0, 0)
        self.write(f"press 1 to play again", False, 'center', ('Arial', 23, 'bold'))



       
        