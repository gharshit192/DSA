'''
    Swap Two Numbers Without Talking as a third variable
'''


def swapTwoNum(a, b):
    a = a + b
    b = a - b
    a = a - b
    return a, b
    # print(a, b)


a = 2
b = 3
i = swapTwoNum(a, b)
print(i)
