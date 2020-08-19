import re

# batRegex = re.compile(r'Batman|Batwoman')
# the ? means that the group (wo) can occur 0 or 1 times
batRegex = re.compile(r'Bat(wo)?man')
mo = batRegex.search('The adventures of Batman')
mo2 = batRegex.search('The adventures of Batwoman')

print(mo.group())
print(mo2.group())

phoneRegex = re.compile(r'(\d\d\d)?\d\d\d-\d\d\d\d')
mo = phoneRegex.search('My phone number is 415-555-1234')
mo2 = phoneRegex.search('My phone number is 555-1234')

print(mo.group())
print(mo2.group())

# wo can appear 0 or more times
batRegex = re.compile(r'Bat(wo)*man')
mo = batRegex.search('The adventures of Batwowowowoman')
print(mo.group())

# wo must appear 1 or more times
batRegex = re.compile(r'Bat(wo)+man')
mo = batRegex.search('The adventures of Batwoman')
print(mo.group())

# exactly 3 matches in a row
haRegex = re.compile(r'(Ha){3}')
mo = haRegex.search('he said HaHaHa')
print(mo.group())

# range of 3-5 matches in a row. notes (3:) means 3 or more
haRegex = re.compile(r'(Ha){3,7}')
mo = haRegex.search('he said HaHaHaHaHa')
print(mo.group())

# by default python is greedy which means it matches the longest possible string
# therefore, instead of matching 1,2,3, it matches 1,2,3,4,5
digitRegex = re.compile(r'(\d){3,5}')
mo = digitRegex.search('123456789')
print(mo.group())

# you can use a ? to create a non-greedy(shortest) match
digitRegex = re.compile(r'(\d){3,5}?')
mo = digitRegex.search('123456789')
print(mo.group())