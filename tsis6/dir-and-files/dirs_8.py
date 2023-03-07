import os
path = r"/Users/nurus/Desktop/tsis/tsis6/copy.txt"
if not os.path.exists(path=path):
    print("Doesnt exist")

os.remove(path)