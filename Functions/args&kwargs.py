"""By default, a function must be called with the correct number of arguments.
However, sometimes you may not know how many arguments that will be passed into your function.
*args and **kwargs allow functions to accept a unknown number of arguments.
"""

#Arbitrary Arguments - *args
#If you do not know how many arguments will be passed into your function, add a * before the parameter name.
#This way, the function will receive a tuple of arguments and can access the items accordingly
def func(*name):
        print("The name is:",name[2])
func("harsh","tannu","antil")

#The *args parameter allows a function to accept any number of positional arguments.
#Inside the function, args becomes a tuple containing all the passed arguments

#accessing elements
def func(*args):
        print("Type:",type(args))
        print("first arg:",args[0])
        print("second arg:",args[1])
        print("all arg:",args)
func(1,2,3,4)

def func(*args):
        for i in args:
                print(i)
func(12,32,4,2,53,5)

def func(*numbers):
        total = 0
        for i in numbers:
                total += i
        return total
print(func(1,2,3,4))

#Using *args with Regular Arguments
#You can combine regular parameters with *args.
#Regular parameters must come before *args
def func(greeting,*name):
        for i in name:
                print(greeting,i)
func("hello","Harsh","tannu")

#finding the max value
def func(*num):
        if len(num)==0:
                return None
        max = num[0]
        for i in num:
                if i>max:
                        max = i
        return max
print(func(1,2,3,4,9))

#Arbitrary Keyword Arguments - **kwargs
#If you do not know how many keyword arguments will be passed into your function, add two asterisks ** before the parameter name.
#This way, the function will receive a dictionary of arguments and can access the items accordingly

def func(**name):
        print("Name is:",name["fname"])
func(fname="harsh",lname="antil")

#The **kwargs parameter allows a function to accept any number of keyword arguments.
#Inside the function, kwargs becomes a dictionary containing all the keyword arguments

def func(**kwargs):
        print("type:",type(kwargs))
        print("First value:",kwargs["fname"])
        print("second value:",kwargs["lname"])
        print("all values:",kwargs)
func(fname="harsh",lname="antil",age=21)

#Using **kwargs with Regular Arguments
#You can combine regular parameters with **kwargs.
#Regular parameters must come before **kwargs

def func(age,**kwargs):
        print(f"Age is {age}")
        print("Additional details:")
        for key,value in kwargs.items():
                print(key + ":" ,value)
        print("\n")
func(21,fname="harsh",lname="antil",city="sonipat")

#Combining *args and **kwargs
"""You can use both *args and **kwargs in the same function.

The order must be:
regular parameters
*args
**kwargs
"""
def func(city,*args,**kwargs):
        print(f"City name is: {city}")
        print("Name is:",args[0])
        print("Surname is:",args[1])
        print("Positional arguments:",args)
        print("Additional details:")
        for i,value in kwargs.items():
                print(i + ":",value)
        print("Keyword arguments:",kwargs)
        print("\n")
func("Sonipat","Harsh","Antil",state="haryana",lifepath=22,ProjectName="Project2027",dream="G")

#Unpacking arguments of a list with * 
#If you have values stored in a list, you can use * to unpack them into individual arguments

def func(a,b,c):
        return a*b*c
numbers = [1,2,3]
result = func(*numbers)
print(result)
print("\n")

#Unpacking Dictionaries with **
#If you have keyword arguments stored in a dictionary, you can use ** to unpack them

def func(name,surname,age):
        print(f"Name is {name} and Surname is {surname}")
        print(f"Age is {age}")
data = {
        "name" : "Harsh",
        "surname" : "Antil",
        "age" : 21
}
func(**data)
func(name="Harsh",surname="antil",age=21)