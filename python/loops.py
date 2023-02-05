a = 200
b = 100
c = 50


# if a > b > c:
#     print("ok")
# else:
#     print("els")


def c1():
    print("inside c1")
    return False


def c2():
    print("inside c2")
    return True


print(c1() and c2())
print(c1() or c2())
