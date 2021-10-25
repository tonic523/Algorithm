import sys

input = sys.stdin.readline

N = int(input())
graph = [
    [1, 1, 2, 2],
    [1, 3, 3, 2],
    [4, 3, 3, 5],
    [4, 4, 5, 5]
]
c, r = map(int, input().rstrip().split())

# 가운데 3에 위치한다면 패스
if graph[r-1][c-1] != 3:
    # 1 또는 2 타일 위치일 때
    if r - 1 < 2:
        # 1이라면(1,1)에 있는 3 값을 1로 초기화
        if c - 1 < 2:
            graph[1][1] = 1
        else:
            graph[1][2] = 2
    else:
        if c - 1 < 2:
            graph[2][1] = 4
        else:
            graph[2][2] = 5
graph[r-1][c-1] = -1

# 출력
for i in range(2**N-1, -1, -1):
    for j in range(2**N):
        print(graph[i][j], end=" ")
    print()