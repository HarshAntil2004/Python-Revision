"""A function is a block of code which only runs when it is called.

A function can return data as a result.

A function helps avoiding code repetition."""

#a function is defined using the def keyword, followed by a function name and parentheses
def my_function():
        print("hello from the fn")

#calling a function
my_function()
my_function()
my_function() #can call mutliple times

"""Function name rules
A function name must start with a letter or underscore
A function name can only contain letters, numbers, and underscores
Function names are case-sensitive (myFunction and myfunction are different)"""

#return values
#If a function doesn't have a return statement, it returns None by default.

def values():
        return "Values"
message = values()
print(message)
print(values()) #can use directly

#Pass statement
#Function definitions cannot be empty. If you need to create a function placeholder without any code, use the pass statement

def my_functin() :
        pass