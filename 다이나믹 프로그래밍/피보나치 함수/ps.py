import sys

dp = [[0, 0] for _ in range(41)]

for _ in range(int(input())):
    num = int(sys.stdin.readline().rstrip())
    for i in range(num+1):
        if i == 0:
            dp[0][0] = 1
        elif i == 1:
            dp[1][1] = 1
        else:
            dp[i][0] = dp[i-1][0] + dp[i-2][0]
            dp[i][1] = dp[i - 1][1] + dp[i - 2][1]
    print(" ".join(map(str, dp[num])))