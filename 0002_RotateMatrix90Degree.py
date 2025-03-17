def displayMatrix(matrix):
    print("####################")
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            print(matrix[i][j], end=" ")
        print()
    print("####################")


def rotateMatrixCW(matrix):
    """
    Rotate all four corners of the matrix
    from 0 to half will rotate the matric
    90degree clockwise
    """
    displayMatrix(matrix)
    n = len(matrix)
    for i in range(int(n // 2)):
        for j in range(i, n - i - 1):
            # print(matrix[i][j], matrix[j][n - i - 1], matrix[n - i - 1][n - j - 1], matrix[n - j - 1][i])
            temp = matrix[i][j]
            matrix[i][j] = matrix[n - j - 1][i]
            matrix[n - j - 1][i] = matrix[n - i - 1][n - j - 1]
            matrix[n - i - 1][n - j - 1] = matrix[j][n - i - 1]
            matrix[j][n - i - 1] = temp
    displayMatrix(matrix)


def rotateMatrixACW(matrix):
    """
    Rotate all four corners of the matrix
    from 0 to half will rotate the matric
    90degree anti clockwise
    """
    displayMatrix(matrix)
    n = len(matrix)
    for i in range(int(n // 2)):
        for j in range(i, n - i - 1):
            # print(matrix[i][j], matrix[j][n - i - 1], matrix[n - i - 1][n - j - 1], matrix[n - j - 1][i])
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][n - i - 1]
            matrix[j][n - i - 1] = matrix[n - i - 1][n - j - 1]
            matrix[n - i - 1][n - j - 1] = matrix[n - j - 1][i]
            matrix[n - j - 1][i] = temp
    displayMatrix(matrix)


matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

rotateMatrixCW(matrix)


matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

rotateMatrixACW(matrix)

matrix = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12],
          [13, 14, 15, 16]]

rotateMatrixCW(matrix)


matrix = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12],
          [13, 14, 15, 16]]

rotateMatrixACW(matrix)


matrix = [[1, 2, 3, 4, 5],
          [6, 7, 8, 9, 10],
          [11, 12, 13, 14, 15],
          [16, 17, 18, 19, 20],
          [21, 22, 23, 24, 25]]

rotateMatrixCW(matrix)


matrix = [[1, 2, 3, 4, 5],
          [6, 7, 8, 9, 10],
          [11, 12, 13, 14, 15],
          [16, 17, 18, 19, 20],
          [21, 22, 23, 24, 25]]

rotateMatrixACW(matrix)
