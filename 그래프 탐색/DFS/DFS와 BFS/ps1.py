import sys
from collections import deque

input = sys.stdin.readline

def sol1260():
    N, M, V = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    def bfs(graph, v):
        result = []
        visited = [False] * (N + 1)
        queue = deque([v])
        while queue:
            now = queue.popleft()
            if not visited[now]:
                visited[now] = True
                result.append(str(now))
                nodes = sorted(graph[now])
                for node in nodes:
                    queue.append(node)
        return result

    def dfs(graph, v):
        result = []
        visited = [False] * (N + 1)
        stack = deque([v])
        while stack:
            now = stack.pop()
            if not visited[now]:
                visited[now] = True
                result.append(now)
                nodes = sorted(graph[now], reverse=True)
                stack += nodes
        return result

    print(" ".join(map(str, dfs(graph, V))))
    print(" ".join(map(str, bfs(graph, V))))

if __name__ == "__main__":
    sol1260()