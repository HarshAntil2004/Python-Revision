#A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
#This is less like the for keyword in other programming languages, and works more like an iterator method as found in other object-orientated programming languages.
#With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.

fruits = [ "apple","banana","mango","cherry"]
for i in fruits :
        print(i)

#The for loop does not require an indexing variable to set beforehand.

a = "banana"
for i in a :
        print(i)

#break statement
#With the break statement we can stop the loop before it has looped through all the items.

for i in fruits :
        print(i)
        if i == "mango" : #mango will be printed
                break

for i in fruits :
        if i == "mango" : #mango will not be printed
                break
        print(i)

#continue statement
#With the continue statement we can stop the current iteration of the loop, and continue with the next.
#for continue statement , it has to be before print else it woudlnt work.

fruits2 = ["mango","grapes","watermelon"]
for i in fruits2 :
        if i == "grapes" :
                continue
        print(i)

#range() function
#Note that range(6) is not the values of 0 to 6, but the values 0 to 5.

for x in range(6) :
        print(x)

#The range() function defaults to 0 as a starting value, however it is possible to specify the starting value by adding a parameter: range(2, 6), which means values from 2 to 6 (but not including 6)

for x in range(2,6) :
        print(x)

#The range() function defaults to increment the sequence by 1, however it is possible to specify the increment value by adding a third parameter: range(2, 30, 3).

for x in range (0,30,3) :
        print(x)

#else in for loop
#The else keyword in a for loop specifies a block of code to be executed when the loop is finished.

for x in range(5) :
        print(x)
        """if x == 4 :
                break"""
        
else :
        print("the loop has ended")

#Note: The else block will NOT be executed if the loop is stopped by a break statement.

#Nested loops
#The "inner loop" will be executed one time for each iteration of the "outer loop"

adj = ["red","big","tasty","sweet"]
fruits
for i in adj :
        for j in fruits :
                print(i,j) #Print each adjective for every fruit

#pass statement
#for loops cannot be empty, but if you for some reason have a for loop with no content, put in the pass statement to avoid getting an error.

for x in [0,1,2] :
        pass