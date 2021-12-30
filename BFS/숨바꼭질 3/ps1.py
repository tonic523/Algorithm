import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().rstrip().split())
queue = deque()

time = [0] * 100001
visited = [False] * 100001
queue.append((N, 0))

while queue:
    now, t = queue.popleft()
    # 동생 위치
    if now == K:
        time[now] = t
        print(t)
        break
    # 해당 위치 초기화
    time[now] = t
    visited[now] = True
    # 순간이동
    if 0 <= now * 2 <= 100000 and not visited[now*2]:
        queue.append((now * 2, t))
    # 1칸씩 이동
    m_now = [now-1, now+1]
    for i in m_now:
        if 0 <= i <= 100000 and not visited[i]:
            queue.append((i, t+1))