from uib_inf100_graphics.simple import canvas, display
import random


colors = ["red", "blue", "green", "yellow", "purple", "orange"]


def draw_pop_art(canvas, col1, col2, x, y):
    canvas.create_rectangle(x, y, x + 150, y + 150, fill=col1, outline=col2)
    canvas.create_oval(x + 20, y + 20, x + 80, y + 80, outline=col2, width=2)
    canvas.create_oval(x + 80, y + 20, x + 120, y + 80, outline=col2, width=2)
    canvas.create_line(x + 40, y + 100, x + 110, y + 100, fill=col2, width=2)
    pass


seen_colors = []

for i in range(3):
    colnum1 = random.randint(0, len(colors) - 1)
    colnum2 = random.randint(0, len(colors) - 1)
    if colnum1 == colnum2 or colnum2 in seen_colors:
        colnum2 = random.randint(0, len(colors) - 1)
    if colnum1 in seen_colors:
        colnum1 = random.randint(0, len(colors) - 1)

    draw_pop_art(canvas, colors[colnum1], colors[colnum2], i % 2 * 200, i / 2 * 200)

display(canvas)
