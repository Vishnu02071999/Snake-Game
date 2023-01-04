from turtle import *
starting_cordinates = [(-20, 0), (-40, 0), (-60, 0)]
move_dist = 20
up = 90
down = 270
left = 180
right = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for points in starting_cordinates:
            self.add_segments(points)

    def add_segments(self, points):
        new_turtle = Turtle()
        new_turtle.shape("square")
        new_turtle.shapesize(1, 1)
        new_turtle.color("White")
        new_turtle.penup()
        new_turtle.goto(points)
        self.segments.append(new_turtle)

    def reset(self):
        for segm in self.segments:
            segm.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def extend(self):
        self.add_segments(self.segments[-1].position())

    def move(self):
        for segnum in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[segnum - 1].xcor()
            new_y = self.segments[segnum - 1].ycor()
            self.segments[segnum].goto(new_x, new_y)
        self.head.forward(move_dist)

    def up(self):
        if self.head.heading() != down:
            self.head.setheading(up)

    def down(self):
        if self.head.heading() != up:
            self.head.setheading(down)

    def left(self):
        if self.head.heading() != right:
            self.head.setheading(left)

    def right(self):
        if self.head.heading() != left:
            self.head.setheading(right)


