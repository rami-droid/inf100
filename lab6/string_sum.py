def get_stringsum(s):
    return sum([eval(n) for n in s.split(' ') if type(eval(n)) is int])

def test_get_stringsum():
    print('Testing get_stringsum... ', end='')
    assert 6 == get_stringsum('4 2')
    assert 9 == get_stringsum('5 -1 3 +2')
    assert 11 == get_stringsum('5 - 1 3 + 2')
    assert 42 == get_stringsum('42')
    assert 42 == get_stringsum('forty-one 42 førtitre')
    assert 42 == get_stringsum('foo2 42 2qux 3x1')
    assert 0 == get_stringsum('')
    assert 0 == get_stringsum('foo bar qux')
    assert 0 == get_stringsum('-9- 3+2')
    print('OK')

test_get_stringsum()
