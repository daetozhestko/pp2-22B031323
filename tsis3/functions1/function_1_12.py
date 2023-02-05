def histogram(nums):
    i=0
    while i < len(nums):
        a=nums[i]
        for x in range(a):
            print('*',end='')
        print("\n")
        i+=1
list=[4,3,2]
histogram(list)