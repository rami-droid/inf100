def get_next_pos(row, column, size):
    next = (row, column)
    if column == 0:
        next = (row-1, column)
    elif column % 2 == 0:
        next = (row, column-1)
    elif row != size - 1 and column % 4 == 1:
        next = (row + 1, column + 1)
    elif column % 4 == 1 or row == 0:
        next = (row, column - 1)
    else:
        next = (row - 1, column + 1)
    return next

def bit_list_to_raw_matrix(bit_list, qr_layout):
    matrix = []
    size = qr_layout['side_length']
    for _ in range(size):
        matrix.append([0 for _ in range(size)])
    # size -= 1

    curr = (size -1, size -1)
    for i in bit_list:
        matrix[curr[0]][curr[1]] = i
        curr = get_next_pos(curr[0], curr[1], size)
    print(matrix)
    return matrix

def test_bit_list_to_raw_matrix():
    print('Testing bit_list_to_raw_matrix...', end='')
    # To make the test easier to read, bit_list contain distinct elements here
    # (in actual applications, bit_list would only have 0's and 1's)
    arg_bit_list = list(range(1, 72))
    arg_qr_layout = {
        'about': 'A fake and incomplete QR layout for testing only',
        'side_length': 9,
        'fixed_positions': {
            'ones': [
                [1, 3], [1, 4], 
            ],
            'zeros': [
                [2, 3], [2, 4],
            ]
        },
        'meta_positions': {
            'first': [
                [5, 2], [5, 3]
            ],
            'second': [
                [6, 2], [6, 3]
            ]
        }
        # key 'meta_patterns' skipped, since it is irrelevant for this task
    }

    expected = [
        [ 0, 50, 49, 48, 47, 20, 19, 18, 17],
        [ 0, 52, 51,  0,  0, 22, 21, 16, 15],
        [71, 54, 53,  0,  0, 24, 23, 14, 13],
        [70, 56, 55, 46, 45, 26, 25, 12, 11],
        [69, 58, 57, 44, 43, 28, 27, 10,  9],
        [68, 59,  0,  0, 42, 30, 29,  8,  7],
        [67, 60,  0,  0, 41, 32, 31,  6,  5],
        [66, 62, 61, 40, 39, 34, 33,  4,  3],
        [65, 64, 63, 38, 37, 36, 35,  2,  1]
    ]
    actual = bit_list_to_raw_matrix(arg_bit_list, arg_qr_layout)
    assert expected == actual
    print(' OK')

test_bit_list_to_raw_matrix()
