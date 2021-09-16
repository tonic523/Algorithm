import sys
from collections import deque
input = sys.stdin.readline

move = (
    (1,0),
    (0,1),
    (-1,0),
    (0,-1)
)

R, C = map(int, input().rstrip().split())
graph = []
for _ in range(R):
    graph.append(list(map(int, list(input().rstrip()))))

queue = deque()
queue.append((0,0))
while queue:
    r,c = queue.popleft()
    for m in move:
        m_r = r + m[0]
        m_c = c + m[1]
        if 0 <= m_r < R and 0 <= m_c < C and graph[m_r][m_c] != 0:
            if graph[m_r][m_c] == 1 or graph[m_r][m_c] > graph[r][c] + 1:
                graph[m_r][m_c] = graph[r][c] + 1
                queue.append((m_r, m_c))
print(graph[R-1][C-1])