'''
Given two integer arrays nums1 and nums2, return an array of their intersection.
Each element in the result must be unique and you may return the result in any order.

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Explanation: [4,9] is also accepted.
'''


# T -> O m*n , S -> O(n)
def intersection(nums1, nums2):
    res = []
    for val1 in nums1:
        for val2 in nums2:
            if val1 == val2 and val1 not in res:
                res.append(val1)
    print(res)
    return res


# T -> O m+n , S -> O(n)
def intersection(nums1, nums2):
    setOf = set()
    for val2 in nums2:
        if val2 in nums1:
            setOf.add(val2)
            nums1.remove(val2)
    return list(setOf)


for nums1, nums2 in [
    ([1, 2, 2, 1], [2, 2]),
    ([4, 9, 5], [9, 4, 9, 8, 4]),
]:
    intersection(nums1, nums2)
