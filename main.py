
from random import choice, randint
import time
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
ball.move(choice([randint(0,45), randint(135,225), randint(290,360)]))

while game_is_on:

    screen.onkey(paddle2.up,'Up')
    screen.onkey(paddle2.down,'Down')
    screen.onkey(paddle1.up,'w')
    screen.onkey(paddle1.down,'s')
    ball.move(ball.heading())
    if ball.ycor()>= (HEIGHT/2-10) or ball.ycor()<= -(HEIGHT/2-10):
        ball.reflect_horizontal()
    elif paddle1.check_collision(ball):
        ball.reflect_vertical()
    elif paddle2.check_collision(ball):
        ball.reflect_vertical()
    elif ball.xcor()>= (WIDTH/2-10) or ball.xcor()<= -(WIDTH/2-10):
        game_is_on = False
    
    time.sleep(0.05)
    screen.update()




screen.exitonclick()
