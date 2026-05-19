def is_magic_square(mat):
    n = len(mat)  
    target = n * (n*n + 1) // 2

    visited = [0] * (n*n + 1)

    d1 = d2 = 0

    for i in range(n):
        row_sum = col_sum = 0

        for j in range(n):
            val_row = mat[i][j]
            val_col = mat[j][i]

            # range + duplicate check
            if val_row < 1 or val_row > n*n or visited[val_row]:
                return False
            visited[val_row] = 1

            row_sum += val_row
            col_sum += val_col

            # diagonals
            if i == j:
                d1 += val_row
            if i + j == n - 1:
                d2 += val_row

        if row_sum != target or col_sum != target:
            return False

    return d1 == target and d2 == target
