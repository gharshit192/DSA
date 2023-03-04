from python.exercise import List

matrix = [

    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]


def spiralOrder(matrix):
    rowMin, rowMax = 0, len(matrix) - 1
    colMin, colMax = 0, len(matrix[0]) - 1
    m = len(matrix)
    n = len(matrix[0])
    res = []
    while True:
        # Traversing from column 1 to last column in first row ,
        for i in range(colMin, colMax + 1):
            res.append(matrix[rowMin][i])
        if len(res) == m * n:
            break
        rowMin += 1

        # Traversing in column 3 to last row , now for 2 row but last column
        for i in range(rowMin, rowMax + 1):
            res.append(matrix[i][colMax])
        if len(res) == m * n:
            break
        colMax -= 1

        # Traversing the last column 3 to first row , now for colMax is decrement so that duplicate entry not allowed
        for i in range(colMax, colMin - 1, -1):
            res.append(matrix[rowMax][i])
        if len(res) == m * n:
            break
        rowMax -= 1

        # Traversing the first row as decrement it due to duplicates
        for i in range(rowMax, rowMin - 1, -1):
            res.append(matrix[i][colMin])
        if len(res) == m * n:
            break
        colMin += 1

    print(res)
    return res


for matrix in [
    [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ],
    [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [51, 43, 23, 65]
    ]
]:
    spiralOrder(matrix)
