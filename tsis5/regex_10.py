import re
text='camelCase'
pattern=r'([A-Z])'
print(re.sub(pattern,r'_\1',text).lower())
