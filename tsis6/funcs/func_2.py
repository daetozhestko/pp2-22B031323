def function(str):
    count=0
    for i in str:
        if i.isupper():
            count+=1
    return count
s=input('Write your string:')
print(function(s))
