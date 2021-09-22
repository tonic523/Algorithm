import sys

input = sys.stdin.readline

N = int(input())
M = int(input())
S = input().rstrip()
cnt = 0
p_n = "IOI"

for _ in range(N-1):
    p_n += "OI"

def is_p_n(i):
    t = 1
    for j in range(i+1, i+(2 * N + 1)):
        if p_n[t] != S[j]:
            return False
        t += 1
    return True

for i in range(M - (2 * N + 1)):
    if S[i] == "I" and is_p_n(i):
        cnt += 1

print(cnt)