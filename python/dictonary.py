# Dictionary-> Unordered, changebale , no duplicate
# Keys can't be duplicate , value can be duplicate

# a = {
#     "class": "10",
#     "school": "HMS",
#     "topic": "DSA",
#     "area": "RMA",
#     "total": 5
# }
# print(a)
# print(type(a))
#
# # empty dictionary
# b = {}
# print(type(b))
# c = dict()
# print(type(c))
#
# # insertion and updation
# a["sex"] = "Male"
# print(a)
#
# a["topic"] = "Python DSA"
# print(a)
#
# # if key is not present than default value None
# y = a.get("topicc")
# print(y)
#
# # y = a.get("topicc", default= "Not Found")
# print(y)
#
# # set can have only hashable values, unhashable values not allowed
#
# # tuple can use as a key due to hasable
#
# # list can't be use as a key due to its unhashable
#
# allkeys = a.keys()
# print(allkeys)
#
# allvalues = a.values()
# print(allvalues)
#
# # list of key, value pair
# print(a.items())
#
# for key, value in a.items():
#     print(key, value)
#
# for key in a:
#     print(key, a[key])
#
# del a["total"]
#
# print(a)
# # tuples also contains in dict
# batch = {
#     "sub": "dsa",
#     (1, 2): ["NAME"],
#     "anotherBatch" : {
#         "sub" : "System Design"
#     }
# }

# print(batch)
# mybatch = batch.copy()
# newBatch = batch
#
# batch["NEW"] = "VALUE"
# print(mybatch)  # copy itself
# print(newBatch)  # using reference itself

#print(id(batch))
#print(id(mybatch))
#print(id(newBatch))

# print(id(batch["anotherBatch"]))
# print(id(mybatch["anotherBatch"]))
# print(id(newBatch["anotherBatch"]))


'''
If value is same copy method showing same address but instead of value change address will change
Also .copy will copy the value upto the one level
'''
from collections import defaultdict

batch = {
    "sub" : "system design",
    "course" : "learnbay"
}

# value = batch["new"]
# print(value)
key = "ifNoKeyIsPresent"
try:
    new = batch["new"]
except Exception as e:
    pass
    # batch[key] = "No DATA"


value = batch.get(key, "keyNotFound")
y = batch.setdefault(key, "hello")
print(value)
print(y)
print(batch)


#COUNTER

a = [2,4,4,7,9,9,7,3,5,5,1,2,1]
x = defaultdict(int)

x["name"] = 2
x["cat"] = 5
x["billi"] = 7

print(x["cow"])


