import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
graph1 = []
graph2 = []
for _ in range(N):
    s1 = input().rstrip()
    graph1.append(list(s1))
    s2 = s1.replace("G", "R")
    graph2.append(list(s2))

def bfs(graph, s_r, s_c):
    move = (
        (1, 0),
        (-1, 0),
        (0, 1),
        (0, -1)
    )
    queue = deque([(s_r,s_c)])
    s_color = graph[s_r][s_c]
    graph[s_r][s_c] = "0"
    while queue:
        r, c = queue.popleft()
        for m in move:
            r_m = r + m[0]
            c_m = c + m[1]
            if 0 <= r_m < N and 0 <= c_m < N:
                if graph[r_m][c_m] == s_color:
                    graph[r_m][c_m] = "0"
                    queue.append((r_m, c_m))
    return graph

def sol(graph):
    answer = 0
    for r in range(N):
        for c in range(N):
            if graph[r][c] == "0":
                continue
            else:
                graph = bfs(graph, r, c)
                answer += 1
    return answer

print(sol(graph1), sol(graph2))