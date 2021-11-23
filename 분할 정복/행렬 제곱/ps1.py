import sys

input = sys.stdin.readline

n, b = map(int, input().rstrip().split())

def solve(a, b):
    if b == 1:
        return a
    temp = solve(a, b//2)
    matrix = matrix_multiply(temp, temp)
    if b % 2 == 0:
        return matrix
    return matrix_multiply(matrix, a)

def matrix_multiply(matrix1, matrix2):
    result = [[0] * n for _ in range(n)]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                result[i][j] += (matrix1[i][k] * matrix2[k][j]) % 1000
                result[i][j] %= 1000
    return result

matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().rstrip().split())))

matrix = solve(matrix, b)

for r in range(n):
    for c in range(n):
        print(matrix[r][c] % 1000, end=" ")
    print()