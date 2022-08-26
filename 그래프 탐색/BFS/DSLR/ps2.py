import sys
from collections import deque

input = sys.stdin.readline

answer = []
for _ in range(int(input())):
    N, M = map(int, input().rstrip().split())
    queue = deque([(N, "")])
    visited = [False] * 10000
    visited[N] = True
    while queue:
        n, a = queue.popleft()
        if n == M:
            answer.append(a)
            break

        l_n = len(str(n))

        t = n * 2 if n * 2 < 10000 else (n*2) % 10000
        if not visited[t]:
            visited[t] = True
            queue.append((t, a+"D"))

        t = n - 1 if n != 0 else 9999
        if not visited[t]:
            visited[t] = True
            queue.append((t, a+"S"))

        if l_n != 4:
            t = n * 10
        else:
            t, d = divmod(n, 10 ** (l_n - 1))
            t += (d*10)
        if not visited[t]:
            visited[t] = True
            queue.append((t, a+"L"))

        if l_n == 1:
            t = n * 1000
        else:
            t, d = divmod(n, 10)
            t += (d * 1000)
        if not visited[t]:
            visited[t] = True
            queue.append((t, a+"R"))

print("\n".join(answer))