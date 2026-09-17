#Given a matrix of integers, if an element is 0, set its entire row and column to 0.

def setZeroes(matrix):
    rows = set ()
    coluns = set ()
    matrixResult = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
    for x in range(0, len(matrix)):
        for y in range(0, len(matrix[0])):
            if matrix[x][y] == 0:
                rows.add(x)
                coluns.add(y)
    for x in range(0, len(matrix)):
        for y in range(0, len(matrix[0])):
            if x in rows or y in coluns:
                matrixResult[x][y] = 0
            else:
                matrixResult[x][y] = matrix[x][y]
    return matrixResult


matrix = [[2, 1, 3, 0, 2], [7, 4, 1, 3, 8], [4, 0, 1, 2, 1], [9, 3, 4, 0, 9]]
print(setZeroes(matrix))