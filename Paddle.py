
from multiprocessing.spawn import import_main_path
import time
from turtle import Turtle, forward
from typing import List
WIDTH = 1500
HEIGHT =  700


# STARTING_POSITIONS = [(-280,-40),(-280,-20),(-280,0),(-280,20),(-280,40)]

class Paddle():

        def __init__(self, STARTING_POSITIONS: List[tuple]) -> None:
                self.BOXES: List[Turtle] =[]
                self.STARTING_POSITIONS = STARTING_POSITIONS
                self.create_paddle()
                self.head = self.BOXES[-1]
                self.tail = self.BOXES[0]
                
                
        def create_box(self,position):
            box = Turtle('square')
            box.color('white')
            box.speed(0)
            box.pu()
            box.shapesize(stretch_len=1.5, stretch_wid=1.5)
            box.goto(position)
            self.BOXES.append(box)

        def create_paddle(self):
            for pos in self.STARTING_POSITIONS:
                self.create_box(pos)
                # time.sleep(1)

        
        def up(self):
            if not (self.head.ycor()>=(HEIGHT/2-50)):
                for box in self.BOXES:
                    box.setheading(90)
                    box.forward(100)
            
        def down(self):
            if not (self.tail.ycor()<=-(HEIGHT/2-50)):
                for box in self.BOXES:
                    box.setheading(270)
                    box.forward(100)


        def check_collision(self, ball: Turtle) -> bool:
            for box in self.BOXES:
                if box.distance(ball) <=40:
                    print("collision")
                    return True

                else:
                    # print("No Collision")
                    return False


        