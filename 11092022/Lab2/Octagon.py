import turtle
import random

t = turtle.Turtle()
t.shape("turtle")

for indx in range(0, 8):
    t.forward(100)
    radom_color = random.choice(["Red", "Blue", "Yellow", "Green", "Purple","Orange"]) 
    t.pencolor(radom_color)
    t.right(45)

turtle.exitonclick()