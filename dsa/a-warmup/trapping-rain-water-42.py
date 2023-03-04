'''
    Tapping Rain Water -> https://leetcode.com/problems/trapping-rain-water/
'''


# 10^4, 10^5 -> O(n)
# 1000 -> O(Log(n))
# 100 -> O(n^2)


# formula -> StoreCap ->min(max bar on right, max bar on left )* bar length - current bar

height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]


# This will create output fine but the b-complexity for this is O(n^2)
def trapWaterCapacity(height, barLength):
    totalStorageCapacity = 0
    for index in range(len(height)):

        maxOnLeft = max(height[:index + 1])
        maxOnRight = max(height[index:])

        totalStorageCapacity += (min(maxOnLeft, maxOnRight) - height[index]) * barLength

    print(totalStorageCapacity)
    return totalStorageCapacity


# O(n) Time Complexity
def trapWaterCapacity_2(height, barLength):
    totalStorageCapacity = 0
    n = len(height)

    leftMax = [0] * n
    leftMax[0] = height[0]
    for i in range(1, n):
        leftMax[i] = max(leftMax[i - 1], height[i])
    print(leftMax)

    rightMax = [0] * n
    rightMax[-1] = height[-1]
    # hence we have already taken last element in rightMax list
    for i in range(n-2, -1,-1):
        rightMax[i] = max(rightMax[i+1], height[i])
    print(rightMax)

    for index in range(len(height)):
        totalStorageCapacity += (min(leftMax[index], rightMax[index]) - height[index]) * barLength

    print(totalStorageCapacity)
    return totalStorageCapacity


trapWaterCapacity_2(height, 1)
