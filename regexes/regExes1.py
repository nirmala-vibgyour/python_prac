import re
nongreedyRegex = re.compile(r'<.*>') # Greedy version
mo = nongreedyRegex.search('<To serve man> for dinner.>')
print(mo.group())
nongreedyRegex = re.compile(r'<.*?>') # Nongreedy version
mo = nongreedyRegex.search('<To serve man> for dinner.>')
print(mo.group())