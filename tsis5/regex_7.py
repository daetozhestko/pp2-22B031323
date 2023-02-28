import re 
text="snake_case"
pattern=r'(.*?)_(.*)'
m=re.match(pattern,text)
print(m.group(1)+m.group(2)[0].upper()+m.group(2)[1:])