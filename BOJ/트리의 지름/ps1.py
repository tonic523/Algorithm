import sys
from collections import deque
import heapq

input = sys.stdin.readline

V = int(input())
tree = [[] for _ in range(V+1)]
answer = []
visited = set()
for _ in range(V):
    s = list(map(int, input().rstrip().split()))
    temp = 0
    for i, n in enumerate(s[1:]):
        if n == -1:
            break
        elif i % 2 == 0:
            temp = n
        else:
            tree[s[0]].append((temp, n))

for t in range(1, V+1):
    queue = deque([(t, 0)])
    visited.add(t)
    while queue:
        now, distance = queue.popleft()
        for v, d in tree[now]:
            if v not in visited:
                visited.add(v)
                queue.append((v, distance + d))
        heapq.heappush(answer, -distance)
    visited.clear()
print(-heapq.heappop(answer))