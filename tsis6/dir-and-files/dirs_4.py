path = r"/Users/nurus/Desktop/tsis/tsis6/test/rows.txt"
with open(path, "rt+") as f:
    counter = 0
    for lines in f:
        counter += 1
    print(counter)