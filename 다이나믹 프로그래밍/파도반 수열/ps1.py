import sys

input = sys.stdin.readline

answer = []
dp = [0] * 101
dp[1] = 1
dp[2] = 1
dp[3] = 1
dp[4] = 2
dp[5] = 2
for _ in range(int(input())):
    N = int(input())
    for n in range(6, N+1):
        dp[n] = dp[n-5] + dp[n-1]
    answer.append(str(dp[N]))
print("\n".join(answer))