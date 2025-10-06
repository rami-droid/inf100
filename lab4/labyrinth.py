def rotate(grid, clockwise):
    num_rows = len(grid)
    num_cols = len(grid[0])

    rotated_grid = [[0 for _ in range(num_rows)] for _ in range(num_cols)]
    if clockwise:
        for row in range(num_rows):
            for col in range(num_cols):
                rotated_grid[col][num_rows - row - 1] = grid[row][col]
    else:
        for row in range(num_rows):
            for col in range(num_cols):
                rotated_grid[num_cols - col - 1][row] = grid[row][col]

    return rotated_grid


grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(rotate(grid, True))
