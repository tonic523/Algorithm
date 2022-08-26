import sys

input = sys.stdin.readline
INF = 1e9

N, M = map(int, input().rstrip().split())
dp = [INF] * 101
ladder_snake = {}
for _ in range(N+M):
    a, b = map(int, input().rstrip().split())
    ladder_snake[a] = b
for i in range(2, 8):
    while True:
        if not ladder_snake.get(i):
            dp[i] = 1
            break
        else:
            i = ladder_snake[i]

for i in range(8, 101):
    m_i = i
    while ladder_snake.get(m_i):
        m_i = ladder_snake[m_i]
    for j in range(1, 7):
        if dp[i-j] != INF:
            dp[m_i] = min(dp[i-j] + 1, dp[m_i])
print(dp[100])