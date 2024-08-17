import re
noNewlineRegex = re.compile('.*') # includes till the first new line character.
print(noNewlineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group())
'Serve the public trust.'
newlineRegex = re.compile('.*', re.DOTALL) # includes everything even the newline character.
print(newlineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group())