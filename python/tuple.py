#tuple is ordered , unchangeble, contains duplicate -> only for reading values
shoeSize = (5,6,7,8,9,10)
print(shoeSize)

print(shoeSize.__contains__(6))

#single element treat as int
tuple1 = (6)
print(type(tuple1))

# treat this as tuple
tuple1 = (6,)
print(type(tuple1))

tuple2 = (4,5)
print(type(tuple2))

print(8 in shoeSize)

y = list(tuple2)
y.append(7)
z = tuple(y)
print(z)

print(tuple1+tuple2)

for size in shoeSize:
    print(size)

for i in range(len(shoeSize)):
    print(shoeSize[i], end= ' ')

print()

#unpacking list of tuple or list of list
for first ,second in [(1,2), (3,0), (4,5)]:
    print(first,second)
