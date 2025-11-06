def count_facilities_by_species(path):
    with open(path, "r", encoding="iso 8859-1") as f:
        content = f.read().splitlines()
        csv = [r.split(";") for r in content]

    index = 0
    for i in range(0, len(csv[1])):
        if csv[1][i].upper() == "ART":
            print(i)
            index = i

    dict = {}

    for item in csv[2::]:
        animal = item[index]
        dict.setdefault(animal, 0)
        dict[animal] += 1
    
    for pair in iter(dict.items()):
        print(f"{pair[0]}: {pair[1]}")

if __name__ == '__main__':
    count_facilities_by_species('Akvakulturregisteret.csv')
