def fil():
    string = []
    with open("string_info.txt") as f:
        for line in f:
            string.append(line.strip('\n'))
        return string
