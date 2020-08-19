import re

mystring = 'hello, my name is john'

# ^ starts with
regexObj = re.compile(r'^hello')
mo = regexObj.search(mystring)
print(mo.group())


mystring2 = 'my name is john, hello'

# $ ends with
regexObj = re.compile(r'hello$')
mo = regexObj.search(mystring2)
print(mo.group())

mystring3 = 'hello'

# ^ % pattern matches entire string match
regexObj = re.compile(r'^hello$')
mo = regexObj.search(mystring3)
print(mo.group())
