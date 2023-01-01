import sys
from collections import deque

input = sys.stdin.readline

move = (
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1), (0, 1),
        (1, -1), (1, 0), (1, 1)
    )


def solve(w, h):
    graph = []
    for _ in range(h):
        graph.append(list(map(int, input().rstrip().split())))

    count = 0
    for i in range(h):
        for j in range(w):
            if graph[i][j]:
                graph[i][j] = 0
                queue = deque([(i, j)])
                while queue:
                    now_h, now_w = queue.popleft()
                    for m in move:
                        m_h = now_h + m[0]
                        m_w = now_w + m[1]
                        if 0 <= m_h < h and 0 <= m_w < w and graph[m_h][m_w]:
                            graph[m_h][m_w] = 0
                            queue.append((m_h, m_w))
                count += 1

    return str(count)


result = []
while True:
    w, h = map(int, input().rstrip().split())
    if w == 0 and h == 0:
        break
    else:
        result.append(solve(w, h))

print("\n".join(result))
