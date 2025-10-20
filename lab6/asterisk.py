from pathlib import Path

def add_asterisks(s):
    return ';'.join([f'*{word}*' for word in s.split(';')])

def add_asterisks_csv(infile, outfile):
    table = []
    with open(infile, 'r') as file:
        content = file.read().strip().split('\n')
        for row in content:
            table.append(row)
    with open(outfile, 'w') as file:
        for row in table:
            file.write(add_asterisks(row) + '\n')

def test_add_asterisks():
    print('Testing add_asterisks...', end='')

    # Test 1
    arg = 'foo;bar;qux'
    actual = add_asterisks(arg)
    expected = '*foo*;*bar*;*qux*'
    assert expected == actual

    # Test 2
    arg = 'honey;mustard'
    actual = add_asterisks(arg)
    expected = '*honey*;*mustard*'
    assert expected == actual

    print('OK')


def test_add_asterisks_csv():
    print('Testing add_asterisks_csv...', end='')

    infile = '.tmp.add_asterisks_csv_test.in.csv'
    outfile = '.tmp.add_asterisks_csv_test.out.csv'

    Path(infile).write_text((
        'foo;bar;qux\n'
        'honey;mustard;sausage\n'
    ), encoding='utf-8')

    add_asterisks_csv(infile, outfile)
    actual = Path(outfile).read_text(encoding='utf-8')
    expected = (
        '*foo*;*bar*;*qux*\n'
        '*honey*;*mustard*;*sausage*\n'
    )
    assert expected.strip() == actual.strip()

    print('OK')
test_add_asterisks_csv()

