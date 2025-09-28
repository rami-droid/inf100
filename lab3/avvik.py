from pathlib import Path
import json

def load_emission_data(filename):
    with open(filename, "r") as f:
        data = json.load(f)

    return data

def get_deviations(content):
    deviations = []
    array = content["data"]
    
    for entry in array:
        entry = entry['intensity']
        if entry['forecast'] is not None and entry['actual'] is not None:
            deviations.append(abs(entry['forecast'] - entry['actual']))

    
    return deviations
    
def count_values_larger_than(values, threshold):
    count = 0
    for value in values:
        if value > threshold:
            count += 1
    return count

print()

def main():
    filename = input()
    threshold = float(input())

    content = load_emission_data(filename)
    deviations = get_deviations(content)

    count = count_values_larger_than(deviations, threshold)
    print(f"Antall avvik større enn {int(threshold)}: {count}")

if __name__ == "__main__":
    main()