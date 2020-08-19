# continue will skip the current iteration. In this case, we skip count == 3
count = 0
while count < 5:
    count += 1
    if count == 3:
        continue
    print(count)

#  break will stop the loop
your_name = ''
while True:
    print('Please type your name')
    your_name = input()
    if your_name != '':
        break
print('Thank you')

spam = 0
while spam < 5: 
    print('Hello world')
    spam += 1

name = ''
while name == '':
    print('Please type your name.')
    name = input()
print('Thank you')

