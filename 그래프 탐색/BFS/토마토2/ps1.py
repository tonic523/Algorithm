import sys
from collections import deque

input = sys.stdin.readline

def sol7569():
    C, R, H = map(int, input().split())
    graph = [[[] for _ in range(R)] for _ in range(H)]
    for h in range(H):
        for r in range(R):
            temp = list(map(int, input().split()))
            graph[h][r] = temp

    def bfs(graph):
        move = (
            (1, 0, 0),
            (0, 1, 0),
            (0, 0, 1),
            (-1, 0, 0),
            (0, -1, 0),
            (0, 0, -1)
        )
        max_time = 0

        def isRange(value, range):
            return True if 0 <= value < range else False

        queue = deque()
        for h in range(H):
            for r in range(R):
                for c in range(C):
                    if graph[h][r][c] == 1:
                        queue.append((h,r,c))

        while queue:
            h, r, c = queue.popleft()
            for m in move:
                m_h = h + m[0]
                m_r = r + m[1]
                m_c = c + m[2]
                if isRange(m_h, H) and isRange(m_r, R) and isRange(m_c, C):
                    if graph[m_h][m_r][m_c] == 0:
                        graph[m_h][m_r][m_c] = graph[h][r][c] + 1
                        max_time = max_time if max_time > graph[m_h][m_r][m_c] else graph[m_h][m_r][m_c]
                        queue.append((m_h, m_r, m_c))
        return max_time if max_time == 0 else max_time - 1

    time = bfs(graph)
    for h in range(H):
        for r in range(R):
            for c in range(C):
                if graph[h][r][c] == 0:
                    print(-1)
                    return
    print(time)

if __name__ == "__main__":
    sol7569()