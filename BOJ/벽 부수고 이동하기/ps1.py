import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
graph = []
blocks = []
answer = 1e9
move = (
    (1,0),
    (-1,0),
    (0,1),
    (0,-1)
)
for _ in range(N):
    graph.append(list(map(int, list(input().rstrip()))))

for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            blocks.append((i, j))

while blocks:
    block = blocks.pop()
    graph[block[0]][block[1]] = 0
    queue = deque([(0,0,1)])
    visited = []
    while queue:
        r, c, d = queue.popleft()
        if r == N-1 and c == M-1:
            answer = min(answer, d)

        for m in move:
            m_r = r + m[0]
            m_c = c + m[1]
            if 0 <= m_r < N and 0 <= m_c < M:
                if graph[m_r][m_c] != 1:
                    if str(m_r) + str(m_c) not in visited:
                        queue.append((m_r,m_c,d+1))
                        visited.append(str(m_r)+str(m_c))
    graph[block[0]][block[1]] = 1

print(answer if answer != 1e9 else -1)