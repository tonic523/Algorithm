import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
graph = [[True] * N for _ in range(N)]
move = (
    (1, 0),
    (1, 1),
    (1, -1),
)
answer = 0
# 퀸 놓기
def place_queen(r, c, graph):
    # 그래프 복사
    n_graph = [item[:] for item in graph]
    n_graph[r][c] = False
    n_graph[r] = [False] * N
    queue = deque([(r, c, 0), (r, c, 1), (r, c, 2)])

    while queue:
        r, c, m = queue.popleft()
        n_r = r + move[m][0]
        n_c = c + move[m][1]
        if 0 <= n_r < N and 0 <= n_c < N:
            n_graph[n_r][n_c] = False
            queue.append((n_r, n_c, m))

    return n_graph

stack = deque()
for c in range(N-1, -1, -1):
    stack.append((0, c, graph))

while stack:
    r, c, g = stack.pop()
    print(r,c)
    if r == N-1:
        answer += 1
        continue

    n_graph = place_queen(r, c, g)
    for i in range(N):
        if n_graph[r+1][i]:
            stack.append((r+1, i, n_graph))

print(answer)