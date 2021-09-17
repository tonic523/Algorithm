import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int, list(input().rstrip()))))
result = []

def bfs(r, c):
    cnt = 0
    move = (
        (1, 0),
        (0, 1),
        (-1, 0),
        (0, -1)
    )
    queue = deque()
    queue.append((r,c))
    while queue:
        now_r, now_c = queue.popleft()
        if graph[now_r][now_c] == 0:
            continue
        graph[now_r][now_c] = 0
        cnt += 1
        for m in move:
            m_r = now_r + m[0]
            m_c = now_c + m[1]
            if 0 <= m_r < N and 0 <= m_c < N:
                if graph[m_r][m_c] == 1:
                    queue.append((m_r, m_c))
    return cnt

for r in range(N):
    for c in range(N):
        if graph[r][c] == 1:
            result.append(bfs(r,c))
result.sort()
print(len(result))
print("\n".join(map(str, result)))