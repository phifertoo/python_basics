#! python3

print('hello world')

# in the command line
# py.exe C:\Users\phife\applications\automate_the_boring_stuff\basics\command_line.py

# to group files to be run together, we can batch them
# we created a batching.bat file with the following code to tell the command line to run this file
# @py C:\Users\phife\applications\automate_the_boring_stuff\basics\command_line.py %*
# @pause

# in the command line type to the run the batch
# C:\Users\phife\applications\automate_the_boring_stuff\basics\batching.bat


import sys
# when you run the program in the command line, you can pass arguments and access them using sys.argv
print(sys.argv)