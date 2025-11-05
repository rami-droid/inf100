import csv

def sum_of_column(path, col):
    total = 0
    with open(path, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            if col < len(row):
                try:
                    total += float(row[col])
                except ValueError:
                    pass
    return total
