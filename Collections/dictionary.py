#Dictionaries cannot have two items with the same key (Duplicates Not Allowed)

thisdict = {
        "Name" : "Harsh" ,
        "Lifepath" : "Masternumber22" ,
        "Age" : 21 ,
        "Colors" : ["red","blue","green"]

}
print(thisdict)

#len()
print(len(thisdict))

#Constructor() Be careful of syntax , we do not put "" around keys , and instead of : we use =
newdict = dict(name = "Antil" , age = 21)
print(newdict)

## Accessing items 
print(thisdict["Name"])
print(thisdict["Colors"])

print(thisdict.get("Age")) #another method

## Get keys using key()
#The list of the keys is a view of the dictionary, meaning that any changes done to the dictionary will be reflected in the keys list.
print(thisdict.keys())

## Get values using value()
#The list of the values is a view of the dictionary, meaning that any changes done to the dictionary will be reflected in the values list.
print(thisdict.values())

## Get items using items()
#The returned list is a view of the items of the dictionary, meaning that any changes done to the dictionary will be reflected in the items list.
print(thisdict.items())

## Check if key exist using in keyword
if "Key" in thisdict :
        print("It is present")
else : print("false")

## Change values 
thisdict["Age"] = 22
print(thisdict["Age"])

## Update dictionary 
#The argument must be a dictionary, or an iterable object with key:value pairs.
thisdict.update({"Colors" : "white"})
thisdict.update(Age = (23,22,21))
print(thisdict["Colors"])
print(thisdict["Age"])
print(thisdict)

## Adding items
#The update() method will update the dictionary with the items from a given argument. If the item does not exist, the item will be added.
thisdict["Number"] = 939
thisdict.update({"Height" : 5.9})
print(thisdict)

## Removing items
#The pop() method removes the item with the specified key name:
thisdict.pop("Age")
print(thisdict)

#The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):
thisdict.popitem()
print(thisdict)

#The del keyword removes the item with the specified key name:
#The del keyword can also delete the dictionary completely: del thisdict
del thisdict["Colors"]
print(thisdict)

#The clear() method empties the dictionary:
#thisdict.clear()

## loop through
# for loop Print all key names in the dictionary, one by one:
for x in thisdict :
        print(x)

for x in thisdict.keys() : #another method for printing keys
        print(x)

for x in thisdict : 
        print(thisdict[x]) #print all values of keys

for x in thisdict.values() : #another method for printing values
        print(x)

for x,y in thisdict.items() :
        print(x,y)

## Copy a dictionary 
#There are ways to make a copy, one way is to use the built-in Dictionary method copy().
thisdict2 = thisdict.copy()
print(thisdict2)

#Another way to make a copy is to use the built-in function dict().
thisdict3 = dict(thisdict)
print(thisdict3)

## Nested dictionaries
myfamily = {
        "child1" : { #here : will be used instead of = because it is inside the dictionary itself
                "name" : "harsh",
                "age" : 20
        },
        "child2" : {
                "name" : "tanmay",
                "age" : 15
        }
}
print(myfamily)

#another method is to create separate dictionaries and then add them in a main one later
child3 = {
        "name" : "bunny",
        "age" : 33
}
child4 = {
        "name" : "bad",
        "age" : 34
}
myfamily2 = {
        "child3" : child3,
        "child4" : child4
}
print(myfamily2)

## Access items in a nested dictionary
print(myfamily["child1"]["name"])
print(myfamily2["child4"]["name"])

## for loops in nested dictionary
for x,obj in myfamily.items() :
        print(x)

        for y in obj :
                print(y + ":",obj[y])

"""
Method	Description
clear()	Removes all the elements from the dictionary
copy()	Returns a copy of the dictionary
fromkeys()	Returns a dictionary with the specified keys and value
get()	Returns the value of the specified key
items()	Returns a list containing a tuple for each key value pair
keys()	Returns a list containing the dictionary's keys
pop()	Removes the element with the specified key
popitem()	Removes the last inserted key-value pair
setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	Updates the dictionary with the specified key-value pairs
values()	Returns a list of all the values in the dictionary"""

## challenge
car = {
        "brand" : "Ford",
        "model" : "Mustang",
        "year" : 2024
}
print(car["model"])
car.update({"color":"red"})
car.pop("brand")
print(car)