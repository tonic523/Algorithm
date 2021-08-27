import sys
sys.setrecursionlimit(10**6)
def dfs(land,y,x):
    land[y][x] = 0
    for m in move:
        m_x = x + m[1]
        m_y = y + m[0]
        if M > m_x >= 0 and N > m_y >= 0:
            if land[m_y][m_x] == 1:
                land[m_y][m_x] = 0
                dfs(land,m_y,m_x)

move = (
    (0, 1),
    (1, 0),
    (0, -1),
    (-1, 0)
)

answers = []

for _ in range(int(input())):
    answer = 0
    M,N,K = map(int, sys.stdin.readline().rstrip().split())
    land = [[0] * M for _ in range(N)]
    for _ in range(K):
        x, y = map(int, sys.stdin.readline().rstrip().split())
        land[y][x] = 1
    for r, line in enumerate(land):
        for c, point in enumerate(line):
            if point == 1:
                dfs(land,r,c)
                answer += 1
    answers.append(str(answer))
print("\n".join(answers))