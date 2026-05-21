def diagonalTraversal(mat):
    n = len(mat)
    diag = [[] for _ in range(2 * n - 1)]

    # Store diagonals
    for i in range(n):
        for j in range(n):
            diag[i + j].append(mat[i][j])

    # Print result
    for d in range(2 * n - 1):
        for val in diag[d]:
            print(val, end=" ")

if __name__ == "__main__":
    mat = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

diagonalTraversal(mat)
