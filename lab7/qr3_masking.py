import qr2_matrix_completion

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
def score_matrix(matrix):
    zeros = 0
    ones = 0
    for r, row in enumerate(matrix):
        for c, value in enumerate(row):
            if matrix[r][c] == 0:
                zeros += 1
            else:
                ones += 1
    return abs(zeros - ones)


def get_refined_matrix(raw_matrix, error_correction_level, qr_layout):
    best = int("inf")
    best_iter = 0
    for i in range(0, 7):
        masked_matrix = get_masked_matrix(raw_matrix, i)
        curr_score = score_matrix(masked_matrix)
        if curr_score < best:
            best_iter = i
    masked_matrix = get_masked_matrix(raw_matrix, best_iter)
    masked_matrix =qr2_matrix_completion.set_meta_fields(masked_matrix, error_correction_level, best_iter, qr_layout)
    masked_matrix = qr2_matrix_completion.set_fixed_fields(masked_matrix, qr_layout)
