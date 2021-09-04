import sys

dp = [1,2,4]
result = []
for n in range(4, 12):
    dp.append(sum(dp[-3:]))

for _ in range(int(input())):
    result.append(str(dp[int(sys.stdin.readline().rstrip()) - 1]))
print("\n".join(result))