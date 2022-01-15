import sys

input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

numbers = sorted(list(map(int, input().rstrip().split())))
answer, visited = [], [False] * N

def dfs(size):
    if size == M:
        print(*answer)
        return
    t = -1
    for i in range(N):
        if visited[i] or t == numbers[i]:
            continue
        visited[i] = True
        answer.append(numbers[i])
        dfs(size+1)
        visited[i] = False
        t = answer.pop()

dfs(0)