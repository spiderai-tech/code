import turtle
import math
import time

s = turtle.Screen()
s.bgcolor("black")
s.setup(800, 700)
s.tracer(0)

t = turtle.Turtle(visible=False)
t.penup()
t.color("#ffb6c1")

for scale in range(11, 17):
    for i in range(120):
        a = i * math.pi / 60
        x = 16 * math.sin(a) ** 3 * scale
        y = (13 * math.cos(a) - 5 * math.cos(2*a)
             - 2 * math.cos(3*a) - math.cos(4*a)) * scale
        t.goto(x, y)
        t.write("I love you", align="center",
                font=("Arial", 8, "bold"))
        s.update()
        time.sleep(0.03)

turtle.done()

