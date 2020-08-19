# strings are immutable

name = 'zophie a cat'
newName = name[:7] + 'the' + name[8:12]
print(newName)

# \ is the line continuation character. it will tell python to ignore any indentation blocks
print('aaaaaaaaaaaaaaaaaaaaaaaaaaa' + \
            'bbbbbbbbbbb')