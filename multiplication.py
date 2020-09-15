row_a, column_a = map(int, input().split())
matrix_a = []

for i in range(0, row_a):
    matrix_a.append([int(x) for x in input().split()])


multiplier = int(input())


for i in range(0, row_a):
    for j in range(0, column_a):
        matrix_a[i][j] *= multiplier
for x in matrix_a:
    print(' '.join(map(str, x)))
