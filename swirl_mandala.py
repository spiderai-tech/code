import turtle as tur

tur.setup(800, 800)
tur.speed(0)
tur.width(2)
tur.bgcolor("black")
tur.color("#FF69B4")   # hot pink

for j in range(30):
    tur.left(j * 2)                    # rotate each ring slightly for a swirl
    for i in range(20):
        tur.right(96)
        tur.circle(200 - j * 4, 90)
        tur.left(90)
        tur.circle(200 - j * 4, 90)
        tur.right(180)
        tur.circle(50, 24)

tur.hideturtle()
tur.done()