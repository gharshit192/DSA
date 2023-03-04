nums = [1, 2, 3, 4, 5, 6, 7]


def rotate(nums, k):
    def reverse(nums, low, high):
        while low <= high:
            nums[low], nums[high] = nums[high], nums[low]
            low += 1
            high -= 1

    n = len(nums)
    k = k % n
    # first reverse it from starting to k element
    reverse(nums, 0, n - k - 1)
    # then  reverse it from  k element to end
    reverse(nums, n - k, n - 1)
    # now reverse the whole list
    reverse(nums, 0, n - 1)

rotate(nums,3)
print(nums)
