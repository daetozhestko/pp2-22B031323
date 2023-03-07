with open("test.txt") as f:
    with open('copy.txt', "w") as cop:
        for line in f:
            cop.write(line)