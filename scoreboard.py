from turtle import Turtle

SCORE=0
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.goto(-20,260)
        self.color("white")
        self.refresh()

    def refresh(self):
        self.write(F"score ={SCORE} ",align="center",font=("arial",15,"normal"))   
    def game_over(self):
        self.goto(0,0)
        self.write(F"GAME OVER",align="center",font=("arial",15,"normal"))
    def score(self):
        global SCORE
        SCORE += 1
        self.clear()
        self.refresh()

