
from turtle import Turtle, Screen
from Ball import Ball

from Paddle import Paddle, HEIGHT, WIDTH

screen = Screen()
screen.setup(WIDTH,HEIGHT)
screen.listen()
screen.bgcolor('black')
screen.tracer(0)
game_is_on = True 

def create_middle_line(len):
    middle_line = Turtle('square')
    middle_line.speed(0)
    middle_line.color('white')
    middle_line.pensize(10)
    middle_line.pu()
    middle_line.goto((0,-HEIGHT+30))
    middle_line.setheading(90)
    for i in range(int(HEIGHT/len)):
        middle_line.pd()
        middle_line.forward(len)
        middle_line.pu()
        middle_line.forward(len)

create_middle_line(50)

paddle1 = Paddle([(-(WIDTH/2 -40),-40),(-(WIDTH/2 -40),-20),(-(WIDTH/2 -40),0),(-(WIDTH/2 -40),20),(-(WIDTH/2 -40),40)])
paddle2 = Paddle([(WIDTH/2 -40,-40),(WIDTH/2 -40,-20),(WIDTH/2 -40,0),(WIDTH/2 -40,20),(WIDTH/2 -40,40)])

screen.update()
ball = Ball()
while game_is_on:
    screen.onkey(paddle1.up,'Up')
    screen.onkey(paddle1.down,'Down')
    screen.onkey(paddle2.up,'w')
    screen.onkey(paddle2.down,'s')
    screen.update()

screen.exitonclick()
