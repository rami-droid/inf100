def good_style(source_code):
    lines = source_code.splitlines()
    for line in lines:
        if len(line) >= 80:
            return False
    return True

def good_style_from_file(filename):
    with open(filename, "r") as f:
        content = f.read()

    return good_style(content)

