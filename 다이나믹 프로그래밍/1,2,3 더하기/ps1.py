import sys

dp = [0] * 12
dp[0] = 1
dp[1] = 1
result = []
for n in range(2, 12):
    if n-1 >= 0:
        dp[n] += dp[n-1]
        if n-2 >= 0:
            dp[n] += dp[n-2]
            if n-3 >= 0:
                dp[n] += dp[n-3]

for _ in range(int(input())):
    result.append(str(dp[int(sys.stdin.readline().rstrip())]))
print("\n".join(result))