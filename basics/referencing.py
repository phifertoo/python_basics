# Variables are just references to a value 

# although you modify the new reference (cheese), the new reference still points to the same data [0, 1, 2, 3, 4, 5]
# therefore, any references pointing to the same data will reflect the altered data

spam = [0, 1, 2, 3, 4, 5]
cheese = spam
cheese[1] = 'hello'
print(cheese) # [0, 'hello', 2, 3, 4, 5]
print(spam) # [0, 'hello', 2, 3, 4, 5]


#________________________________________________________________________________________________________

def eggs(input):
    input.append('hello')

# although the input variable is destroyed after eggs() is called, input is a reference to my_list.
# therefore, the original data (my_list) is altered

my_list = [1, 2, 3]
eggs(my_list)
print(my_list)


import copy
# instead of creating a reference to the list, we can create a whole new list, we can use deepcopy
deepcopy = copy.deepcopy(spam)
deepcopy[0] = 'start'
print(deepcopy)
print(spam) # spam is unaffected by the changes we made to deepcopy