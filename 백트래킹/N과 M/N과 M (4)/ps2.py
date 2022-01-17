import sys

input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

# dfs 순회
def dfs(sequence):
    if len(sequence) == M:
        print(*sequence)
        return

    for i in range(1, N+1):
        # 백 트래킹을 위한 조건
        if sequence[-1] <= i:
            sequence.append(i)
            dfs(sequence)
            sequence.pop()

for i in range(1, N+1):
    dfs([i])