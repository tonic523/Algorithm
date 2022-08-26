import sys
from collections import deque
# 숨바꼭질
def sol1697():
    input = sys.stdin.readline
    N, K = map(int, input().split())
    visited = [False] * (int(1e5) + 1)
    if N == K:
        print(0)
    else:
        queue = deque()
        queue.append((N, 0))
        result = 0
        while queue:
            n, time = queue.popleft()

            if not visited[n]:
                visited[n] = True
            else:
                continue

            if n-1 == K or n+1 == K or n*2 == K:
                result = time + 1
                break
            if 0 <= n-1 <= 100000:
                queue.append((n - 1, time + 1))
            if 0 <= n + 1 <= 100000:
                queue.append((n + 1, time + 1))
            if 0 <= n * 2 <= 100000:
                queue.append((n * 2, time + 1))
        print(result)

if __name__ == "__main__":
    sol1697()