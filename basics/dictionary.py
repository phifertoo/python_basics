import pprint

eggs = { 
    'name': 'Zophie',
    'species': 'cat', 
    'age': '8'
}

ham = { 
    'name': 'Zophie',
    'age': '8',
    'species': 'cat' 
}


print(ham == eggs) #true
print(list(eggs.keys()))
print(list(eggs.values()))
print(list(eggs.items()))

for a, b in ham.items():
    print(a,b)

# return the value of 'age'. If it does not exist, return 0
print(eggs.get('age',0))

# sets the value of a key if the key does not already exist
eggs.setdefault('color', 'orange')

# triple quote is for multi-line strings
message = '''It was a bright cold day in April, and the clocks were striking thirteen'''
count = {}
for character in message.upper():
    count.setdefault(character, 0)
    count[character] = count[character] + 1

print(count)

pprint.pprint(count)
print(pprint.pformat(count))