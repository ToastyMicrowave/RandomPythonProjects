from pathlib import Path
from turtle import Turtle
FONT = ("Elephant", 16)
ALIGNMENT = "center"
HIGHSCORE_FILE = Path(__file__).parent / "highscore.txt"


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.up()
        self.color("white")
        self.hideturtle()
        self.score = 0
        with open(HIGHSCORE_FILE) as highscore_file:
            self.highscore = int(highscore_file.readline())
        self.update_scoreboard()

    def reset(self):
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open(HIGHSCORE_FILE, "w") as highscore_file:
                highscore_file.write(f"{self.highscore}")
        self.clear()
        self.goto(0, 270)
        self.write(arg=f"Score = {self.score}, High Score = {self.highscore}",
                   move=False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
