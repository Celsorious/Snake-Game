from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40,0)]
MOVE_DISTANCE = 20
class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
    
    def add_segment(self, position):
        new_segment = Turtle()
        new_segment.shape("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)
    
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def move(self):
        for num_segment in range (len(self.segments) -1, 0, -1):
            new_position_x = self.segments[num_segment -1].xcor()
            new_position_y = self.segments[num_segment -1].ycor()
            self.segments[num_segment].goto(new_position_x, new_position_y)
        self.segments[0].forward(MOVE_DISTANCE)
    def extend(self):
        """ Add a new segment to the snake"""
        self.add_segment(self.segments[len(self.segments) -1].position())

    def up(self):
        if self.segments[0].heading() != 270:
            self.segments[0].setheading(90)

    def down(self):
        if self.segments[0].heading() != 90:
            self.segments[0].setheading(270)

    def right(self):
        if self.segments[0].heading() != 180:
            self.segments[0].setheading(0)
            
    def left(self):
        if self.segments[0].heading() != 0:
            self.segments[0].setheading(180)



