import sys

input = sys.stdin.readline

N, K = map(int, input().rstrip().split())
coins = [int(input()) for _ in range(N)]
answer = 0

while K > 0:
    c = coins.pop()
    if K >= c:
        answer += K // c
        K %= c

print(answer)