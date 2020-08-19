# escape character \
print('he\'s my brother')

# line break \n
print('yo \n let\'s meet \n tomorrow')

# raw string returns every character and escapes are ignored: r''
print(r'don\'t escape anything')

# multi-line string used for long strings''' ''''
print('''Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque non pulvinar velit. Curabitur euismod dolor id massa sagittis, lobortis ornare urna iaculis. Sed in ante sed leo convallis ornare elementum ut nisl. Donec in orci ante. Nunc tincidunt congue enim, nec feugiat orci rhoncus quis. Cras egestas, erat in aliquam efficitur, mi nisi mattis nibh, sed varius dolor metus id turpis. Proin gravida in ipsum ut rhoncus. Ut luctus lectus id lectus scelerisque, pulvinar dapibus quam malesuada. Curabitur dignissim finibus egestas. Pellentesque bibendum odio a pretium hendrerit. Donec cursus maximus justo, sed commodo purus.

Nam non nisi sem. Curabitur aliquam in nulla in bibendum. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Nulla eu turpis eros. In gravida leo et pulvinar placerat. Nam faucibus vehicula arcu a commodo. Aliquam velit lorem, tempus eu libero id, facilisis porta diam. Sed sed diam diam. Suspendisse magna nunc, ultricies quis sollicitudin in, vulputate nec elit. Praesent quis eros quis elit ornare lacinia. Cras ultrices tortor porta purus congue suscipit. Proin in volutpat nibh, convallis faucibus elit.

Curabitur euismod ligula et ipsum dapibus, quis pretium ligula ullamcorper. Ut congue tellus et ex accumsan, sit amet tempor massa dictum. Mauris mattis malesuada commodo. Aenean efficitur dolor justo, in pellentesque nisl sollicitudin tristique. Integer sit amet suscipit neque. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Vivamus feugiat sit amet nibh non congue. Pellentesque non tempus nulla. In faucibus odio at nisi varius dictum. Vestibulum gravida a erat sit amet maximus. Donec vitae viverra purus, vitae pellentesque lorem. Integer dictum ex leo, nec pretium tellus egestas rhoncus.

Vestibulum faucibus, leo posuere ornare venenatis, neque tellus tristique ex, quis rutrum quam diam in urna. Suspendisse eros enim, ullamcorper nec sem ac, mollis sodales odio. Curabitur ut faucibus velit, sit amet viverra justo. Aenean sodales semper arcu, in vestibulum arcu semper quis. Phasellus sit amet urna nulla. Suspendisse diam purus, cursus convallis rhoncus faucibus, interdum sit amet lectus. Aliquam vestibulum vel eros ut aliquam. Cras a feugiat ligula. Etiam ultrices aliquet massa at malesuada. Vestibulum eros turpis, congue ut volutpat sit amet, varius id neque. Curabitur efficitur felis dolor, a malesuada massa molestie id. Lorem ipsum dolor sit amet, consectetur adipiscing elit.

Nunc fringilla neque lacinia ipsum feugiat, ut mattis sapien bibendum. Suspendisse vestibulum, urna nec imperdiet laoreet, enim nisi viverra mi, non laoreet orci lectus non mi. Aliquam id commodo lorem. Sed ullamcorper augue nec mattis dapibus. Cras vel purus pulvinar, semper nulla in, facilisis dui. Suspendisse lacinia justo quis turpis semper egestas. Integer sollicitudin nisi tristique mi placerat dictum. Aenean dolor purus, pretium feugiat hendrerit vel, vehicula eu orci.''')


# slicing strings
spam = 'hello'
print(spam[:3])


# upper/lower
print(spam.upper(), spam.lower())

# islower()/isupper()
print(spam.isupper(), spam.islower())

# isalpha()
# tests if all characters (including spaces) are letters
print(spam.isalpha())

# isspace()
# all characters are spaces
print(spam.isspace())

# istitle()
# all first characters are uppercase
print(spam.istitle())

# startswith()
print(spam.startswith('h'))

# endswith()
print(spam.endswith('o'))

# join()
# connects two strings
# , is the delimiter
','.join(['cats', 'rats', 'bats'])

# split()
# returns a list of strings based on a delimiter
print('My name is Simon'.split())

# rjust() / ljust()
# add whitespace to the left
print('hello'.rjust(10))
print('hello'.ljust(5))
print('hello'.center(10))
print('hello'.rjust(10, '-'))

# strip()
# returns a new string with white space removed from both sides
print('     Hello      '.strip())

# lstrip()
# remove whitespace from the left of the string
print('     Hello      '.lstrip())

# replace()
ham = 'hello there!'
ham = ham.replace('e', 'XYZ')
print(ham)

import pyperclip
pyperclip.copy('helllo')
print(pyperclip.paste())


name = 'Alice'
place = 'Main Street'
time = '6 am'
food = 'turnips'

# string interpolation
output = 'Hello %s, you are invited to a party at %s, at %s. Please bring %s' % (name, place, time, food)
print(output)
