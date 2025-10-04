def compress(raw_binary):
    curr = raw_binary[0]
    count = 0
    compressed_stack = []
    if curr == "1":
        compressed_stack.append(0)
    for num in raw_binary:
        if curr != num:
            curr = num
            compressed_stack.append(count)
            count = 1
        else:
            count += 1
    compressed_stack.append(count)
    print(compressed_stack)
    return compressed_stack


def decompress(compressed_binary):
    "input is string of ints"
    data = []
    curr_bit = 0 if compressed_binary[0] == "1" else 1
    for num in compressed_binary:
        curr_bit = 1 - curr_bit
        for i in range(int(num)):
            data.append(str(curr_bit).strip("-"))
    return "".join(data)


def test_compress():
    print("Tester compress... ", end="")
    # [2, 2, 3]
    assert [2, 3, 4, 4] == compress("0011100001111")
    assert [0, 2, 1, 8, 1] == compress("110111111110")
    assert [4] == compress("0000")
    print("OK")


def test_decompress():
    print("Tester decompress... ", end="")
    assert "0011100001111" == decompress([2, 3, 4, 4])
    assert "110111111110" == decompress([0, 2, 1, 8, 1])
    assert "0000" == decompress([4])
    print("OK")


test_decompress()
