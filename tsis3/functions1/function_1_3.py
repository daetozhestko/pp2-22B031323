def solve(numheads,numlegs):
    c=int((numlegs-2*numheads)/2)
    print("Number of chickens:",c)
    print("Number of rabbits:",numheads-c)
numheads =35
numlegs = 94
solve(numheads,numlegs)