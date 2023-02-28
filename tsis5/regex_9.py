import re
text='ILoveMathSoMuch'
pattern='([A-Z])'
print(re.sub(pattern,r' \1',text))