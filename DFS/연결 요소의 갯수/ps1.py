import sys

input = sys.stdin.readline

def sol11724():
    N, M = map(int, input().split())
    graph = [[] for _ in range(N + 1)]
    visited = [False] * (N+1)
    result = 0

    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    for n in range(1, N+1):
        if not visited[n]:
            dfs(graph, visited, n)
            result += 1
    print(result)

def dfs(graph, visited, n):
    visited[n] = True
    for p in graph[n]:
        if not visited[p]:
            dfs(graph, visited, p)


if __name__ == "__main__":
    sys.setrecursionlimit(2000)
    sol11724()