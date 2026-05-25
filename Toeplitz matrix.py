# function to check if diagonal elements are same
def checkDiagonal(mat, x, y):
    n, m = len(mat), len(mat[0])

    i, j = x + 1, y + 1
    while i < n and j < m:
        if mat[i][j] != mat[x][y]:
            return False
        i += 1
        j += 1
    return True

# Function to check whether given
# matrix is toeplitz matrix or not
def isToeplitz(mat):
    n, m = len(mat), len(mat[0])

    # check each descending diagonal starting from
    # first row and first column of the matrix

    for i in range(m):
        if not checkDiagonal(mat, 0, i):
            return False

    for i in range(n):
        if not checkDiagonal(mat, i, 0):
            return False

    return True

if __name__ == "__main__":
    mat = [
        [6, 7, 8],
        [4, 6, 7],
        [1, 4, 6]
    ]
    if isToeplitz(mat):
        print("true")
    else:
        print("false")
