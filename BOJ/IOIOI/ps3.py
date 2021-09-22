import sys

input = sys.stdin.readline

N = int(input())
M = int(input())
S = input().rstrip()
pattern = 0
answer = 0
i = 1
while i < M - 2:
    if S[i-1] == "I" and S[i] == "O" and S[i+1] == "I":
        pattern += 1
        if pattern == N:
            answer += 1
            pattern -= 1
        i += 1
    else:
        pattern = 0
    i += 1
print(answer)
