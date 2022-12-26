import sys

input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

prefix_sum_graph = [[0] * N for _ in range(N)]
for i in range(N):
    line = list(map(int, input().rstrip().split()))
    for j in range(N):
        temp = line[j]
        if i > 0:
            temp += prefix_sum_graph[i-1][j]
        if j > 0:
            temp += prefix_sum_graph[i][j-1]
        if i > 0 and j > 0:
            temp -= prefix_sum_graph[i-1][j-1]
        prefix_sum_graph[i][j] = temp

for _ in range(M):
    x1, y1, x2, y2 = map(lambda x: x-1, map(int, input().rstrip().split()))
    answer = prefix_sum_graph[x2][y2]
    if x1 > 0:
        answer -= prefix_sum_graph[x1-1][y2]
    if y1 > 0:
        answer -= prefix_sum_graph[x2][y1-1]
    if x1 > 0 and y1 > 0:
        answer += prefix_sum_graph[x1-1][y1-1]
    print(answer)
