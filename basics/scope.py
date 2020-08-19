rice = 42 #global variable

def eggs():
    eggs = 20 #local variable

def spam():
    spam = 99
    bacon() #does not have access to the spam variable unless we pass it into bacon()

def bacon():
    ham = 101
    print(rice) #has access to the rice global variable

def global_rice():
    global rice #rice is declared in the global scope. to adjust the value of the global variable, 
    #you need to decleare that you will be using the global variable
    rice = 55 

def local_rice():
    rice = 21 #this is a local variable even though it is declared in the global scope.


spam()
# when the function is called, the scope is temporarily created
# when the function is returned, the function scope is destroyed. 

# 1: code in the global scope cannot use local variables (inside of functions)
# 2: code in a local scope can access global variables
# 3: code in one function cannot use local variables from another function
# 4: you can use the same name for variables if they are in the different scopes