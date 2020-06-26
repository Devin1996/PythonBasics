thislist = ["apple", "banana", "cherry"]
print(thislist)

#Access items
print(thislist[1])

#Negative indexing means beginning from the end, -1 refers to the last item, -2 refers to the second last item etc.
print(thislist[-1])

#Range of Indexes
thislist2 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist2[2:5])
print(thislist[:4])
print(thislist[2:])

#Range of Negative Indexes
print(thislist2[-4:-1])


#Change item value
thislist3 = ["apple", "banana", "cherry"]
thislist3[1] = "blackcurrant"
print(thislist3)

#Loop Through a List
for x in thislist3:
    print(x)

#Check if Item Exists
if "apple" in thislist3:
  print("Yes, 'apple' is in the fruits list")

#List Length
print(len(thislist3))

#add items
thislist3.append("orange")
print(thislist3)

#To add an item at the specified index, use the insert() method:
thislist3.insert(1, "Grapes")
print(thislist3)

#remove items
thislist4 = ["apple", "banana", "cherry"]
thislist4.remove("banana")
print(thislist4)

#The pop() method removes the specified index, (or the last item if index is not specified):
thislist5 = ["apple", "banana", "cherry"]
thislist5.pop()
print(thislist5)

#The del keyword removes the specified index:
thislist6 = ["apple", "banana", "cherry"]
del thislist6[0]
print(thislist6)

#The del keyword can also delete the list completely:
thislist7 = ["apple", "banana", "cherry"]
del thislist7

#The clear() method empties the list:

thislist8 = ["apple", "banana", "cherry"]
thislist8.clear()
print(thislist8)

#Make a copy of a list with the copy() method:
thislist9 = ["apple", "banana", "cherry"]
mylist = thislist9.copy()
print(mylist)

#Make a copy of a list with the list() method:

thislist10 = ["apple", "banana", "cherry"]
mylist2 = list(thislist10)
print(mylist2)

#Join two list:

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

#Append list2 into list1:

for x in list2:
  list1.append(x)

print(list1)

#Use the extend() method to add list2 at the end of list1:
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)

#Using the list() constructor to make a List:

thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)

# Method	Description
# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	Removes the element at the specified position
# remove()	Removes the item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list