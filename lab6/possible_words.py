def possible_words_from_file(path, letters):
    with open(path, "r") as f:
        content = f.read()
    words = []

    letters = list(letters)

    for word in content.splitlines():
        temp_letters = letters.copy()
        valid = True
        for char in word:
            if char in temp_letters:
                temp_letters.remove(char)
            else:
                valid = False
                break
        if valid:
            words.append(word)
    return words

def test_possible_words_from_file():
    print('Tester possible_words_from_file... ', end='')
    assert(['du', 'dun', 'hu', 'hud', 'hun', 'hund', 'nu', 'uh']
            == possible_words_from_file('nsf2022.txt', 'hund'))

    # Ekstra test for varianten hvor det er wildcard i bokstavene
    # assert(['a', 'cd', 'cv', 'e', 'i', 'pc', 'wc', 'æ', 'å']
    #         == possible_words_from_file('nsf2022.txt', 'c*'))
    print('OK')

if __name__ == '__main__':
    test_possible_words_from_file()
