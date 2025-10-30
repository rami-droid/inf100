def sum_of_column(path, col):
    with open(path, "r") as f:
        content = f.read()
        lines = content.splitlines()
        table = [line.split(",") for line in lines]
        sum = 0
        for row in table:
            try:
                print(row[col])
                sum += float(row[col])
            except ValueError:
                pass
        return sum
