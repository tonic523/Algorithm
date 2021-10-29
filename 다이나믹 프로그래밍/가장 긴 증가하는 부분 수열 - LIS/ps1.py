import sys

input = sys.stdin.readline

n = int(input())
A = list(map(int, input().rstrip().split()))
dp = [1] * (n)

for i in range(n):
    temp = 0
    for j in range(i):
        if A[i] > A[j]:
            temp = max(temp, dp[j])
    dp[i] = temp+1
print(max(dp))