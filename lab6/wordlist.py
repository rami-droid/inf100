def filter_wordlist(path, search_string):
    with open(path, 'r') as file:
        content = file.read()
        words = content.split('\n')
        return [word for word in words if search_string in word]
