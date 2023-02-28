import re 
text='aj.bcf euf uehd,nedfoen.iefne'
pattern=r'[., ]'
print(re.sub(pattern,':',text))
