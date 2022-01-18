import sys

input = sys.stdin.readline

N = int(input())
board = []
answer = 0

def dfs(count, board):
    if count == N:
        global answer
        answer += 1
        return

    attackable = update_attackable(count, board)
    for i in range(N):
        if not attackable[i]:
            dfs(count+1, board + [(count, i)])

def update_attackable(count, board):
    attackable = [False] * N
    for r, c in board:
        attackable[c] = True
        d = abs(r - count)
        if 0 <= c + d < N:
            attackable[c + d] = True
        if 0 <= c - d < N:
            attackable[c - d] = True
    return attackable

dfs(0, board)
print(answer)