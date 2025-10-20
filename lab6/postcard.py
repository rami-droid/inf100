def symbol_count(path):
    char_count = {}
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
        for char in content:
            if not char.isspace():
                char_count[char] = char_count.get(char, 0) + 1
    return char_count

def test_count_letters():
    print('Tester count_letters... ', end='')
    expected = {
        'K': 2, 'j': 1, 'æ': 1, 'r': 10, 'e': 15, 'v': 3, 'n': 10, ',': 2,
        'S': 2, 'a': 3, 't': 2, 'y': 3, '.': 2, '"': 2, 'F': 2, 'i': 3,
        ':': 1, 'B': 1, 'o': 2, 'd': 2, 'J': 1, 'u': 1, "'": 1, 's': 4,
        'E': 1, 'p': 1, '!': 1, 'l': 2, 'm': 3,
    }
    actual = symbol_count('postcard.txt')
    assert 'æ' in actual, 'æ mangler, har du husket utf-8 encoding?'
    assert expected == actual
    print('OK')

test_count_letters()
