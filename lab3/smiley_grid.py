# smiley_grid.py
from smiley import draw_smiley
from uib_inf100_graphics.simple import canvas, display


def draw_smiley_line(y, size, n):
    x_coords = []
    for i in range(n):
        x_coords.append(i * size)

    for x in x_coords:
        draw_smiley(canvas, x, y, size)


def draw_smiley_grid(size, n):
    for i in range(n):
        draw_smiley_line((i) * size, size, n)


def main():
    draw_smiley_grid(70, 5)
    # draw_smiley_line(0, 60, 4)
    display(canvas)


if __name__ == "__main__":
    main()
