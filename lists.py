mylist = ["A","B","C"]
list1 = [1,2,3]
list2 = [True,False]
finallist = [1,"Hello",True,3.5]

print(mylist)

print(len(mylist))

print(type(mylist))

#constructor
constructorlist = list((33,44,55))
print(constructorlist)

#Access in lists
print(list1[2])
print(finallist[1:3])
print(list2[-1])
print(list1[:2])
print(finallist[0:])
print(finallist[-3:-1])

#check if present in list
if True in finallist :
        print("Yes the item is present\n")

#change item value
list1[1] = 4
print(list1)

finallist[1:3] = ["World" , False]
#Slice assignment (list[a:b] = [...]) replaces the slice completely—so the list grows if you add more items, shrinks if you add fewer, with no size restriction.
print(finallist)

#insert new item
mylist.insert(1,"inserted")
print(mylist)

#add item at last
mylist.append("Apended")
print(mylist)

#to add another list to another (can add any iterable)
mylist.extend(list2)
print(mylist)

#remove item from a list
mylist.remove("A")
print(mylist)

#remove specified index ( removes last item if index not specified ) / can also use del keyword
mylist.pop(0)
del mylist[0]
print(mylist)

#empty the list but the list remains
mylist.clear()
print(mylist)

#for loop for list
for x in finallist :
        print(x)

#looping by using index numbers
for i in range(len(finallist)) :
        print(finallist[i])

#while loop
v = 0
while v < len(finallist) :
        print(finallist[v])
        v += 1

#list comprehension
[print(x) for x in finallist ]

###List comprehension has some doubts , study it again later

#sorting the list ( sort is case sensitive , sorting capital letters before small letters )
newlist = [ 3 , 645 , 12 , 55 , 5 ]
newlist2 = ["banana", "Orange", "Kiwi", "cherry"]
newlist.sort()
print (newlist)

#Case insesitive sort using built in key function
newlist2.sort(key = str.lower)
print(newlist2)

newlist.sort(reverse=True) #In descending order
print(newlist)

#customise sort function by using a key
def myfunc(n) :
        return abs (n-50) #sort based on how close the number is to 50
newlist.sort(key = myfunc)
print(newlist)


#reversing a list
newlist.reverse()
print(newlist)

#Copy a list
listcopy = newlist.copy()
print(listcopy)

listcopy2 = list(listcopy) #another built in method to copy
print(listcopy2)

listcopy3 = listcopy[:] #another one
print(listcopy3)

#join 2 lists
joinedlist = listcopy2 + listcopy3
print(joinedlist)

for x in listcopy3 : #another method
        listcopy2.append(x)
print(listcopy2)

listcopy2.extend(listcopy3) #another method
print(listcopy2)