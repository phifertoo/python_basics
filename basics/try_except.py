# errors cause python to crash. We can use try/except to prevent crashes
print('How many cats do you have?')
cats = input()
try:
# The int function acepts numbers. If the user inputs non-numbers, python will throw a ValueError which we can catch
    if int(cats) >=4:
        print("That's a lot of cats")
    else:
        print('That is not very many cats')
except ValueError:
    print('You did not enter a number')

# ______________________________________________________________________________________________


def divide_100_by(num):
    try:
        return 42 / num
# we can use generir error catching. No matter what error python encounters, it will print this error message instead of crashing
    except:
        print('Error: You tried to divide by Zero')


def divide_42_by(num):
    try:
        return 42 / num
# if you try to divide by 0, python will throw an error called ZeroDivisionError
# therefore, we can tell python that if it encounters this error, to print a message
# without this error catching mechansim, the program will crash
    except ZeroDivisionError:
        print('Error: You tried to divide by Zero')

print(divide_42_by(0)) #when we divide by 0, python will print our error statement instead of crashing
print(divide_42_by(15))



