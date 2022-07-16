from random import randint
import turtle
from typing import List
from Paddle import HEIGHT, WIDTH


class Ball(turtle.Turtle):
    def __init__(self, shape: str = 'circle' , visible: bool = True, color = 'white') -> None:
        super().__init__(shape, visible)
        self.pu()
        self.goto((randint(-(WIDTH/2- WIDTH/4), (WIDTH/2- WIDTH/4))),randint(-(HEIGHT/2- HEIGHT/4), (HEIGHT/2- HEIGHT/4)))        
        self.color(color)
        self.speed(10)

    def move(self, angle: int):
        self.setheading(angle)
        self.forward(20)
        
    def reflect_horizontal(self):
        current_heading = self.heading()
        if (current_heading>0 and current_heading<=90) or (current_heading>270 and current_heading<360):
            self.setheading(360-current_heading)
        elif current_heading>90 and current_heading<=270:
            self.setheading(360-current_heading)
    
    def reflect_vertical(self):
        current_heading = self.heading()
        if current_heading>=0 and current_heading<=180:
            self.setheading(180-current_heading)
        elif current_heading>180 and current_heading<=360:
            self.setheading(540-current_heading)





        



