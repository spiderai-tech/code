import turtle as t, math as m, random as r, time, sys

if sys.platform == "win32":
    try:
        import ctypes
        ctypes.windll.shcore.SetProcessDpiAwareness(1)
    except Exception:
        pass

s = t.Screen()
s.setup(900, 700)
s.bgcolor("black")
s.title("Gradient Heart")
s.tracer(0)

pen = t.Turtle(visible=False)
pen.speed(0)
pen.penup()

def draw_heart():
    pen.clear()
    count = 0
    for i in range(320):
        a = 2 * m.pi * i / 320
        xo = 16 * (m.sin(a) ** 3) * 16
        yo = (13*m.cos(a) - 5*m.cos(2*a) - 2*m.cos(3*a) - m.cos(4*a)) * 16
        L = r.uniform(0.15, 0.5)
        xi, yi = xo * (1 - L), yo * (1 - L)
        for j in range(10):
            f = j / 10
            pen.pencolor(1 - 0.6*f, 0.7 * (1 - f), 0.8 * (1 - f))
            pen.width(2)
            pen.penup()
            pen.goto(round(xo + (xi - xo) * f), round(yo + (yi - yo) * f))
            pen.pendown()
            pen.goto(round(xo + (xi - xo) * (f + 0.1)), round(yo + (yi - yo) * (f + 0.1)))
            count += 1
            if count % 40 == 0:
                s.update()
                time.sleep(0.005)
    s.update()

while True:
    draw_heart()
    time.sleep(5)
    
t.done()