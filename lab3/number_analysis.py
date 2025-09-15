from pathlib import Path
import json

input_file = "numbers.json"
file_content = Path(input_file).read_text(encoding="utf-8")
numbers = json.loads(file_content)

total = 1
for num in numbers:
    # Oddetall eller partall
    if num % 3 == 0:
        kind = "kan deles på 3"
    else:
        kind = "kan ikke deles på 3"

    total *= num

    print(f"Tittei! {num} er {kind}")

print(f"Produktet av tallene {numbers} er {total}")
