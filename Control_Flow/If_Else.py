"""Basic syntax
Equals: a == b
Not Equals: a != b
Less than: a < b
Less than or equal to: a <= b
Greater than: a > b
Greater than or equal to: a >= b
"""

a = -384.32
b = -2214
if b < a :
        print("b is smaller than a")

#Boolean variables can be used directly in if statements without comparison operators.
is_valid_admin = True
if is_valid_admin :
        print("They are a valid admin")

x = 0
y = None #falsy but not false
z = "" #falsy but not false
a = False
if x == False :
        print("false for x")
if not y :
        print("falsy for y")
if not z :
        print("falsy for z")
if a == False :
        print("false for a")
print(bool(y))
print(bool(z))
        
"""1. if checks truth (not equality)
if x: → runs only if bool(x) is True
if not x: → runs if bool(x) is False

2. Falsy ≠ False
Falsy values: 0, None, "", [], etc. → behave like False in if
But they are not equal to False
None == False → False
"" == False → False

3. Only False is actually False
False is the real boolean
0 is just a special case where 0 == False happens to be True

if uses behavior (bool(x)), not actual value (x == False)
"""

#elif keyword
m = 23
n = 23
if m > 23 :
        print("m is greater")
elif m:=n :
        print("they are equal")

#multiple elif
score = 75
if score>=90:
        print("GradeA")
elif score>=80:
        print("GradeB")
elif score>=70:
        print("GradeC") 
elif score>=60:
        print("GradeD")

#Only the first true condition will be executed. Even if multiple conditions are true, Python stops after executing the first matching block.

#else
#taking the previous a , b code
if b > a:
        print("b is greater")
elif b==a:
        print("they are equal")
else :
        print("a is greater than b")
"""elif b :
        print("bool works")"""

#The else statement acts as a fallback that executes when none of the preceding conditions are true. This makes it useful for error handling, validation, and providing default values.

#short hand if
q = 10
w = 5
if w<q : print("w is smaller than q")

#short hand if-else
print("w greater than q") if w > q else print("w smaller") #This is called a conditional expression (sometimes known as a "ternary operator").

#assign value with if-else
ab = 33.4
bc = 32.1
bigger = bc if bc > ab else ab 
name,value = ("bc",32.1) if bc < ab else bc
print("bigger is ",bigger)
print(f"Smaller is {name} with value {value}")

#multiple conditions on one line
cd = 100
de = 100
print("cd") if cd > de else print("de") if de > cd else print("=")

#ternary operator ex
#name = (input("Please enter your name : "))
display_name = name if name else "guest"
print("welcome,",display_name)

"""Logical operators for if statements
and - Returns True if both statements are true
or - Returns True if one of the statements is true
not - Reverses the result, returns False if the result is true
"""
#Python evaluates not first, then and, then or.
a = 100
b = 50
c = 30
if a>b and a>c :
        print("a is the greatest")
if b>a or b>c :
        print("b has higher value once between the two")
if not a>b :
        print("not printed")

#combining all these in one
age = 18
is_student = False
have_voter_id = True
if (age>=18 and have_voter_id) and not is_student :
        print("the person can vote")

"""Truth tables
and Operator Truth Table
Condition 1	Condition 2	Result
True	        True	        True
True	        False	        False
False	        True	        False
False	        False	        False

or Operator Truth Table
Condition 1	Condition 2	Result
True	        True	        True
True	        False	        True
False	        True	        True
False	        False	        False

"""

#mini example for login check
username = "harsh"
password = 124
userinp = input("please enter you username : ")
userpass = int(input("please enter password : "))
is_valid = (username==userinp and password==userpass)
if username and password and is_valid :
        print("Login successfull")
else : print("failed")

#Nested if statements
#In this example, the inner if statement only runs if the outer condition (score > 10) is true.

score = 30
if score>10 :
        print("score above 10")
        if score>20 :
                print("score also above 20")
else : print("failed to analyse")

#example
score = 65
attendance = 70
submitted = True
if score>60 :
        if attendance > 75 :
                if submitted :
                        print("good marks")
                else : print("assignment missing")
        else : print("attendance is low")
else : print("score is low")

#Use nested if statements when the inner logic is complex or depends on the outer condition. Use and when both conditions are simple and equally important.

#pass statement
#The pass statement is a null operation - nothing happens when it executes. It serves as a placeholder.
"""The pass statement is useful in several situations:
When you're creating code structure but haven't implemented the logic yet
When a statement is required syntactically but no action is needed
As a placeholder for future code during development
In empty functions or classes that you plan to implement later
"""
a = 33 
b = 100
if a<b :
        pass

#While we focus on pass with if statements here, it's also commonly used with loops, functions, and classes.
def calculate_discount(price):
        pass # toadd: Implement discount logic

# Function exists but doesn't do anything yet