# open file in read mode
helloFile = open(r'C:\Users\phife\applications\automate_the_boring_stuff\files\hello.txt')

# read() returns a string
content = helloFile.read()
print(content)

# close the file. you have to close the file before reading again
helloFile.close()

# readlines returns a list with the text delimited by lines
helloFile = open(r'C:\Users\phife\applications\automate_the_boring_stuff\files\hello.txt')
content = helloFile.readlines()
print(content)
helloFile.close()

# open in "write" mode which will erase the entire file then write text
helloFile = open(r'C:\Users\phife\applications\automate_the_boring_stuff\files\hello.txt', 'w')
helloFile.write('writing')
helloFile.close()

# open in "append" mode which will retain the existing content then add text
helloFile = open(r'C:\Users\phife\applications\automate_the_boring_stuff\files\hello.txt', 'a')
helloFile.write('\nappending')

# you can only read, write text in txt files. You can store dictionaries in shelf files. see shelf.py