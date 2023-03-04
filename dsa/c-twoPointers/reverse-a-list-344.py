'''
    Reverse a list -> https://leetcode.com/problems/reverse-string/
'''

list = [1, 3, 4, 5]


def reverseAList(list):
    nums = []
    for i in range(len(list) - 1, -1, -1):
        nums.append(list[i])
    print(nums)
    return nums


reverseAList(list)

l2 = ["h","e","l","l","o"]
# Time -O(n) Spa e - O(1)
def reverseViaTwoPointer(list):
    low = 0
    high = len(list) - 1
    while low < high:
        list[low], list[high] = list[high], list[low]
        low = low + 1
        high = high - 1

    print(list)


reverseViaTwoPointer(l2)
