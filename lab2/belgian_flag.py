def draw_belgian_flag(canvas, x1, y1, x2, y2):
    width = x2 - x1
    stripe_width = width / 3

    canvas.create_rectangle(x1, y2, x1 + stripe_width, y1, fill='black')
    canvas.create_rectangle(x1 + stripe_width, y2, x1 + stripe_width * 2, y1, fill='yellow')
    canvas.create_rectangle(x1 + stripe_width * 2, y2, x2, y1, fill='red')
    pass
