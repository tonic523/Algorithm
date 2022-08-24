import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, M = map(int, input().rstrip().split())
    rowSumList = [0] * (N + 1)
    columnSumList = [0] * (N + 1)
    # 배열 생성
    for row_index in range(1, N + 1):
        row = list(map(int, input().rstrip().split()))
        rowSumList[row_index] = sum(row)
        for c in range(N):
            columnSumList[c + 1] += row[c]

    # 연산
    for _ in range(M):
        r1, c1, r2, c2, v = map(int, input().rstrip().split())
        row_add = (c2 - c1 + 1) * v
        column_add = (r2 - r1 + 1) * v
        for c in range(c1, c2 + 1):
            columnSumList[c] += column_add
        for r in range(r1, r2 + 1):
            rowSumList[r] += row_add

    # 출력
    print(*rowSumList[1:])
    print(*columnSumList[1:])
