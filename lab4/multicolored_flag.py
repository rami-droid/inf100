def draw_multicolored_flag(canvas, x1, y1, x2, y2, colors):
    width = x2 - x1
    segments = len(colors)
    stripe_width = width / segments

    for col_i, color in enumerate(colors):
        canvas.create_rectangle(
            x1 + col_i * stripe_width,
            y2,
            x1 + (col_i + 1) * stripe_width,
            y1,
            fill=color,
            outline="",
        )
