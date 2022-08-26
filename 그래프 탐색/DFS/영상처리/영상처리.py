import sys

input = sys.stdin.readline

sys.setrecursionlimit(10**6)


def makeGraph():
    graph = []
    for n in range(N):
        temp = []
        li = list(map(int, input().rstrip().split()))
        for i in range(len(li)):
            if i % 3 == 2:
                temp.append(li[i - 2] + li[i - 1] + li[i])
        graph.append(temp)
    T = int(input())
    for r in range(len(graph)):
        for c in range(len(graph[r])):
            graph[r][c] = True if (graph[r][c] / 3) >= T else False
    return graph


def dfs(r, c):
    global graph
    for r_d, c_d in d_list:
        r_m = r + r_d
        c_m = c + c_d
        if 0 <= r_m < N and 0 <= c_m < M:
            if graph[r_m][c_m]:
                graph[r_m][c_m] = False
                dfs(r_m, c_m)


N, M = map(int, input().rstrip().split())
graph = makeGraph()

result = 0
d_list = [(1, 0), (0, 1), (-1, 0), (0, -1)]

for r in range(len(graph)):
    for c in range(len(graph[r])):
        if graph[r][c]:
            result += 1
            dfs(r, c)

print(result)
