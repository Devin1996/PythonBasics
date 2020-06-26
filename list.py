list = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(list)
print(list[1])
print(list[-1])
print(list[2:5])

list2 = ["apple", "banana", "cherry"]
list2.pop(1)
list2[1] = "blackcurrant"
print(list2)

for x in list:
    print(x)

print(len(list))

list3 = ["ac", "ad", "ed", "dx", "xf"]
list3.append("new")
print(list3)

list4 = ["ac", "ad", "ed", "dx", "xf"]
list4.insert(1, "new")
print(list4)

list5 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
list5.remove("banana")
print(list5)

list6 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
list6.pop()
print(list6)

list7 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
del list7[0]
print(list7)

list8 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
del list8

list9 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
list9.clear()
print(list9)

List0515 = ["apple","banana","cherry"]
for x in List0515:
    print(x)

print(len(List0515))

List0516 = ["apple","banana","cherry"]
for y in List0516:
    print(y)

List0517 = ["apple","banana","cherry"]
List0517.append("Orange")
print(List0517)

List0518 = ["apple","banana","cherry"]
List0518.insert(1,"Grapes")
print(List0518)

List0519 = ["apple","banana","cherry"]
List0519.insert("apple")
print(List0519)

List0520 = ["apple","banana","cherry"]
List0520.pop()
print(List0520)
#remove the last index

List123 = ["apple","banana","cherry"]
del List123[0]
print(List123)
