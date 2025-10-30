def draw_qr(canvas, x_left, y_top, size, qr):
    num_rows = len(qr)
    num_cols = len(qr[0])

    x_segment_length = size / num_cols
    y_segment_length = size / num_rows
    

    for row_i, row in enumerate(qr):
        for col_i, color in enumerate(row):
            x0 = x_left + col_i * x_segment_length
            y0 = y_top + row_i * y_segment_length
            x1_seg = x0 + x_segment_length
            y1_seg = y0 + y_segment_length
            if qr[row_i][col_i] == 0:
                canvas.create_rectangle(x0, y0, x1_seg, y1_seg, fill="white", outline = '')
            else: 
                canvas.create_rectangle(x0, y0, x1_seg, y1_seg, fill="black")

    pass


def display(matrix):
    from uib_inf100_graphics.simple import canvas, display as dsp
    canvas.create_rectangle(0, 0, 400, 400, fill='white', outline='')
    draw_qr(canvas, 25, 25, 350, matrix)
    dsp(canvas)

if __name__ == '__main__':
    sample_grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1],
        [0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0],
        [0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0],
        [0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0],
        [0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1],
        [0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0],
        [0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0],
        [0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0],
        [0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]
    
    display(sample_grid)
