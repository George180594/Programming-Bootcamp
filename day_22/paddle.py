from turtle import Screen, Turtle

POSITION_1=(-350,0)
POSITION_2=(350,0)
MOVE_DISTANCE=20
UP=90
DOWN=270

class Paddle(Turtle):
    def __init__(self,*postion):
        super().__init__()
        self.shape("square")
        self.color('white')
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.penup()
        self.goto(postion)
        # self.go_up(self)
        # self.go_down(self)


    def go_up(self):
        new_y= self.ycor() +20
        self.goto(self.xcor(),new_y)       

    def go_down(self):
        new_y= self.ycor() -20
        self.goto(self.xcor(),new_y)     




