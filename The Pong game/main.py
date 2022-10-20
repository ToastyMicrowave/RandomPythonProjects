from turtle import Screen
from pyautogui import sleep
from ball import Ball
from paddle import Paddle
from scoreboard import ScoreBoard

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800
screen = Screen()
screen.title("Pong!")
screen.bgcolor("black")
screen.setup(height=SCREEN_HEIGHT, width=SCREEN_WIDTH)
screen.tracer(0)

paddle1 = Paddle(-(SCREEN_WIDTH // 2 - 50))
paddle2 = Paddle(SCREEN_WIDTH // 2 - 50)
ball = Ball()
score_board = ScoreBoard()
paddles = [paddle1, paddle2]

screen.listen()
screen.onkeypress(paddle1.up, "w")
screen.onkeypress(paddle2.up, "Up")
screen.onkeypress(paddle1.down, "s")
screen.onkeypress(paddle2.down, "Down")

ball.set_random_heading()

while True:
    sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with top or botton walls
    if ball.ycor() >= SCREEN_HEIGHT // 2 - 20 or ball.ycor() <= -(SCREEN_HEIGHT // 2 - 20):
        ball.bounce()

    # Detect collision with paddles
    for paddle in paddles:
        if ball.distance(paddle) < 50\
           and (ball.xcor() >= SCREEN_WIDTH // 2 - 70
           or ball.xcor() <= -(SCREEN_WIDTH // 2 - 70)):
            ball.paddle_bounce()
            print(ball.move_speed)

    # Detect if paddles missed
    if ball.xcor() > SCREEN_WIDTH // 2:
        score_board.update_paddle1_score()
        ball.reset()
    elif ball.xcor() < -(SCREEN_WIDTH // 2):
        score_board.update_paddle2_score()
        ball.reset()

screen.exitonclick()
