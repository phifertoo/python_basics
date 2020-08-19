import re

mystring = 'Agent Alice gave secret documents to Agent Bob'

namesRegex = re.compile(r'Agent \w+')
mo = namesRegex.findall(mystring)
print(mo)

# substitue
namesRegex = re.compile(r'Agent \w+')
mo = namesRegex.sub('REDACTED', mystring)
print(mo)

# looking for "Agent" followed by 1 letter then 1 or more letters
namesRegex = re.compile(r'Agent (\w)\w*')
mo = namesRegex.findall(mystring)
print(mo)

# substitute with groups. \1 pertains to the (\w) which is the first group
namesRegex = re.compile(r'Agent (\w)\w*')
mo = namesRegex.sub(r'Agent \1****', mystring)
print(mo)

