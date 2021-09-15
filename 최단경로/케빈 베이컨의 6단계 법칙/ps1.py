import sys

input = sys.stdin.readline
INF = int(1e9)

N, M = map(int, input().split())
graph = [[INF] * (N+1) for _ in range(N+1)]

for i in range(N+1):
    graph[i][i] = 0

for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

for k in range(1, N+1):
    for a in range(1, N+1):
        for b in range(1, N+1):
            k_v = graph[a][k] + graph[k][b]
            graph[a][b] = graph[a][b] if graph[a][b] < k_v else k_v

result = []
for line in range(1, N+1):
    result.append(sum(graph[line]))
print(result.index(min(result)) + 1)