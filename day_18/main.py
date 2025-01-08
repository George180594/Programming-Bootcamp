import turtle as t
from turtle import Screen
tim=t.Turtle()

def draw_shape(num_sides):
    angle=360/num_sides
    for _ in range (num_sides):
        tim.forward(100)
        tim.right(angle)
for shape_side_n in range(3,11):
    draw_shape(shape_side_n)

# tim.color('red')
# tim.shape("turtle")
# for _ in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

# tim.right(90)
# tim.forward(100)
# tim.right(90)
# # tim.dot(5)
# tim.forward(100)

















screen=Screen()
screen.exitonclick()