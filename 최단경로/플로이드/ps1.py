import sys

input = sys.stdin.readline

N = int(input())
graph = [[1e9] * (N) for _ in range(N)]
for _ in range(int(input())):
    s, e, c = map(int, input().rstrip().split())
    graph[s-1][e-1] = min(graph[s-1][e-1], c)

for i in range(N):
    graph[i][i] = 0

for i in range(N):
    for j in range(N):
        for k in range(N):
            graph[j][k] = min(graph[j][k], graph[j][i] + graph[i][k])

for r in graph:
    for c in r:
        print(c if c != 1e9 else 0, "", end="")
    print()