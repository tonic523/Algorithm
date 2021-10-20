import copy
import sys

input = sys.stdin.readline

N = int(input())
graph = []
for i in range(N):
    graph.append(list(map(int, input().rstrip().split())))

def get_point(graph, max_or_min):
    t_graph = copy.deepcopy(graph)
    for i in range(1, N):
        for j in range(3):
            temp = graph[i-1][j]
            if j - 1 >= 0:
                temp = max_or_min(temp, t_graph[i-1][j-1])
            if j + 1 < N:
                temp = max_or_min(temp, t_graph[i-1][j+1])
            t_graph[i][j] += temp
    return max_or_min(t_graph[N-1])

print(get_point(graph, max), get_point(graph, min))