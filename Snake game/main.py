from time import sleep
from turtle import Screen
from food import Food
from scoreboard import ScoreBoard
from snake import Snake

game_is_on = True
screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)

snake = Snake()
snake.make_new_snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.left, "a")
screen.onkey(snake.down, "s")
screen.onkey(snake.right, "d")

while True:
    sleep(0.07)
    screen.update()
    snake.move()

    # Detect collision with food
    if snake.snake_head.distance(food) < 15:
        snake.add_tail_seg()
        scoreboard.increase_score()
        food.refresh()

    # Detect collision with walls
    if snake.snake_head.xcor() > 299 or snake.snake_head.ycor() > 299 or\
            snake.snake_head.xcor() < -299 or snake.snake_head.ycor() < -299:
        scoreboard.reset()
        snake.reset()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.snake_head.distance(segment) < 1:
            scoreboard.reset()
            snake.reset()


screen.exitonclick()
