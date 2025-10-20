def shopping_list_to_dict(s):
    result = {}
    for entry in s.strip().split('\n'):
        qty, item = entry.split(' ', 1)
        result[item] = int(qty)
    return result


def shopping_list_file_to_dict(path):
    with open(path, "r") as file:
        return shopping_list_to_dict(file.read())


def test_shopping_list_file_to_dict():
    print('Tester shopping_list_file_to_dict... ', end='')
    expected = {
        'brød': 2,
        'pizza': 3,
        'poteter': 10,
        'kaffe': 1,
        'ost': 1,
        'epler': 13,
    }
    actual = shopping_list_file_to_dict('handleliste.txt')
    assert expected == actual
    print('OK')

test_shopping_list_file_to_dict()
