import sys

input = sys.stdin.readline
points = []
dp = []
N = int(input())
for _ in range(N):
    points.append(int(input()))

dp.append(points[0])
if N >= 2:
    dp.append(points[1] + points[0])
if N >= 3:
    dp.append(max(points[0], points[1]) + points[2])

for i in range(3, N):
    dp.append(max(dp[i-3] + points[i-1], dp[i-2]) + points[i])
print(dp[N-1])