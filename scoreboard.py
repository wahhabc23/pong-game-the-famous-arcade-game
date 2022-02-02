from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color('white')
        self.l_score = 0
        self.r_score = 0
        self.update()

    def update(self):
        self.clear()
        self.goto(-100, 240)
        self.write(f"{self.l_score}", align='center',
                   font=['Arial', 40, 'normal'])
        self.goto(100, 240)
        self.write(f"{self.r_score}", align='right',
                   font=['Arial', 40, 'normal'])
