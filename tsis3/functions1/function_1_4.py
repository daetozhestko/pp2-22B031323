def filter_prime(list):
    i=0
    while i<len(list):
        if list[i]>1:
            for j in range(2,int(list[i]/2)+1):
                if(list[i] % j) == 0:
                    list.pop(i)
                    break
            else:
                pass
        else:
            list.pop[i]
        i+=1
    print(list)
list=[24, 5, 9, 7, 8, 17]
filter_prime(list)