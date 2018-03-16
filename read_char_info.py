
def read_char():
    char = []
    with open("char_info.txt") as f:
        for line in f:
            char.append(line.strip('\n\r'))
    return char
