import sys

input = sys.stdin.readline

def get_solve(n):
    result = n
    for c in str(n):
        result += int(c)
    return result

N = int(input().rstrip())
M = 0

for i in range(N):
    solve = get_solve(i)
    if solve == N:
        M = i
        break

print(M)