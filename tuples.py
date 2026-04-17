mytuple = ("Apple" , "Banana" , "Mango")
print(mytuple)

print(len(mytuple))

#tuple with one item
mytuple2 = ("ONEITEM",)
print(type(mytuple2))

tuple1 = ("abc", 34, True, 40, "male")

#contructor
newtuple = tuple(("A","B","C"))
print(newtuple)

#access ( same as lists )
print(tuple1[0])
print(tuple1[0:3])
print(tuple1[-4:-1])
print(tuple1[1:])

if 34 in tuple1: #To check if present
        print("YES")

#To change value of tuple , ( First convert to list , change and convert back to tuple )
y = list(tuple1)
y[0] = "def"
tuple1 = tuple(y)
print(tuple1)

#Add items
#1)add items to a tuple
thistuple = ("apple", "banana", "cherry")
extendtuple = ("extended",)
y = list(thistuple)
y.append("orange")
y.insert(0,"inserted")
y.extend(extendtuple)
thistuple = tuple(y)
print(thistuple)

#2)add tuple to a tuple
thistuple += extendtuple
print(thistuple)

#Remove the items
#1)
y = list(thistuple)
y.remove("extended") #
y.pop(0) #
del y[0] #
thistuple = tuple(y)
print(thistuple)

#unpacking (can also do in lists)
#1)unpacking
fruits = ("apple", "banana", "cherry")
(a,b,c) = fruits #assigning multiple values to multiple variables at once
print(a)
print(b)
print(c)

#2)Using asterisk * #print a list like , cherry would be assigned to e and the first 2 or all the remaining in form of list in d
fruits2 = ("apple", "banana", "cherry")
(*d,e) = fruits2
print(d)
print(e)

#loops
#1)for loop simple
for x in fruits2 :
        print(x)

#2)for loop using index numbers
for x in range(len(fruits2)) :
        print(fruits2[x])

#3)while loop simple ( used index number directly here )
v = 0
while v < len(fruits2) :
        print(fruits2[v])
        v += 1


#Join tuples
fruits3 = fruits + fruits2
print(fruits3)

#Multiply tuples
fruits4 = fruits3 * 2
print(fruits4)

#tuple methods
#1)count() Returns the number of times a specified value occurs in a tuple
new = fruits4.count("cherry")
print(new)

#2)index() Searches the tuple for a specified value and returns the position of where it was found
new2 = fruits4.index("apple")
print(new2)

#Challenge exercise
fruitsch = ("apple","banana","cherry")
print(fruitsch[1])
print(len(fruitsch))
( a , b , c ) = fruitsch
print(b)