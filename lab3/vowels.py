def vowels(strings):
    vowels = ["a", "e", "i", "o", "u"]
    if isinstance(strings, str):
        for char in strings.lower():
            if char in vowels:
                count += 1
        print(f'"{text}": {count}')
        return count
    for text in strings:
        count = 0
        for char in text.lower():
            if char in vowels:
                count += 1
        print(f'"{text}": {count}')
        return count
if __name__ == "__main__":
    from pathlib import Path
    import json

    def load_test_data(file_path):
        content = Path(file_path).read_text(encoding="utf-8")
        data = json.loads(content)
        return data

    strings = load_test_data("strings.json")


    vowels(strings)
