def foo(a, b):
    print(a, b)
    return a, b


output = foo(2, 4)

print(output)


class Student:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def getId(id):
        return id


s1 = Student(100, "Harshit")
print(s1.name)

id = Student.getId(10)
print(id)


class test:
    __privateVar = "27"

    def _privateMeth(self):
        print("Inside private")

    def hello(self):
        print("private value" + test.__privateVar)


test().hello()
test()._privateMeth()
