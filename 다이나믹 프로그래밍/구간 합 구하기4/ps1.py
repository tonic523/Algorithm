import sys

input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
li = list(map(int, input().rstrip().split()))
dp = [0] * (len(li) + 1)
for i in range(1, len(li) + 1):
    dp[i] = dp[i-1] + li[i-1]

answer = []
for _ in range(M):
    start, end = map(int, input().rstrip().split())
    answer.append(str(dp[end] - dp[start-1]))
print("\n".join(answer))