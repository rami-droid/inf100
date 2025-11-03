def set_fixed_fields(matrix, qr_layout):
    content = qr_layout
    zeroes = content["fixed_positions"]["zeros"]
    ones = content["fixed_positions"]["ones"]

    for coords in zeroes:
        row = coords[0]
        col = coords[1]

        matrix[row][col] = 0
    for coords in ones:
        row = coords[0]
        col = coords[1]
        matrix[row][col] = 1



def set_meta_fields(matrix, err_corr, mask_no, qr_layout):
    masks = qr_layout["meta_patterns"][err_corr][mask_no]
    meta_positions = qr_layout["meta_positions"]

    for i in range(len(masks)):
        row, col = meta_positions["first"][i]
        matrix[row][col] = masks[i]
    for i in range(len(masks)):
        row, col = meta_positions["second"][i]
        matrix[row][col] = masks[i]


def test_set_meta_fields():
    print('Testing set_meta_fields...', end='')
    # For easier visualization the test uses a matrix of strings rather
    # than 0's and 1's, but ultimately 1's and 0's should also work
    matrix = [
        ['-', '|', '-', '|', '-'],
        ['|', '-', '|', '-', '|'],
        ['-', '|', '-', '|', '-'],
        ['|', '-', '|', '-', '|'],
        ['-', '|', '-', '|', '-'],
    ]
    sample_layout = {
        'about': 'A fake and incomplete QR layout for testing only',
        'side_length': 5,
        # skipping key 'fixed_positions' since it is irrelevant here 
        'meta_positions': {
            'first': [
                [0, 0], [0, 1], [0, 2]
            ],
            'second': [
                [0, 4], [4, 4], [3, 1]
            ]
        },
        'meta_patterns': {
            'L': [
                ['A', 'B', 'C'], # mask_no = 0
                ['a', 'b', 'c']  # mask_no = 1
            ],
            'Q': [
                ['Q', 'R', 'S'], # mask_no = 0
                ['q', 'r', 's']  # mask_no = 1
            ],
        }
    }
    err_corr = 'L'
    mask_no = 0
    set_meta_fields(matrix, err_corr, mask_no, sample_layout)
    assert matrix == [
        ['A', 'B', 'C', '|', 'A'],
        ['|', '-', '|', '-', '|'],
        ['-', '|', '-', '|', '-'],
        ['|', 'C', '|', '-', '|'],
        ['-', '|', '-', '|', 'B'],
    ]

    err_corr = 'Q'
    mask_no = 1
    set_meta_fields(matrix, err_corr, mask_no, sample_layout)
    assert matrix == [
        ['q', 'r', 's', '|', 'q'],
        ['|', '-', '|', '-', '|'],
        ['-', '|', '-', '|', '-'],
        ['|', 's', '|', '-', '|'],
        ['-', '|', '-', '|', 'r'],
    ]

    print(' OK')
test_set_meta_fields()
