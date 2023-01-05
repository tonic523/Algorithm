import sys
from collections import deque

input = sys.stdin.readline

'''
dfs 로 탐색
'''


def dfs(r, c, k):
    global answer
    global visited
    if k == K:
        if (r, c) == (0, C-1):
            answer += 1
        else:
            return

    for m in move:
        m_r = r + m[0]
        m_c = c + m[1]
        if (m_r, m_c) not in visited and 0 <= m_r < R and 0 <= m_c < C and graph[m_r][m_c] != 'T':
            visited.append((m_r, m_c))
            dfs(m_r, m_c, k+1)
            visited.pop()


R, C, K = map(int, input().rstrip().split())
graph = []
for _ in range(R):
    graph.append(input().rstrip())

move = ((1, 0), (-1, 0), (0, 1), (0, -1))
answer = 0
visited = deque([(R-1, 0)])
dfs(R - 1, 0, 1)

print(answer)
