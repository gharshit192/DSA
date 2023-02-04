#set  -> unordered, unchangeable , or not-duplicate aslo no index because unordered


myset = {1,25,6,6,9}
print(myset)
print(type(myset))

for val in myset:
    print(val)
myset.add(60)
print(myset)

# No Indexing so can't use this gives error
"""
for i in range(len(myset)):
    print(myset[i])
"""

# union operator |  gives intersection
set1 = {1,2,3,5}
set2 = {1,6,8,5}
union = set1 | set2
print(union)