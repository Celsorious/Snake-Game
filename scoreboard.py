from turtle import Turtle

ALIGN = "center"
FONT = ('Arial', 12, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.position_x = 0
        self.position_y = 280
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(self.position_x, self.position_y)
        self.score = 0
        self.write(f"Scoreboard: {self.score}", align = ALIGN, font = FONT)
    def refresh_score(self):
        self.score += 1
        self.clear()
        self.write(f"Scoreboard: {self.score}", align = ALIGN, font = FONT)
    
    def game_over(self):
        self.position_x = 0
        self.position_y = 0
        self.goto(self.position_x, self.position_y)
        self.write("GAME OVER", align = ALIGN, font = FONT)
