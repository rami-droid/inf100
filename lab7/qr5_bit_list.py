from re import error


def string_to_data(string):
    bits = []
    for c in string:
        for x in f"{ord(c):08b}":
            bits.append(int(x))

    return bits

def get_core_list(input_string):
    bit_list = []
    # byte mode
    mode = [0,1,0,0]
    bit_list.extend(mode)

    length = len(input_string)
    length_bits = [int(bit) for bit in format(length, '08b')]
    bit_list.extend(length_bits)

    data = string_to_data(input_string)

    bit_list.extend(data)

    terminator = [0,0,0,0]
    bit_list.extend(terminator)

    return bit_list

def pad_bit_list(core_bit_list, pad_to_bytes):
    PAD1 = [1, 1, 1, 0, 1, 1, 0, 0]
    PAD2 = [0, 0, 0, 1, 0, 0, 0, 1]   

    target_bits = pad_to_bytes * 8
    current_bits = len(core_bit_list)
    bits_to_add = target_bits - current_bits
    bytes_to_add = bits_to_add // 8

    for i in range(bytes_to_add):
        core_bit_list.extend(PAD1) if i % 2 == 0 else core_bit_list.extend(PAD2)

def string_to_bit_list(content_string, qr_layout):
    bit_list = get_core_list(content_string)
    error_correction_bytes = qr_layout["error_correction_bytes"]
    data_bytes_needed = len(bit_list) // 8
    byte_capacity = qr_layout['byte_capacity']

    ec_level = None
    for level in ["L", "M", "Q", "H"]:
        ec_bytes = error_correction_bytes[level]
        available_data_bytes = byte_capacity - ec_bytes
        if data_bytes_needed <= available_data_bytes:
            ec_level = level
            break

    ec_bytes = error_correction_bytes[ec_level]
    data_bytes = byte_capacity - ec_bytes
    pad_bit_list(bit_list, data_bytes)

    return (bit_list, ec_level)


def test_pad_bit_list():
    print('Testing pad_bit_list...', end='')
    PAD1 = (1, 1, 1, 0, 1, 1, 0, 0)
    PAD2 = (0, 0, 0, 1, 0, 0, 0, 1)
    
    arg = [1, 1, 1, 1, 1, 1, 1, 1]
    expected = arg + list(PAD1) + list(PAD2) + list(PAD1)
    pad_bit_list(arg, 4)
    assert expected == arg

    arg = [1, 1, 1, 1, 1, 1, 1, 1]
    expected = arg + list(PAD1) + list(PAD2) + list(PAD1) + list(PAD2)
    pad_bit_list(arg, 5)
    assert expected == arg

    arg = [1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1]
    expected = arg + list(PAD1) + list(PAD2) + list(PAD1) + list(PAD2)
    pad_bit_list(arg, 6)
    assert expected == arg
    print(' OK')

test_pad_bit_list()
