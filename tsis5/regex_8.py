import re 
text="ILoveMathSoMuch"
pattern=r'([A-Z])'
print(re.split(pattern,text))