'''
Challege 3: Regex?
'''

import re

f = open('3.txt', 'r')
rand = f.read()

search_obj = re.findall(r'[a-z]{1,}[A-Z]{3}[a-z]{1}[A-Z]{3}[a-z]{1,}', rand)
print(search_obj)
