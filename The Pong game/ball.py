import random
from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__(shape="circle")
        self.color("white")
        self.speed(0)
        self.up()
        self.move_speed = 0.05

    def move(self):
        self.forward(5)

    def set_random_heading(self):
        self.setheading(random.randrange(0, 270))

    def bounce(self):
        self.setheading(self.heading() * -1)

    def paddle_bounce(self):
        self.setheading(self.heading() + random.randint(70, 150))
        if self.move_speed > 0.01:
            self.move_speed -= 0.01

    def reset(self):
        self.home()
        self.move_speed = 0.05
        self.set_random_heading()
