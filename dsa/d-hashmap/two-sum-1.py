'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
'''


# Time -O(n^2) Space O(n)
def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


nums = [2, 7, 11, 15]
target = 9
print(twoSum(nums, target))


# Time -O(n) Space O(n)
def twoSum(nums, target):
    map = {}
    for i in range(len(nums)):
        if map.__contains__(target - nums[i]):
            return [map.get(target - nums[i]), i]
        else:
            map.setdefault(nums[i], i)


nums = [2, 7, 11, 15]
target = 9
print(twoSum(nums, target))
