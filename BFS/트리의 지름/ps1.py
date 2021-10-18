import sys
from collections import deque
import heapq

input = sys.stdin.readline

n = int(input())
tree = [[] for _ in range(n+1)]
for i in range(1, n):
    a, b, c = map(int, input().rstrip().split())
    tree[a].append((b, c))
    tree[b].append((a, c))

def bfs(start):
    distance = [(0, start)]
    visited = [False] * (n+1)
    queue = deque([(start, 0)])

    while queue:
        now, c = queue.popleft()
        visited[now] = True
        for v, cost in tree[now]:
            if not visited[v]:
                cost += c
                heapq.heappush(distance, (-cost, v))
                queue.append((v, cost))
    return heapq.heappop(distance)

start = bfs(1)[1]
print(-bfs(start)[0])