'''
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n,
representing the number of elements in nums1 and nums2 respectively.
Merge nums1 and nums2 into a single array sorted in non-decreasing order.
The final sorted array should not be returned by the function, but instead be stored inside the array nums1.
 To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged,
 and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

'''
from copy import copy


# T -> O(m+n) S -> O(m+n)
def merge(nums1, m, nums2, n):
    m = len(nums1)
    n = len(nums2)
    i = 0
    j = 0
    res = []
    while i < m and j < n:
        if nums1[i] == nums2[j]:
            res.append(nums1[i])
            res.append(nums2[j])
            i += 1
            j += 1
        elif nums1[i] < nums2[j]:
            if nums1[i] != 0:
                res.append(nums1[i])
                i += 1
            else:
                i += 1
        else:
            res.append(nums2[j])
            j += 1

    while i < m:
        res.append(nums1[i])
        i += 1
    while j < n:
        res.append(nums2[j])
        j += 1
    print(res)
    return res

nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
merge(nums1, m, nums2, n)
