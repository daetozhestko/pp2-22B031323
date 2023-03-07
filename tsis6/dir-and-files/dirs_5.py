l = [1,2,3,4,5]
with open("test.txt", "w+") as f:
    for i in l:
        f.write(str(i))