import re

message = 'call me 415-555-1011 tomorrow, or at 415-555-9999'

# digits
# /d

# non-digits
# /D

# letters
# /w

# non-letters
# /W

# space, tab, new line
# /s

# not a space, tab, or line
# /S

lyrics = '''12 drummers drumming
11 pipers piping
10 lords a-leaping
9 ladies dancing
8 maids a-milking
Seven swans a-swimming
Six geese a-laying
Five golden rings
Four calling birds
Three french hens
Two turtle doves, and
A partridge in a pear tree'''

# find 1 or more digits followed by a space following by 1 or more letters
xmasRegex = re.compile(r'\d+\s\w+')
mo = xmasRegex.findall(lyrics)
print(mo)

# a | e | i | o | u
vowelRegex = re.compile(r'[aeiouAEIOU]')
mo = vowelRegex.findall(lyrics)
print(mo)

# two vowels in a row
vowelRegex = re.compile(r'[aeiouAEIOU]{2}')
mo = vowelRegex.findall(lyrics)
print(mo)

# ^ inside of [] finds character that is not specified
# two vowels in a row
nonvowelRegex = re.compile(r'[^aeiouAEIOU]')
mo = nonvowelRegex.findall(lyrics)
print(mo)

# . is any character that is not \n
atRegex = re.compile(r'.ens')
mo = atRegex.findall(lyrics)
print(mo)

# if you want . to include \n, you have to add the re.DOTALL argument to the compile()
atRegex = re.compile(r'.*', re.DOTALL)
mo = atRegex.findall(lyrics)
print(mo)

# ignore casing by passing in re.I into the compile
vowelRegex = re.compile(r'[aeiou]', re.I)
mo = vowelRegex.findall(lyrics)
print(mo)


mystring = 'First Nae: Al Last Name: Sweigart'
# .* means any pattern. It will always find the longest match possible
# for a non-greedy match add a ?
nameRegex = re.compile(r'First Nae: (.*) Last Name: (.*)')
mo = nameRegex.findall(mystring)
print(mo)

# greedy example
server = '<To serve humans> for dinner.>'

# longest match possible
greedy = re.compile(r'<(.*)>')
mo = greedy.findall(server)
print(mo)

# shortest match possible with ?
nongreedy = re.compile(r'<(.*?)>')
mo = nongreedy.findall(server)
print(mo)