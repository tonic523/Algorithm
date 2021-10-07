import sys

input = sys.stdin.readline

graph = [[0,0,0]]
N = int(input())
for _ in range(N):
    graph.append(list(map(int, input().rstrip().split())))

for i in range(1, N+1):
    graph[i][0] += min(graph[i-1][1], graph[i-1][2])
    graph[i][1] += min(graph[i-1][0], graph[i-1][2])
    graph[i][2] += min(graph[i-1][0], graph[i-1][1])
print(min(graph[N]))