def draw_grid(canvas, x1, y1, x2, y2, color_grid):
    x_lo, x_hi = sorted((x1, x2))
    y_lo, y_hi = sorted((y1, y2))

    x_length = x_hi - x_lo
    y_length = y_hi - y_lo

    x_segment_length = x_length / len(color_grid)
    y_segment_length = y_length / len(color_grid[0])

    for col_i, col in enumerate(color_grid):
        for row_i, row in enumerate(color_grid[col]):
            color = color_grid[col][row]

            x0 = x_lo + col_i * x_segment_length
            y0 = y_lo + row_i * y_segment_length

            x1_segment = x0 + x_segment_length
            y1_segment = y0 + y_segment_length

            canvas.create_rectangle(x0, y0, x1_segment, y1_segment, fill=color)
            # draw whatever
    # canvas.create_rectangle(x1, y2, x1 + stripe_width, y1, fill='black')
    return
