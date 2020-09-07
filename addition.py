def init_matrix(rows):
    matrix = []
    for i in range(rows):
        matrix.append(list(map(int, input().split())))
    return matrix


row_1, col_1 = map(int, input().split())
matrix_1 = init_matrix(row_1)
row_2, col_2 = map(int, input().split())
matrix_2 = init_matrix(row_2)

if row_1 == row_2 and col_1 == col_2:
    result = [[matrix_1[i][j] + matrix_2[i][j]
               for j in range(col_1)] for i in range(row_1)]
    for num in result:
        print(" ".join(map(str, num)))
else:
    print("ERROR")
