# List.py Is ordered, changebale, contains duplicate
from collections import deque
from copy import deepcopy

myList = ["abc", "def", "ghi", "jkl,'mno"]

# myList.sort()
myList.sort()
print(myList)

print(myList[-3:-1])

# doesn't make sense hence starting index is greater than last index
print(myList[5:2])
print(myList[2:3])

# travel is possible only from left to right -> no backward possibility of traversing
print(myList[-1:2])

''' Membership Operator
    in -> Inside the collections
    not -> Not in collections
'''
if ('learnbay' in myList):
    print("YES")
else:
    print("No")

# replace is done character by charter
myList[3:5] = "changed"
print(myList)

# replace is done fully
myList[3:5] = ["changed"]
print(myList)

myList[3:5] = ["changed", "new", "my"]
print(myList)

myList.insert(3, "HARSHIT")
print(myList)

# range(start, stop , step)
print(list(range(0, 4, 2)))
n = len(myList)
print(n)
for i in range(n):
    print(i, myList[i])

for i, val in enumerate(myList):
    print(i, val, end=' ')
print()
# return in pair
print(list(enumerate(myList)))

# reverse
myList.reverse()
print(myList)

# list concatination
list1 = [2, [4,8], 5]
list2 = [2, 4, 6]
list3 = list1 + list2
print(list3)

list4 = deepcopy(list1)
list1.pop()
print(list1)

any = deque([1,2,3,4])
print(any)

any.pop()
any.popleft()
any.appendleft(6)
print(any)
print()
print()
print()

l1 = [2,4,5]
l2 = [2,4,5]

print(l1 == l2)

s1 = "harshit"
s2 = "harshit"

print(s1 ==s2)

print(s1 is s2)

