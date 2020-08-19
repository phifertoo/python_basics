spam = ['cat', 'bat', 'rat', 'elephant']

sliced = spam[0:-1] # [cat, bat, rat]
first_3 = spam[:3]
last_3 = spam[-3:]
joined_list = [1, 2, 3] + [4, 5, 6]
multiplied_list = [1,2,3] * 3
list_of_string = list('hello')
isPresent = 'cat' in spam
isNotPresent = 'dog' not in spam
del spam[2] #delete item at index 2
spam.remove('bat')
spam.append('gopher')
spam.insert(1, 'Chicken') # insert 'chicken' at index 1
spam.sort(reverse = True, key = str.lower) # cannot sort lists with stings and numbers. Uppercase characters come before lower case characters


# multiple assignment
fruit = ['strawberry', 'banana', 'grape']
red, yellow, purple = fruit

# finding the index of an element. If it is not found, python will throw an error
# the index() method will return the index of the first element found
my_index = spam.index('cat')





print(spam)
