def spy_game(nums):
    i=-1
    while i < len(nums)-3:
        a=bool()
        one=nums[i+1]
        two=nums[i+2]
        three=nums[i+3]
        if one==0 and two==0 and three==7:
            a=True
            break
        else:
            a=False
        i+=1
    print(a)
nums=[9, 2, 0, 0, 7]
spy_game(nums)