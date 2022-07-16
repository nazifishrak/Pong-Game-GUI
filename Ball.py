from random import randint
import turtle
from Paddle import HEIGHT, WIDTH


class Ball(turtle.Turtle):
    def __init__(self, shape: str = 'circle' , visible: bool = True, color = 'white') -> None:
        super().__init__(shape, visible)
        self.pu()
        self.goto((randint(-(WIDTH/2- WIDTH/4), (WIDTH/2- WIDTH/4))),randint(-(HEIGHT/2- HEIGHT/4), (HEIGHT/2- HEIGHT/4)))        
        self.color(color)

    def move(self, angle: int):
        pass
        
    def reflect(self):
        pass

