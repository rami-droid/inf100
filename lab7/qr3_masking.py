import enum


def should_flip(row, col, mask_no):
    match mask_no:
        case 0:
            return (row + col) % 2 == 0
        case 1:
            return row % 2 == 0
        case 2:
            return col % 3 == 0
        case 3:
            return (row + col) % 3 == 0
        case 4:
            return (row//2 + col//3) % 2 == 0
        case 5:
            return (row*col) % 2 + (row*col) % 3 == 0
        case 6:
            return ((row*col) % 2 + (row*col) % 3) % 2 == 0
        case 7:
            return ((row+col) % 2 + (row*col) % 3) % 2 == 0
    return False

def get_masked_matrix(matrix: list, mask_no):
    new_matrix = [row.copy() for row in matrix]

    for r, row in enumerate(new_matrix):
        for c, value in enumerate(row):
            if should_flip(r, c, mask_no):
                new_matrix[r][c] = 0 if value == 1 else 1
    return new_matrix


def get_refined_matrix(raw_matrix, error_correction_level, qr_layout):
    penalty = 0
    best_mask = 0
    for i in range(0, 7):
        masked_matrix = get_masked_matrix(raw_matrix, i)
        for r, row in enumerate(masked_matrix):
            for c, value in enumerate(row):
                try:
                    if sum(masked_matrix[r][c:c+5]) == 5:
                        penalty += 3
                except IndexError:
                    pass
                try:
                    if sum(masked_matrix[r:r+5]) == 5:
                        penalty += 3
                except IndexError:
                    pass

    #  if curr_penalty < penalty:
    #      best_mask = i
    pass
