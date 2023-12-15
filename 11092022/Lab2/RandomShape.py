import turtle
import random

t = turtle.Turtle()
t.shape("turtle")

random_size = random.randint(0,9)
print(random_size)
for indx in range(0, random_size):
    t.forward(100)
    random_angle = random.randint(0,100)
    t.right(random_angle)

turtle.exitonclick()