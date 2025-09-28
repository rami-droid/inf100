<<<<<<< HEAD
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
        return count


=======
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
>>>>>>> 2b3c8f15c78cb651a425f8274e7ed951dc0b72c7
if __name__ == "__main__":

    def load_test_data(file_path):
        content = Path(file_path).read_text(encoding="utf-8")
        data = json.loads(content)
        return data

    strings = load_test_data("strings.json")

<<<<<<< HEAD
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
            return count

    from pathlib import Path
    import json
=======
>>>>>>> 2b3c8f15c78cb651a425f8274e7ed951dc0b72c7

    vowels(strings)
