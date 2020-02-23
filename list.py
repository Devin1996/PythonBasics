list = ["apple","banana","cherry","orange","kiwi","melon","mango"]
print(list)
print(list[1])
print(list[-1])
print(list[2:5])


list2=["apple","banana","cherry"]
list2[1]="blackcurrant"
print(list2)

for x in list:
    print(x)

print(len(list))

list3=["ac","ad","ed","dx","xf"]
list3.append("new")
print(list3)

list4=["ac","ad","ed","dx","xf"]
list4.insert(1, "new")
print(list4)

list5 = ["apple","banana","cherry","orange","kiwi","melon","mango"]
list5.remove("banana")
print(list5)

list6 = ["apple","banana","cherry","orange","kiwi","melon","mango"]
list6.pop()
print(list6)

list7 = ["apple","banana","cherry","orange","kiwi","melon","mango"]
del list7[0]
print(list7)

list8 = ["apple","banana","cherry","orange","kiwi","melon","mango"]
del list8

list9 = ["apple","banana","cherry","orange","kiwi","melon","mango"]
list9.clear()
print(list9)