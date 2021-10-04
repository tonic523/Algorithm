import sys
import heapq

input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().rstrip().split())))
visited = set()
answer = []
def dfs(r,c,value,visited):
    global answer
    move = (
        (1, 0),
        (-1, 0),
        (0, 1),
        (0, -1)
    )
    if len(visited) == 4:
        heapq.heappush(answer, -value)
        return

    for m in move:
        m_r = r + m[0]
        m_c = c + m[1]
        visited_v = str(m_r) + str(m_c)
        if 0 <= m_r < N and 0 <= m_c < M and visited_v not in visited:
            visited.add(visited_v)
            dfs(m_r, m_c, value+graph[m_r][m_c], visited)
            visited.remove(visited_v)

def tet(r, c):
    global answer
    if r + 2 < N and c + 1 < M:
        heapq.heappush(answer, -(graph[r][c] + graph[r + 1][c] + graph[r + 2][c] + graph[r + 1][c + 1]))
    if r + 2 < N and c - 1 >= 0:
        heapq.heappush(answer, -(graph[r][c] + graph[r + 1][c] + graph[r + 2][c] + graph[r + 1][c - 1]))
    if r + 1 < N and c + 2 < M:
        heapq.heappush(answer, -(graph[r][c] + graph[r][c + 1] + graph[r][c + 2] + graph[r + 1][c + 1]))
    if r - 1 >= 0 and c + 2 < M:
        heapq.heappush(answer, -(graph[r][c] + graph[r][c + 1] + graph[r][c + 2] + graph[r - 1][c + 1]))

for r in range(N):
    for c in range(M):
        visited.add(str(r)+str(c))
        dfs(r,c,graph[r][c],visited)
        visited.remove(str(r)+str(c))
        tet(r,c)

print(-answer[0])