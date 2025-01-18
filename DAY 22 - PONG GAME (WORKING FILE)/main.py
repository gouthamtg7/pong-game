from SetupGame import Create_game
from turtle import Turtle,Screen
from StartGame import Start_Game
from Score import Score
import random
screen = Screen()

game_over=False
create_game = Create_game()
score = Score()
start_game = Start_Game()
create_game.create_screen()

screen.update()
create_game.create_paddles()
screen.update()
screen.listen()
screen.onkeypress(key="Up", fun=create_game.forward1)
screen.onkeypress(key="Q".lower(), fun=create_game.forward2)
screen.onkeypress(key="Down", fun=create_game.backward1)
screen.onkeypress(key="A".lower(), fun=create_game.backward2)
game_over = False
screen.tracer(1)
start_game.c=False
while(game_over==False):
    start_game.move_ball()
    if start_game.ball.ycor()>240 or start_game.ball.ycor()<-240:
        start_game.bounce_ball()
    start_game.c = start_game.check_for_collision_with_paddle1(create_game, score)
    start_game.c = start_game.check_for_collision_with_paddle2(create_game, score)
    if start_game.c==True:
        continue
    if start_game.collision_with_wall()==True:
        score.game.write(arg="Game Over", align="Center", font=("Arial", 20, "normal"))
    if score.Score1 > 2 or score.Score2 > 2:
        start_game.ball.speed(2)
screen.exitonclick()



























