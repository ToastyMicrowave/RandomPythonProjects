from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__(visible=False)
        self.up()
        self.color("white")
        self.paddle1_score = 0
        self.paddle2_score = 0
        self.scoreboard()

    def scoreboard(self):
        self.clear()
        self.goto(-100, 220)
        self.write(f"{self.paddle1_score}", False, "center", ("Elephant", 30, "bold"))
        self.goto(100, 220)
        self.write(f"{self.paddle2_score}", False, "center", ("Elephant", 30, "bold"))

    def update_paddle1_score(self):
        self.paddle1_score += 1
        self.scoreboard()

    def update_paddle2_score(self):
        self.paddle2_score += 1
        self.scoreboard()
