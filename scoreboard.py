from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.setpos(200,260)
        self.score = 0
        self.life = 3
        self.write(f"Life : {self.life} | Score : {self.score}", align="center", font=("Arial",14,"normal"))

    def change_score_life(self):
        self.clear()
        self.write(f"Life : {self.life} | Score : {self.score}", align="center", font=("Arial",14,"normal"))

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over", align="center", font=("Arial", 14, "normal"))

    def game_win(self):
        self.goto(0,0)
        self.write("You win!!", align="center", font=("Arial", 14, "normal"))