import turtle
import random
import math
import time

# Screen setup
screen = turtle.Screen()
screen.setup(900, 800)
screen.bgcolor("#050509")
screen.title("PINK BLOSSOM TREE")
screen.tracer(0)

t = turtle.Turtle()
t.hideturtle()
t.speed(0)

random.seed(15)

# Pink flower colors
flower_colors = [
    "#ff1493",
    "#ff69b4",
    "#ff85b3",
    "#ffc0cb",
    "#ffb6c1",
    "#e75480",
    "#ff007f",
    "#ffffff",
    "#ffd6e7"
]

# Draw pink flower clusters
def flowers(x, y):

    for _ in range(random.randint(4, 8)):

        angle = random.uniform(0, math.tau)
        distance = random.uniform(2, 13)

        px = x + math.cos(angle) * distance
        py = y + math.sin(angle) * distance

        t.penup()
        t.goto(px, py)

        color = random.choice(flower_colors)
        t.dot(random.randint(3, 7), color)

        if random.random() > 0.5:
            t.dot(2, "#ffffff")


# Draw branches recursively
branch_count = 0

def branch(x, y, length, angle, width, depth):

    global branch_count
    branch_count += 1

    rad = math.radians(angle)

    nx = x + math.cos(rad) * length
    ny = y + math.sin(rad) * length

    # Pink branches
    if depth > 4:
        t.pencolor("#a83268")
    else:
        t.pencolor("#e078a5")

    t.pensize(max(1, width))

    t.penup()
    t.goto(x, y)
    t.pendown()
    t.goto(nx, ny)
    t.penup()

    if branch_count % 30 == 0:
        screen.update()

    # Flower clusters
    if depth <= 0:
        flowers(nx, ny)
        return

    spread = random.uniform(24, 34)
    new_length = length * random.uniform(0.70, 0.78)

    # Left branch
    branch(nx, ny, new_length, angle + spread,
           width * 0.72, depth - 1)

    # Right branch
    branch(nx, ny, new_length, angle - spread,
           width * 0.72, depth - 1)

    # Center branch
    if depth > 3 and random.random() > 0.55:
        branch(nx, ny, new_length * 0.85,
               angle + random.uniform(-8, 8),
               width * 0.65, depth - 1)


# Main tree
branch(0, -330, 125, 90, 8, 9)

screen.update()
turtle.done()
 