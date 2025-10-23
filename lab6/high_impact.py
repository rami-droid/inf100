def get_impact(line: str):
    num = line.strip().split(';')[2] 
    try:
        return float(num)
    except: 
        return None


def filter_earthquakes(earthquake_csv_string, threshold):
    table = [line.split(';') for line in earthquake_csv_string.splitlines()]
    filtered = []
    filtered.append(table[0])
    table = table[1:]
    for row in table:
        try:
            filtered.append(row if float(row[2]) >= threshold else None)
        except AssertionError:
            pass
        except ValueError:
            pass
    return '\n'.join([";".join(row) for row in filtered if row is not None])
    # filtered = [row for row in table if  float(row[2]) >= threshold]
    # table = [n.split(';') for n in for line.split() in earthquake_csv_string.splitlines() if n[2] >= threshold or n[2] == 'impact']
def read_file(path):
    with open(path, 'rt', encoding='utf-8') as f:
        return f.read()
    
def filter_earthquakes_file(source, target, threshold):
    with open(target, 'w') as f:
        f.write(filter_earthquakes(read_file(source), threshold))

def test_filter_earthquakes_file():
    print('Tester filter_earthquakes_file... ', end='')


    filter_earthquakes_file('earthquakes_simple.csv',
                            'earthquakes_above_7.csv', 7.0)
    expected_value = (
        'id;location;impact;time\n'
        'us100068jg;Northern Mariana Islands;7.7;2016-07-29 17:18:26\n'
        'us10006d5h;New Caledonia;7.2;2016-08-11 21:26:35\n'
        'us10006exl;South Georgia Island region;7.4;2016-08-19 03:32:22\n'
    )
    actual_value = read_file('earthquakes_above_7.csv')
    assert expected_value.strip() == actual_value.strip()
    print('OK')

    # Manuell test: Åpne earthquakes_above_7.csv og se at innholdet stemmer
test_filter_earthquakes_file()
