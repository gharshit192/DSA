def main(list):
    for val in list:
        print(val, end=" ")
    for val in list:
        print(val, end=" ")


lst = [
    [1, 2, 3],
    [1, 2, 3, 6, 7, 8],
    [1, 2, 3, 6],
    [1, 2, 3, 6, 8, 9, 29],
]
# main(lst)

'''
# RULE - 1  --> As time complexity for above program is O(n) or we have calculated O(2n) but as 2 is constant, so we ignore it
# RULE - 1  --> Drop the non-dominant term ie. f(n) -> n^2 + 2n + 7 -> so complexity for this is O(n^2)
'''


# Complexity will be O (m + n) where m, n are the length of list1 and list2
def main2(list, list2):
    for val in list:
        print(val, end=" ")
    for val in list2:
        print(val, end=" ")


# Here Complexity will be O(m*n)
def main3(list, list2):
    for val in list:
        for val2 in list2:
            print(val, val2, end=" ")


for list, list2 in [
    ([1, 2, 3], [4, 5, 6, 7]),

]:
    main3(list, list2)
    print()


def main4(a, b):
    sum = 0
    for i in range(b):
        sum += a

    print(sum)
    return sum


def main5(n):
    sum = 0
    while n:
        sum += n % 10
        n //= 10

    return sum


for n in [486]:
    print(main5(n))
