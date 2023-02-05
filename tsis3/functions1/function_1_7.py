def has_33(nums):
    a=bool()
    i =0
    while i < len(nums)-1:
        if nums[i]== nums[i+1]==3:
            a= True
            break
        else:
            a= False
            i+=1
    print(a)
nums =[1, 3, 2, 3, 3]
has_33(nums)
