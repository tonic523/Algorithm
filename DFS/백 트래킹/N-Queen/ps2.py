import sys
import time

input = sys.stdin.readline


N = int(input())
answer = 0
cnt = 0
row = []

def validate(c, row):
    global cnt
    for n_r, n_c in enumerate(row):
        cnt += 1
        if abs(len(row)-n_r) == abs(c-n_c):
            return False
    return True

def dfs(row):
    if len(row) == N:
        print(len(row), row)
        global answer
        answer += 1
        return
    for i in range(N):
        if i not in row:
            if validate(i, row):
                dfs(row + [i])

start = time.time()
for i in range(N):
    dfs([i])
print(cnt, answer, "time :", time.time() - start)