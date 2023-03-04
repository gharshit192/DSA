'''

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
'''


# Brute force approac- O(n^2)
def productExceptSelf(nums):
    length = len(nums)
    output = []
    leftProduct = 1
    for i in range(length):
        rightProduct = 1
        for j in range(i + 1, length):
            rightProduct *= nums[j]
        output.append(leftProduct * rightProduct)
        leftProduct *= nums[i]
    return output


for list in [
    [1, 2, 3, 4]
]:
    productExceptSelf(list)

# Time- O(n) Space O(3n)-> O(n)
def productExceptSelf(nums):
    length = len(nums)
    output = []
    leftProductArr = []
    leftProduct = 1
    rightProduct = 1
    rightProductArr = []
    for i in range(length):
        leftProductArr.append(leftProduct)
        leftProduct *= nums[i]
    print(leftProductArr)

    for j in range(length - 1, -1, -1):
        rightProductArr.append(rightProduct)
        rightProduct *= nums[j]
    print(rightProductArr)

    for k in range(length):
        output.append(leftProductArr[k] * rightProductArr[len(rightProductArr) - 1 - k])

    print(output)
    return output


for list in [
    [1, 2, 3, 4]
]:
    print(productExceptSelf(list))


# def productOfArraysWithoutSpace(nums):
#     n = len(nums)
#     res = [1]*n
#     for i in range(1, n):
#         res[i] = res[i-1]* nums[i-1]
#     right = 1
#     for i in range(n-1, -1,-1):
#         res[i] = res[i]*
