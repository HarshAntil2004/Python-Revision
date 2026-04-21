#With the while loop we can execute a set of statements as long as a condition is true.

"""i = 1
while i<6 :
        print(i)
        i+=1
"""
#The while loop requires relevant variables to be ready, in this example we need to define an indexing variable, i, which we set to 1.

#break statement
#With the break statement we can stop the loop even if the while condition is true

"""i = 1
while i < 5 :
        print(i)
        if i == 3 :
                break
        i += 1
"""
#continue statement
#With the continue statement we can stop the current iteration, and continue with the next

"""i = 0
while i < 6 :
        i += 1
        if i == 3:
                continue
        print(i)"""

#else statement
#With the else statement we can run a block of code once when the condition no longer is true
#Note: The else block will NOT be executed if the loop is stopped by a break statement.

"""i = 0
while i < 6 :
        print(i)
        i += 1
else : print("Loop has ended")"""

