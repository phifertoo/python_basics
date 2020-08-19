# to start debuggin: fn+f5
# open the debugging panel to see the available variables: control+shift+d
# to walk through the code line-by-line, step into each line (fn+f11)

a = 5
c = 10

def add2():
    global a
    a = a + 2


add2()
print(a)

print('a')
print('b')
print('c')
print('d')
print('e')
print('f')
