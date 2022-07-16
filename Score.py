


from turtle import Turtle
FONT = ('Courier', 80, "bold")
ALIGN = 'center'
class ScoreBoard(Turtle):
    def __init__(self, pos :tuple) -> None:
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color('white')
        self.goto(pos)
        self.write(f'{self.score}',align = ALIGN, font = FONT)

    def increase_score(self):
        self.clear()
        self.score +=1
        self.write(f'{self.score}',align= ALIGN, font = FONT)

    def game_over(self):
        self.goto(0,0)
        self.color('red')
        self.write("GAME OVER", align= ALIGN, font = FONT)
        

