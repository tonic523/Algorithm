import sys
from collections import deque

input = sys.stdin.readline
points = [0]
N = int(input())
for _ in range(N):
    points.append(int(input()))
result = []
queue = deque()
queue.append((N, points[N], True))
while queue:
    now, point, b = queue.popleft()
    if now == 1:
        result.append(point)
    elif now == 2:
        if b:
            result.append(point + points[now-1])
        else:
            result.append(point)
    else:
        if b:
            queue.append((now - 1, point + points[now - 1], False))
        queue.append((now - 2, point + points[now - 2], True))
print(result)