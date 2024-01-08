import re


s = '1-23-45 6'
sep = re.split('[- ]', s)
lst = ''.join(sep)
print(lst)
