if __name__ == "__main__":
    from pathlib import Path
    import json

    def load_test_data(file_path):
        content = Path(file_path).read_text(encoding="utf-8")
        data = json.loads(content)
        return data

    strings = load_test_data("strings.json")

    def vowels(strings):
        for text in strings:
            text = text.lower()
            vowels = ["a", "e", "i", "o", "u"]
            count = 0

            for char in text:
                for vowel in vowels:
                    if char == vowel:
                        count += 1

            print(f'"{text}": {count}')

    vowels(strings)
