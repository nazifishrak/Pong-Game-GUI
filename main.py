
from random import choice, randint
import time
from turtle import Turtle, Screen
from Ball import Ball

from Paddle import Paddle, HEIGHT, WIDTH
from Score import ScoreBoard

screen = Screen()
screen.setup(WIDTH,HEIGHT)
screen.listen()
screen.bgcolor('black')
screen.tracer(0)
score_l = ScoreBoard((-60,(HEIGHT/2)-120))
score_r = ScoreBoard((60,(HEIGHT/2)-120))
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

paddle1 = Paddle([(-(WIDTH/2 -20),-40),(-(WIDTH/2 -20),-20),(-(WIDTH/2 -20),0),(-(WIDTH/2 -20),20),(-(WIDTH/2 -20),40)])
paddle2 = Paddle([(WIDTH/2 -20,-40),(WIDTH/2 -20,-20),(WIDTH/2 -20,0),(WIDTH/2 -20,20),(WIDTH/2 -20,40)])

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
    elif ball.xcor()>= (WIDTH/2-10):
        score_l.increase_score()
        ball.goto((randint(-(WIDTH/2- WIDTH/4), (WIDTH/2- WIDTH/4))),randint(-(HEIGHT/2- HEIGHT/4), (HEIGHT/2- HEIGHT/4)))
        ball.move(choice([randint(0,45), randint(135,225), randint(290,360)]))
    elif ball.xcor()<= -(WIDTH/2-10):
        score_r.increase_score()
        ball.goto((randint(-(WIDTH/2- WIDTH/4), (WIDTH/2- WIDTH/4))),randint(-(HEIGHT/2- HEIGHT/4), (HEIGHT/2- HEIGHT/4)))
        ball.move(choice([randint(0,45), randint(135,225), randint(290,360)]))

    if score_l.score==10:
        score_l.game_over()
        game_is_on = False
    elif score_r.score ==10:
        score_r.game_over()
        game_is_on = False
    else:
        pass

    
    time.sleep(0.05)
    screen.update()




screen.exitonclick()
