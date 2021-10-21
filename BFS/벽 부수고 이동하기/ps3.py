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

queue = deque([(0,0,1,0)])
visited = [[[False] * 2 for _ in range(M)] for _ in range(N)]
visited[0][0][0] = True
while queue:
    r, c, d, isBroken = queue.popleft()
    if r == N-1 and c == M-1:
        answer = d
        break
    for m in move:
        m_r = r + m[0]
        m_c = c + m[1]
        if 0 <= m_r < N and 0 <= m_c < M:
            if graph[m_r][m_c] == 0 and not visited[m_r][m_c][isBroken]:
                queue.append((m_r, m_c, d+1, isBroken))
                visited[m_r][m_c][isBroken] = True
            elif graph[m_r][m_c] == 1 and isBroken == 0:
                visited[m_r][m_c][1] = True
                queue.append((m_r,m_c,d+1,1))

print(answer if answer != 1e9 else -1)