def searchMatrix(mat, x):
    n = len(mat)
    m = len(mat[0])

    # traverse every element in the matrix
    for i in range(n):
        for j in range(m):
            if mat[i][j] == x:
                return True

    return False

if __name__ == "__main__":
    mat = [
        [1, 5, 9],
        [14, 20, 21],
        [30, 34, 43]
    ]
    x = 14
    print("true" if searchMatrix(mat, x) else "false")
