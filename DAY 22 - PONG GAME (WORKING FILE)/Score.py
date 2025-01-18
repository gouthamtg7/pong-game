from turtle import Turtle,Screen
class Score:
    def __init__(self):
        self.Score1 = 0
        self.Score2 = 0
        self.score1 = Turtle()
        self.score2 = Turtle()
        self.score1.color("Orange")
        self.score2.color("Orange")
        self.score1.penup()
        self.score2.penup()
        self.score1.goto(50,270)
        self.score2.goto(-50, 270)
        self.score1.hideturtle()
        self.score2.hideturtle()
        self.display_score()
        self.game = Turtle()
        self.game.color("Orange")
        self.game.penup()
        self.game.hideturtle()

    def display_score(self):
        self.score1.write(f"{self.Score1}",align="left", font=("Arial", 20, "normal"))
        self.score2.write(f"{self.Score2}", align="right", font=("Arial", 20, "normal"))



