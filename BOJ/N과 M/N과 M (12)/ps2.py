import sys

input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
numbers = list(set(map(int, input().rstrip().split())))
numbers.sort()
sequence = []

# dfs 순회
def dfs(count):
    if count == M:
        print(*map(int, sequence))
        return

    for n in numbers:
        # 백 트래킹을 위한 조건
        if sequence and sequence[-1] > n:
            continue

        sequence.append(n)
        dfs(count + 1)
        sequence.pop()

dfs(0)