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
    pass
