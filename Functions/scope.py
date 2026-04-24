#A variable is only available from inside the region it is created. This is called scope.

#Local Scope
#A variable created inside a function belongs to the local scope of that function, and can only be used inside that function.
def func(x):
        print("You age is:",x)
func(21)
print("")

#Function Inside Function
#The local variable can be accessed from a function within the function
def func():
        x = 10
        def settimer():
                print(f"Timer is {x} seconds.")
        settimer() #Have to call the inner function first else code will not work
func()
print("")

#Global Scope
#A variable created in the main body of the Python code is a global variable and belongs to the global scope.
#Global variables are available from within any scope, global and local.
x = 1
def func():
        print(x)
func()
print("")

#Naming Variables
#The function will print the local x, and then the code will print the global x
x = 300
def func():
        x = 200
        print(x)
func()
print(x)
print("")

#Global Keyword
#If you need to create a global variable, but are stuck in the local scope, you can use the global keyword.
#The global keyword makes the variable global.
def func():
        global x #global should be used before assigning value
        x = 100
func()
print(x)
print("")

#Also, use the global keyword if you want to make a change to a global variable inside a function.
x = "global"
def func():
        global x
        x = "changed"
func()
print(x)
print("")

#Nonlocal Keyword
#The nonlocal keyword is used to work with variables inside nested functions.
#The nonlocal keyword makes the variable belong to the outer function.
def func1():
        x = "outerfn"
        def func2():
                nonlocal x
                x = "innerfn"
        func2()
        return x
print(func1())
print("")

#The LEGB Rule
"""Python follows the LEGB rule when looking up variable names, and searches for them in this order:

Local - Inside the current function
Enclosing - Inside enclosing functions (from inner to outer)
Global - At the top level of the module
Built-in - In Python's built-in namespace
"""
x = "global"
def func1():
        x = "Outerfn"
        def func2():
                x = "Innerfn"
                print("Inner:",x)
        func2()
        print("Outer:",x)
func1()
print(x)
print("")