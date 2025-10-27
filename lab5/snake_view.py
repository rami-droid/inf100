def get_color(num: int, length):
    if  num == length:
        return "red"
    if num == 0:
        return "lightgray"
    elif num > 0:
        return "orange"
    else:
        return "cyan"


def draw_board(canvas, x1, y1, x2, y2, board, info_mode: bool, length):
    x_lo, x_hi = sorted((x1, x2))
    y_lo, y_hi = sorted((y1, y2))

    num_rows = len(board)
    num_cols = len(board[0])

    x_length = x_hi - x_lo
    y_length = y_hi - y_lo

    x_segment_length = x_length / num_cols
    y_segment_length = y_length / num_rows

    for row_i, row in enumerate(board):
        for col_i, num in enumerate(row):
            color = get_color(num, length)
            x0 = x_lo + col_i * x_segment_length
            y0 = y_lo + row_i * y_segment_length
            x1_seg = x0 + x_segment_length
            y1_seg = y0 + y_segment_length

            canvas.create_rectangle(x0, y0, x1_seg, y1_seg, fill=color)
            if info_mode:
                canvas.create_text(
                    x0 + (x_segment_length / 2), y0 + 10, text=(row_i, col_i)
                )
                canvas.create_text(x0 + (x_segment_length / 2), y0 + 20, text=num)


if __name__ == "__main__":
    from uib_inf100_graphics.simple import canvas, display

    test_board = [
        [1, 2, 3, 0, 5, 4, -1, -1, 1, 2, 3],
        [0, 4, 0, 7, 0, 3, -1, 0, 0, 4, 0],
        [0, 5, 0, 8, 1, 2, -1, -1, 0, 5, 0],
        [0, 6, 0, 9, 0, 0, 0, -1, 0, 6, 0],
        [0, 7, 0, 10, 11, 12, -1, -1, 0, 7, 0],
    ]

    draw_board(canvas, 25, 80, 375, 320, test_board, True, 3)
    display(canvas)
