from turtle import Turtle
MOVE_DISTANCE = 20

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def make_new_snake(self, length=3):
        self.segments = []
        self.add_snake_segs(length)
        self.snake_head = self.segments[0]

    def add_snake_segs(self, length, x=0, y=0):
        for _ in range(length):
            snake_seg = Turtle(shape="square")
            snake_seg.up()
            snake_seg.color("white")
            snake_seg.goto(x, y)
            x -= 20
            self.segments.append(snake_seg)

    def add_tail_seg(self):
        x = self.segments[-1].xcor()
        y = self.segments[-1].ycor()
        self.add_snake_segs(length=1, x=x, y=y)

    def reset(self):
        for seg in self.segments:
            seg.reset()
        self.make_new_snake()

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x_coord = self.segments[seg_num - 1].xcor()
            new_y_coord = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x_coord, new_y_coord)
        self.snake_head.forward(MOVE_DISTANCE)

    def up(self):
        if self.snake_head.heading() != DOWN:
            self.snake_head.setheading(UP)

    def down(self):
        if self.snake_head.heading() != UP:
            self.snake_head.setheading(DOWN)

    def left(self):
        if self.snake_head.heading() != RIGHT:
            self.snake_head.setheading(LEFT)

    def right(self):
        if self.snake_head.heading() != LEFT:
            self.snake_head.setheading(RIGHT)
