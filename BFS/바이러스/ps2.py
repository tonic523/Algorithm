import sys
from collections import deque

def bfs():
    q = deque([1])
    result = -1
    while q:
        v_com = q.popleft()
        if visited[v_com]:
            continue
        else:
            visited[v_com] = 1
            v_coms = computers[v_com]
            q.extend(v_coms)
            result += 1
    return result

N = int(input())
computers = { k : [] for k in range(1, N+1)}
visited = [0] * (N+1)
for _ in range(int(input())):
    c1, c2 = map(int, sys.stdin.readline().rstrip().split())
    computers[c1].append(c2)
    computers[c2].append(c1)

print(bfs())