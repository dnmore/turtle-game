from turtle import Turtle

STARTING_POSITION = (-280, 0)
MOVE_DISTANCE = 10
FINISH_LINE_X = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color('green')
        self.penup()
        self.go_to_start()

    def go_to_start(self):
        self.goto(STARTING_POSITION)

    def move(self):
        self.forward(MOVE_DISTANCE)

    def is_at_finish_line(self):
        if self.xcor() > FINISH_LINE_X:
            return True
        else:
            return False
