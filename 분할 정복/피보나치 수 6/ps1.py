import sys

input = sys.stdin.readline


def matrix_multiplication(matrix1, matrix2):
    result = [[0] * len(matrix2[0]) for _ in range(len(matrix1))]
    for i in range(len(matrix1)):
        for j in range(len(matrix1[0])):
            for k in range(len(matrix2[0])):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
            result[i][j] %= 1000000007
    return result


def solve(matrix, B):
    if B == 1:
        return matrix
    temp = solve(matrix, B // 2)
    t_matrix = matrix_multiplication(temp, temp)
    if B % 2 == 0:
        return t_matrix
    if B % 2 == 1:
        return matrix_multiplication(t_matrix, matrix)


M = [[1, 1], [1, 0]]
n = int(input())

Mn = solve(M, n)
print(Mn[0][1])
