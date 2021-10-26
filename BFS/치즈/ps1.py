import sys
from collections import deque

input = sys.stdin.readline

move = (
        (1, 0),
        (-1, 0),
        (0, 1),
        (0, -1)
    )
N, M = map(int, input().rstrip().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().rstrip().split())))
time = 1
graph[0][0] = -1

def change_air(graph):
    visited = [[False] * M for _ in range(N)]
    visited[0][0] = True
    queue = deque([(0,0)])
    while queue:
        r, c = queue.popleft()
        for m in move:
            m_r = r + m[0]
            m_c = c + m[1]
            if 0 <= m_r < N and 0 <= m_c < M:
                if graph[m_r][m_c] != 1 and not visited[m_r][m_c]:
                    visited[m_r][m_c] = True
                    graph[m_r][m_c] = -1
                    queue.append((m_r, m_c))

def exist_cheeze():
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1:
                return True
    return False

def is_melt(r, c):
    cnt = 0
    for m in move:
        m_r = r + m[0]
        m_c = c + m[1]
        if graph[m_r][m_c] == -1:
            cnt += 1
    return True if cnt >= 2 else False

while exist_cheeze():
    change_air(graph)
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1 and is_melt(i, j):
                graph[i][j] = 0
    time += 1
print(time - 1)