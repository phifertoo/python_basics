# Truthy values

value_test = ''
if value_test:
    print('empty string')


value_test = 'john'
if value_test:
    print('non-empty string')

value_test = {}
if value_test:
    print('empty dictionary')

value_test = []
if value_test:
    print('empty list')

value_test = ()
if value_test:
    print('empty tuple')

number = 0
if number:
    print('number ' + str(number))

number = 1
if number:
    print('number ' + str(number))

# convert truthy/falsy value to boolean
print(bool(0))
print(bool(1))
print(bool(''))
print(bool('john'))
print(bool({}))
print(bool({'a': 'b'}))
print(bool([]))
print(bool([3,9]))
print(bool(()))
print(bool((2,3)))


