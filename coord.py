from turtle import *


def draw_coordinates(size = 250, step = 50):
    """Draws a coordinate system with the given size."""
    initial_pos = pos()
    for i in range(-size, size + 1, step):
        # vertical lines
        penup()
        goto(i, -size)
        pendown()
        if i == 0:
            # main axis
            width(2)
            goto(i, size)
            setheading(90)
            stamp()
            width(1)
        else:
            goto(i, size)
        write(i)

        # horizontal lines
        penup()
        goto(-size, i)
        pendown()
        if i == 0:
            # main axis
            width(2)
            goto(size, i)
            setheading(0)
            stamp()
            width(1)
        else:
            goto(size, i)
        write(i)
    penup()
    goto(initial_pos)
    pendown()


if __name__ == "__main__":
    speed(0)
    draw_coordinates(500)
    done()