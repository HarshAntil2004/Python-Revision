#Sets are unordered, so you cannot be sure in which order the items will appear.
#Once a set is created, you cannot change its items, but you can remove items and add new items.
#The values True and 1 are considered the same value in sets, and are treated as duplicates:
#The values False and 0 are considered the same value in sets, and are treated as duplicates:

thisset = {"apple", "banana", "cherry", False, True, 0}
print(thisset)

print(len(thisset))

#constructor
thissetnew = set(("apple","banana","cherry"))
print(thissetnew)

#Access
#1)using for loop
for x in thisset :
        print(x)

#2)using in or not in
print("banana" in thisset)
print("hello" not in thisset)

#Add items
#1)To add one item
thisset.add("added")
print(thisset)

#2)To add from another set ( can be any iterable in this )
newset = {"hello","world"}
list = [33,44]
newset.update(thisset)
newset.update(list)
print(newset)

#Remove items
#1)remove or discard method 
newset.remove("banana")
newset.discard("cherry")
print(newset)

#2)pop method You can also use the pop() method to remove an item, but this method will remove a random item, so you cannot be sure what item that gets removed.
#The return value of the pop() method is the removed item.
x = newset.pop()
print(x)

#clear() method empties the set
testclear = {"Testclear1","Testclear2"}
testclear.clear()
print(testclear)

#The del keyword will delete the set completely
#del testclear
#print(testclear) #will be an error because no such set exits anymore

#Loop sets
#1)for loop
for x in newset :
        print(x)

#2)while loop ( while loop cannot be used , because index would be used and index is not there in sets )

## JOIN SETS ##
#1)union() and update() methods joins all items from both sets. You can use the | operator instead of the union() method, and you will get the same result.
set1 = {"12","34","423","set2"}
set2 = {"set2","set22","set222"}
set22 = {"setnew","setneww","setnewww"}
set3 = set1.union(set2) #or set3 = set1 | set2
set7 = set1.union(set2,set22) #When using a method, just add more sets in the parentheses, separated by commas or set7 = set1 | set2 | set22
list = [38,534,634]
set7 = set1.union(set2,set22,list) #The union() method allows you to join a set with other data types, like lists or tuples. The  | operator only allows you to join sets with sets, and not with other data types like you can with the  union() method.
print(set3)
print(set7)

#update() The update() changes the original set, and does not return a new set.The update() method inserts all items from one set into another.
setwjn = {38993,4234,635}
setjfm = {344,53,632}
setwjn.update(setjfm)
print(setwjn)

#2)The intersection() method keeps ONLY the duplicates.You can use the & operator instead of the intersection() method, and you will get the same result.The & operator only allows you to join sets with sets, and not with other data types like you can with the intersection() method.
set4 = set1.intersection(set2) 
#or set4 = set1 & set2
print(set4)

#3)The difference() method keeps the items from the first set that are not in the other set(s).
set5 = set1.difference(set2)
#or set5 = set1 - set2
print(set5)

#4)The symmetric_difference() method keeps all items EXCEPT the duplicates.You can use the ^ operator instead of the symmetric_difference() method, and you will get the same result.
set6 = set1.symmetric_difference(set2)
#or set6 = set1 ^ set2
print(set6)

## frozenset()Like sets, it contains unique, unordered, unchangeable elements.#Unlike sets, elements cannot be added or removed from a frozenset.
m = frozenset({"mosquito","fly","bee"})
print(m)
print(type(m))

"""methods of frozenset
MethodShortcut	Description	
copy()	 	Returns a shallow copy	
difference()	-	Returns a new frozenset with the difference	
intersection()	&	Returns a new frozenset with the intersection	
isdisjoint()	 	Returns whether two frozensets have an intersection	
issubset()	<= / <	Returns True if this frozenset is a (proper) subset of another	
issuperset()	>= / >	Returns True if this frozenset is a (proper) superset of another	
symmetric_difference()	^	Returns a new frozenset with the symmetric differences	
union()	|	Returns a new frozenset containing the union	
"""

""" set methods Method	
Shortcut	Description
add()	 	Adds an element to the set
clear()	 	Removes all the elements from the set
copy()	 	Returns a copy of the set
difference()	-	Returns a set containing the difference between two or more sets
difference_update()	-=	Removes the items in this set that are also included in another, specified set
discard()	 	Remove the specified item
intersection()	&	Returns a set, that is the intersection of two other sets
intersection_update()	&=	Removes the items in this set that are not present in other, specified set(s)
isdisjoint()	 	Returns whether two sets have a intersection or not
issubset()	<=	Returns True if all items of this set is present in another set
 	<	Returns True if all items of this set is present in another, larger set
issuperset()	>=	Returns True if all items of another set is present in this set
 	>	Returns True if all items of another, smaller set is present in this set
pop()	 	Removes an element from the set
remove()	 	Removes the specified element
symmetric_difference()	^	Returns a set with the symmetric differences of two sets
symmetric_difference_update()	^=	Inserts the symmetric differences from this set and another
union()	|	Return a set containing the union of sets
update()	|=	Update the set with the union of this set and others"""

#challenge
colors = {"red","blue","green"}
print(colors)
colors.add("yellow")
colors.discard("green")
print(len(colors))