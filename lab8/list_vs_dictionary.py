def key_value_getter(d):
    values = []
    keys = []
    for item in iter(d.items()):
        values.append(item[0])
        keys.append(item[1])

    print("Dictionary keys")
    for key in keys:
        print(key)

    print("\nDictionary values")
    for value in values:
        print(value)

def index_value_getter(a):
    indeces = []
    values = []

    for i, val in enumerate(a):
        indeces.append(i)
        values.append(val)

    print("Dictionary keys")
    for i in indeces:
        print(i)

    print("\nDictionary values")
    for value in values:
        print(value)
