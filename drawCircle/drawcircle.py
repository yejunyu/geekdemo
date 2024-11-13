import math
import turtle


def draw_circle_turtle(x, y, r):
    # move to start of circle
    turtle.up()
    turtle.setpos(x + r, y)
    turtle.down()
    # draw the circle
    for i in range(0, 365, 5):
        a = math.radians(i)
        turtle.setpos(x + r * math.cos(a), y + r * math.sin(a))


if __name__ == '__main__':
    draw_circle_turtle(100, 100, 50)
    turtle.mainloop()
