from turtle import Turtle

class Paddle(Turtle):
    """Create a gaming paddle.
    Provide 'left' argument to create a paddle on the left side,
    or 'right' to create a paddle on the right side"""
    def __init__(self, starting_position):
        super().__init__()
        self.shape('square')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.color('white')

        if starting_position == 'left':
            self.goto(-350, 0)
        elif starting_position == 'right':
            self.goto(350, 0)
        else:
            raise ValueError(f"Invalid starting_position '{starting_position}'. Use 'left' or 'right'.")

    def go_up(self):
        current_ycor = self.ycor()
        if self.ycor() < 250:
            new_ycor = current_ycor + 20
            self.goto(self.xcor(), new_ycor)

    def go_down(self):
        current_ycor = self.ycor()
        if self.ycor() > -250:
            new_ycor = current_ycor - 20
            self.goto(self.xcor(), new_ycor)