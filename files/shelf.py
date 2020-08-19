# you can store lists and dicionaries in shelf files.

import shelve

# it will create binary files that stores dictionaries
shelfFile = shelve.open('mydata')
shelfFile['cats'] = ['Zophie', 'Pooka', 'Simon', 'Fat-tail', 'Cleo']
shelfFile.close()

shelfFile = shelve.open('mydata')
value = shelfFile['cats']
print(value)

# keys of the shelf module
keys = list(shelfFile.keys())
print(keys)

values = list(shelfFile.values())
print(values)