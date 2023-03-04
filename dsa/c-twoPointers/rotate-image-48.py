'''
    [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]
    You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
    You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.
    Output - [
                [7,4,1],
                [8,5,2],
                [9,6,3]
            ]

    Approach -> First do a transpose of the matrix than reverse all the rows
    so transpose ->
            [
                [1,4,7],
                [2,5,8],
                [3,6,9]
            ]
            Now reverse each row ->
            [
                [7,4,1],
                [8,5,2],
                [9,6,3]
            ]

'''


# Time- O(M X N) Space- O(1)
def rotateImage(matrix):
    m = len(matrix)
    n = len(matrix[0])
    for i in range(m):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    def reverseList(list):
        low = 0
        high = len(list) - 1
        while low < high:
            list[low], list[high] = list[high], list[low]
            low = low + 1
            high = high - 1

    for row in matrix:
        reverseList(row)
    print(matrix)


for matrix in [
    [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
]:
    rotateImage(matrix)
    [
        [1, 4, 7],
        [2, 5, 6],
        [3, 8, 9]
    ]
