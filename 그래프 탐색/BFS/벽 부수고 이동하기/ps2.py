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

queue = deque([(0,0,1,True)])
visited = [[False] * M for _ in range(N)]
visited[0][0] = True
while queue:
    r, c, d, canBroke = queue.popleft()
    if r == N-1 and c == M-1:
        answer = min(answer, d)
    for m in move:
        m_r = r + m[0]
        m_c = c + m[1]
        if 0 <= m_r < N and 0 <= m_c < M:
            if graph[m_r][m_c] != 1 and not visited[m_r][m_c]:
                queue.append((m_r,m_c,d+1,canBroke))
                visited[m_r][m_c] = True
            elif graph[m_r][m_c] == 1 and canBroke:
                queue.append((m_r,m_c,d+1,False))

print(answer if answer != 1e9 else -1)