import sys
from collections import deque
input = sys.stdin.readline
INF = 1e9

N, M = map(int, input().rstrip().split())
queue = deque([(1, 0)])
visited = [False] * 110
ladder_snake = {}
answer = 0
for _ in range(N+M):
    a, b = map(int, input().rstrip().split())
    ladder_snake[a] = b

while queue:
    answer += 1
    now, count = queue.popleft()
    if now == 100:
        print(count)
        break;
    for m in range(1, 7):
        m_now = now + m
        if ladder_snake.get(m_now):
            m_now = ladder_snake[m_now]
        if not visited[m_now]:
            queue.append((m_now, count+1))
            visited[m_now] = True