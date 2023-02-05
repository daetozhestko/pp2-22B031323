def unique(list):
    list.sort()
    unique_list = []
    for i in list:
        if i not in unique_list:
            unique_list.append(i)
    print(unique_list)
list=[1,2,4,1,7,8,9,9,2,5]
unique(list)