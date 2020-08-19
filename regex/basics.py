import re

message = 'call me 415-555-1011 tomorrow, or at 415-555-9999'

# compile() finds the string that matches
# re.comiple returns a regular expresion object that has the search() method
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
match_object = phoneNumRegex.search(message)
# match_object has a group() method which returns the text found.
print(match_object.group())

# findall() returns all matches
allMatches = phoneNumRegex.findall(message)
print(allMatches)

# if you use groups/parentheses, it will return a list of tuples matching your groups
# note, you can have groups inside of groupss
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.findall(message)
print(mo)