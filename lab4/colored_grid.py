def draw_grid(canvas, x1, y1, x2, y2, color_grid):
    x_lo, x_hi = sorted((x1, x2))
    y_lo, y_hi = sorted((y1, y2))

    num_rows = len(color_grid)
    num_cols = len(color_grid[0])

    x_length = x_hi - x_lo
    y_length = y_hi - y_lo

    x_segment_length = x_length / num_cols
    y_segment_length = y_length / num_rows

    for row_i, row in enumerate(color_grid):
        for col_i, color in enumerate(row):
            x0 = x_lo + col_i * x_segment_length
            y0 = y_lo + row_i * y_segment_length
            x1_seg = x0 + x_segment_length
            y1_seg = y0 + y_segment_length

            canvas.create_rectangle(x0, y0, x1_seg, y1_seg, fill=color)

