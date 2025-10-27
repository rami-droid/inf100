def get_stringsum(s):
    statements = s.split(" ")
    sum = 0
    for num in statements:
         try: 
            sum += int(num)
         except ValueError:
            continue
    return sum
    

def get_line_with_highest_stringsum(s):
    nums = s.strip().split('\n')
    curr = float('-inf')
    line_nr = -1
    highest = ''
    for i, line in enumerate(nums):
        line_sum = get_stringsum(line)
        if line_sum > curr:
            curr = line_sum
            line_nr = i + 1
            highest = line
    return (line_nr, curr, highest)

def main(path):
    with open(path, 'r') as f:
        line, curr, highest = get_line_with_highest_stringsum(f.read())
    print(f"Høyeste strengsum er {curr}, funnet først på linje {line}: {highest}")


def test_get_line_with_highest_stringsum():
    print('testing get_line_with_highest_stringsum... ', end='')

    arg = '4 2\n3 3\n6 6 6 6 12 6\n'
    assert (3, 42, '6 6 6 6 12 6') == get_line_with_highest_stringsum(arg)

    arg = '4 99 -98\nfoo 42 qux\nfoo bar quz\n'
    assert (2, 42, 'foo 42 qux') == get_line_with_highest_stringsum(arg)

    arg = '4 2\n3 3\n'
    assert (1, 6, '4 2') == get_line_with_highest_stringsum(arg)

    print('ok')

test_get_line_with_highest_stringsum()

#if __name__ == "__main__":
    #path = input("Filnavn: ")
    # main(path)
