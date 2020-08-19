import traceback

def boxPrint(symbol, width, height):
    # raise an exception
    if len(symbol) != 1:
        raise Exception('symbol needs to be a string of length 1')

    print(symbol * width)

    for i in range(height - 2):
        print(symbol + (' ' * (width - 2)) + symbol)

    print(symbol * width)

boxPrint('*', 15, 5)


# __________________________________________________________________________________________
# if you don't want your program to crash if it encounters an error, you have to use
# try/except and tell the program what to do if it encouters an error.

try: 
    # raise an exception
    raise Exception('this is the error message')
except:
    # when there is an exception, the following code will run
    errorFile = open('error_log.txt', 'a')
    errorFile.write(traceback.format_exc())
    errorFile.close()
    print('The traceback info was written error_log.txt')


# if the assert condition evaluates to false, it raises an assertion error
assert False, 'This is an error message'

