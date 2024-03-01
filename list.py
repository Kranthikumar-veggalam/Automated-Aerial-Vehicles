list=[1,2,3,4,4,5]
print(list)

list.append(6)
print(list)

list.sort()
print(list)

list.sort(reverse=True)
print(list)

list.remove(4)
print(list)

list.pop(0)
print(list)

list1=list[0:2]
print(list1)

list2=list.copy()
print(list2)

list2.reverse()
print(list2)

print(list[0])
list.sort()
print(list)

print(list.count(4))
list.clear()
print(list)
