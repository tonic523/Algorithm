import sys

input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

graph = []

for i in range(N):
    graph.append(list(map(int, input().rstrip().split())))

# 누적합 연산
for i in range(N):
    for j in range(M):
        if i > 0:
            graph[i][j] += graph[i-1][j]
        if j > 0:
            graph[i][j] += graph[i][j-1]
        if i > 0 and j > 0:
            graph[i][j] -= graph[i-1][j-1]

for _ in range(int(input())):
    y1, x1, y2, x2 = map(lambda x: x-1, map(int, input().rstrip().split()))
    result = graph[y2][x2]
    if y1 > 0:
        result -= graph[y1-1][x2]
    if x1 > 0:
        result -= graph[y2][x1-1]
    if y1 > 0 and x1 > 0:
        result += graph[y1-1][x1-1]
    print(result)
