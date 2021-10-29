import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    answer = 0
    dp = [list(map(int, input().rstrip().split())) for _ in range(2)]
    if n == 1:
        print(max(dp[0][0], dp[1][0]))
        continue
    dp[0][1] += dp[1][0]
    dp[1][1] += dp[0][0]
    if n == 2:
        print(max(dp[0][1], dp[1][1]))
        continue
    for i in range(2, n):
        temp = max(dp[0][i-2], dp[1][i-2])
        dp[0][i] += max(temp, dp[1][i-1])
        dp[1][i] += max(temp, dp[0][i-1])
        answer = max(*[answer, dp[0][i], dp[1][i]])
    print(answer)