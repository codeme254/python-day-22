from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.speed("fast")
        self.penup()
        self.x_move = 10
        self.y_move = 15
    
    def reset_ball(self):
        self.goto(0, 0)
        self.paddle_bounce()
        
    def move(self):
        new_y = self.ycor() + self.y_move
        new_x = self.xcor() + self.x_move
        self.goto(new_x, new_y)

    def bounce(self):
        self.y_move *= -1
    
    def paddle_bounce(self):
        self.x_move *= -1