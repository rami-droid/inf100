def get_next_pos(row, column, size):
    if column % 2 == 0:
        if column == 0:
            return (row - 1, column)
        return (row, column - 1)
    
    elif column % 4 == 1:
        if row == size - 1:
            return (row, column - 1)
        return (row + 1, column + 1)
    
    else:  
        if row == 0:
            return (row, column - 1)
        return (row - 1, column + 1)

def bit_list_to_raw_matrix(bit_list, qr_layout):
    fixed_ones = []
    fixed_zeroes = []
    meta_first = []
    meta_second = []

    for r, c in qr_layout['meta_positions']['first']:
        meta_first.append((r, c))
    for r, c in qr_layout['meta_positions']['second']:        
        meta_second.append((r, c))

    matrix = []
    size = qr_layout['side_length']

    for r, c in qr_layout['fixed_positions']['ones']:
        fixed_ones.append((r, c))
    for r, c in qr_layout['fixed_positions']['zeros']:
        fixed_zeroes.append((r, c))

    for _ in range(size):
        matrix.append([0 for _ in range(size)])

    curr = (size -1, size -1)
    for i in bit_list:
        while curr in fixed_ones or curr in fixed_zeroes or curr in meta_second or curr in meta_first:
            curr = get_next_pos(curr[0], curr[1], size)
        matrix[curr[0]][curr[1]] = i
        curr = get_next_pos(curr[0], curr[1], size)

    return matrix

