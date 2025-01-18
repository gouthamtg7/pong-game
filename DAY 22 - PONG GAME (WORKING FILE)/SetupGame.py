from turtle import Turtle, Screen
import random
screen = Screen()
screen.screensize(canvwidth=750, canvheight=500, bg="black")
screen.tracer(0)


class Create_game():

    def __init__(self):
        self.q = 0
        self.k = 0
        self.lines = Turtle()
        self.mid_line = Turtle()
        self.boundary_properties()
        self.paddle_limit = 230

    def boundary_properties(self):
        self.lines.width(2)
        self.lines.color("white")
        self.lines.hideturtle()
        self.mid_line.hideturtle()
        self.mid_line.color("white")

    def create_screen(self):
        self.lines.teleport(-375, -250)
        self.lines.goto(-375, 250)
        self.lines.goto(375, 250)
        self.lines.goto(375, -250)
        self.lines.goto(-375, -250)
        self.mid_line.setheading(90)
        self.mid_line.teleport(0, -250)
        self.mid_line.color("white")
        for i in range(100, 0, -1):
            if self.mid_line.ycor() < -250 or self.mid_line.ycor() > 250:
                break
            else:
                if i % 2 == 0:
                    self.mid_line.pendown()
                    self.mid_line.forward(20)
                else:
                    self.mid_line.penup()
                    self.mid_line.forward(20)

    def create_paddles(self):
        self.paddle1 = Turtle("square")
        self.paddle2 = Turtle("square")
        self.paddle1.color("white")
        self.paddle2.color("white")
        self.paddle1.shapesize(stretch_len=3,stretch_wid=1)
        self.paddle1.penup()
        self.paddle1.goto(-365,0)
        self.paddle2.shapesize(stretch_len=3, stretch_wid=1)
        self.paddle2.penup()
        self.paddle2.goto(365, 0)
        self.paddle1.setheading(90)
        self.paddle2.setheading(90)


    def forward1(self):
        screen.tracer(0)
        self.paddle1.forward(20)
        screen.update()
        screen.tracer(1)

    def forward2(self):
        screen.tracer(0)
        self.paddle2.forward(20)
        screen.update()
        screen.tracer(1)


    def backward1(self):
        screen.tracer(0)
        self.paddle1.backward(20)
        screen.update()
        screen.tracer(1)

    def backward2(self):
        screen.tracer(0)
        self.paddle2.backward(20)
        screen.update()
        screen.tracer(1)







