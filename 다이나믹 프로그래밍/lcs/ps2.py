import sys

input = sys.stdin.readline

s1 = input().rstrip()
s2 = input().rstrip()

dp = [[0] * (len(s2)+1) for _ in range(len(s1)+1)]

for i in range(len(s1)):
    d_i = i+1
    for j in range(len(s2)):
        d_j = j+1
        if s1[i] == s2[j]:
            dp[d_i][d_j] = dp[d_i-1][d_j-1] + 1
        else:
            dp[d_i][d_j] = dp[d_i-1][d_j-1]
            dp[d_i][d_j] = max(*[dp[d_i-1][d_j-1], dp[d_i][d_j-1], dp[d_i-1][d_j]])
print(dp[len(s1)][len(s2)])