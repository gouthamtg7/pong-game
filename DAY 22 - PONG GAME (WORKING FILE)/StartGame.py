from turtle import Turtle,Screen
import random, time
from SetupGame import Create_game
from Score import Score
#Create a ball to play with ✅
#Create its movement from one end to another ✅
#Make it bounce on the middle floor ✅
#Detect collision with the paddle
#Movement after collision
score = Score()
create_game = Create_game()
class Start_Game:
    def __init__(self):
        self.ball = Turtle()
        self.ball = Turtle("circle")
        self.ball.color("blue")
        self.ball.penup()
        self.ball.speed(1)
        self.pos = []
        self.k = 0
        self.c = False
        self.dx = 10
        self.dy = 10


    def check_for_collision_with_paddle1(self,create_game,score):
        if self.ball.xcor() <= create_game.paddle1.xcor() + 10 and self.ball.xcor() >= create_game.paddle1.xcor() - 10:
            if self.ball.distance(create_game.paddle1.xcor(), create_game.paddle1.ycor()) <= 50:
                self.dx*=(-1)
                self.move_ball()
                score.score2.clear()
                score.Score2 += 1
                score.display_score()
                self.k += 1
                return True
            elif self.ball.distance(create_game.paddle2.xcor(), create_game.paddle2.ycor()) > 50:
                return False


    def check_for_collision_with_paddle2(self,create_game,score):
        if self.ball.xcor() <= create_game.paddle2.xcor() + 10 and self.ball.xcor() >= create_game.paddle2.xcor() - 10:
            if self.ball.distance(create_game.paddle2.xcor(), create_game.paddle2.ycor()) <= 50:
                self.dx *= (-1)
                self.move_ball()
                score.Score1 += 1
                score.display_score()
                self.k += 1
                return True
            elif self.ball.distance(create_game.paddle2.xcor(), create_game.paddle2.ycor()) > 50:
                return False





    def collision_with_wall(self):
        if self.ball.xcor() >= 380 or self.ball.xcor() <= -380:
            return True

    def move_ball(self):
        self.new_x = (self.ball.xcor() + self.dx)  # dx is the change in x direction
        self.new_y = (self.ball.ycor() + self.dy)  # dy is the change in y direction
        self.ball.goto(self.new_x,self.new_y)
    def bounce_ball(self):
        self.dy*=(-1)






















