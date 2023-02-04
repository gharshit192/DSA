# Dictionary-> Unordered, changebale , no duplicate
#Keys can't be duplicate , value can be duplicate

a= {
    "class" : "10",
    "school" : "HMS",
    "topic" : "DSA",
    "area" : "RMA",
    "total" : 5
}
print(a)
print(type(a))

# empty dictionary
b = {}
print(type(b))
c = dict()
print(type(c))

#insertion and updation
a["sex"] = "Male"
print(a)

a["topic"] = "Python DSA"
print(a)

#if key is not present than default value None
y = a.get("topicc")
print(y)

# y = a.get("topicc", default= "Not Found")
print(y)

# set can have only hashable values, unhashable values not allowed

# tuple can use as a key due to hasable

# list can't be use as a key due to its unhashable

allkeys = a.keys()
print(allkeys)

allvalues = a.values()
print(allvalues)

# list of key, value pair
print(a.items())


for key, value in a.items():
    print(key,value)

for key in a:
    print(key,a[key])

del a["total"]

print(a)
