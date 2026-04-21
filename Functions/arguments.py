"""Information can be passed into functions as arguments.
Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, just separate them with a comma.
"""

def my_fn(fname) :
        print(fname + " Antil")
my_fn("Harsh")
my_fn("Tanmay")

#Parameters vs Arguments
"""From a function's perspective:
A parameter is the variable listed inside the parentheses in the function definition.
An argument is the actual value that is sent to the function when it is called."""

def my(name) : #name is parameter
        print(name + " antil")
my("harsh") #harsh is argument

#Number of arguments
"""By default, a function must be called with the correct number of arguments.
If your function expects 2 arguments, you must call it with exactly 2 arguments.
"""

def sum(a,b) :
        print("the sum is :",a+b)
sum(1,1919)

#Default parameter values
#You can assign default values to parameters. If the function is called without an argument, it uses the default value

def myname(name = "friend") :
        print("Hello ",name)
myname("Harsh")
myname()

#Keyword arguments
#You can send arguments with the key = value syntax
#The phrase Keyword Arguments is often shortened to kwargs in Python documentation.

def dict(Car,Model) :
        print("The Car name is :",Car + " And the Model is :",Model)
dict(Car="Porsche",Model=911)
dict(Model=922,Car="Porsche") #This way, with keyword arguments, the order of the arguments does not matter.

#Positional arguments
#When you call a function with arguments without using keywords, they are called positional arguments.
#Positional arguments must be in the correct order:

def ani(animal,name) : #Python allows a function parameter to have the same name as the function itself, but it’s usually a bad idea in practice Breaks recursion and function reuse , Can cause unexpected bugs
        print("I have a",animal)
        print("Its name is",name)
ani("Dog","buddy")

#Mixing positional and keyword arguments
#You can mix positional and keyword arguments in a function call.
#However, positional arguments must come before keyword arguments:

def car(make,model,name) :
        print("I have a ",make,"made ",name,"car of model ",model)
car(2022,name="Porsche",model=911)

#passing different data types
#You can send any data type as an argument to a function (string, number, list, dictionary, etc.).
#The data type will be preserved inside the function

def my_function(fruits) :
        for i in fruits :
                print(i)
my_fruits = ['apple','banana','mango']
my_function(my_fruits)

def dic(person) :
        print("Name" , person["Name"])
        print("Age" , person["Age"])
my_dic = {"Name" : "Harsh" , "Age" : 21}
dic(my_dic)

#Return values
#Functions can return values using the return statement

def calc(x,y) :
        return x + y
result = calc(1,2)
print(result)

#Returning different data types
#Functions can return any data type, including lists, tuples, dictionaries, and more.

def type() :
        return ["Apple","Banana","Cherry"]
result = type()
print(result[0])
print(result[1])
print(result[2])

def tup() :
        return (10,20)
x,y = tup()
print(x)
print(y)

#positional only arguments
#To specify positional-only arguments, add , / after the arguments:
#Without the , / you are actually allowed to use keyword arguments even if the function expects positional arguments
def func(name,/) :
        print("Name is:",name)
func("harsh")

#Keyword only arguments
#To specify that a function can have only keyword arguments, add *, before the arguments

def func(*,name) :
        print("Name is:",name)
func(name="harsh")

#Combining positional only and keyword only

def func(name,/,*,age) :
        print("Name is:",name," and age is:",age)
func("harsh",age=21)

