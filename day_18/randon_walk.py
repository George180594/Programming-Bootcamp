import turtle as t
import random

tim=t.Turtle()

colors = [
    "white", "black", "red", "green", "blue", "yellow", "cyan", 
    "magenta", "orange", "pink", "purple", "brown", "gray", 
    "lightgreen", "lightblue", "darkgreen", "darkblue", "gold", 
    "silver", "violet", "indigo"
]

directions= [0,90,180,270]
for _ in range(30):
    tim.setheading(180)
    tim.penup()
    tim.forward(30)
    tim.pendown()
    tim.color(random.choice(colors))
    tim.pensize(10)
    tim.penup()
    tim.forward(30)
    tim.pendown()
    tim.dot()
    