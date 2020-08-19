import re

message = 'call me 415-555-1011 tomorrow, or at (415) 555-9999'
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
match_object = phoneNumRegex.search(message)

print(match_object.group())
print(match_object.group(1))
print(match_object.group(2))

# to find parentheses you have to escape them in the regex. Note that you are not escaping the 
# the parentheses from python
phoneNumRegex = re.compile(r'\(\d\d\d\) \d\d\d-\d\d\d\d')
mo = phoneNumRegex.search(message)
print(mo.group())

# using | means "or"
batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel')
print(mo.group())
print(mo.group(1))
