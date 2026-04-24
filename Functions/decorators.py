#Decorators let you add extra behavior to a function, without changing the function's code.
#A decorator is a function that takes another function as input and returns a new function.
def changecase(func):
        def inner():
                return func().upper()
        return inner
@changecase
def myfunction():
        return "hello world"
print(myfunction())
print("")

#By placing @changecase directly above the function definition, the function myfunction is being "decorated" with the changecase function.
#The function changecase is the decorator.
#The function myfunction is the function that gets decorated.

#Multiple Decorator Calls
#A decorator can be called multiple times. Just place the decorator above the function you want to decorate.
def changecase2(func):
        def inner():
                return func().upper()
        return inner

@changecase2
def func1():
        return "hello this is the second function"
print(func1())

@changecase2
def func2():
        return 'this is second function part 2'
print(func2())
print("")

#Arguments in the Decorated Function
#Functions that require arguments can also be decorated, just make sure you pass the arguments to the wrapper function.
def changecase3(func):
        def inner(x): #add an parameter here as well if our main fn has parameters and arguments
                return func(x).upper() #add an parameter here as well if our main fn has parameters and arguments
        return inner
@changecase3
def func3(name):
        return f"hello the name is {name}."
print(func3("Harsh"))
print("")

#*args and **kwargs
#Sometimes the decorator function has no control over the arguments passed from decorated function, to solve this problem, add (*args, **kwargs) to the wrapper function, this way the wrapper function can accept any number, and any type of arguments, and pass them to the decorated function.
def changecase4(func):
        def inner(*args,**kwargs):
                return func(*args,**kwargs).upper()
        return inner
@changecase4
def func4(nam):
        return "Hello " + nam
print(func4("Harsh Antil"))
print("")

#Decorator With Arguments
#Decorators can accept their own arguments by adding another wrapper level.
#A decorator factory that takes an argument and transforms the casing based on the argument value.
x = int(input("Enter value of decorator argument:"))
def decorator(x):
        def changecase(func):
                def inner():
                        if x in (1,2) : #a way to check for or values , could be mutliple ,or we could also use x == 1 or 2
                                a = func().upper()
                        else : 
                                a = func().lower()
                        return a
                return inner
        return changecase
@decorator(x)
def func():
        return "Argument1"
print(func())
print("")

#Multiple Decorators
#You can use multiple decorators on one function.
#This is done by placing the decorator calls on top of each other.
#Decorators are called in the reverse order, starting with the one closest to the function.
def change(func):
        def inner():
                return func().upper()
        return inner
def addgreeting(func):
        def inner():
                return f"Good Morning {func()}."
        return inner
@addgreeting
@change
def function():
        return "Harsh"
print(function())

#Preserving Function Metadata
#Functions in Python has metadata that can be accessed using the __name__ and __doc__ attributes.
#Normally, a function's name can be returned with the __name__ attribute:
def myfunc():
        return "hlo wrld"
print(myfunc.__name__)
print("")

#But, when a function is decorated, the metadata of the original function is lost.
def cha(func):
        def inner():
                return func().upper()
        return inner
@cha
def newfunc():
        return "Hello World"
print(newfunc.__name__)
print("")

#To fix this, Python has a built-in function called functools.wraps that can be used to preserve the original function's name and docstring.
import functools
def cha(func):
        @functools.wraps(func) #this is also added
        def inner():
                return func().upper()
        return inner
@cha
def newfunc():
        return "Hello World"
print(newfunc.__name__)