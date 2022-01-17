import sys

input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
numbers = list(map(int, input().rstrip().split()))
numbers.sort()

# dfs 순회
def dfs(sequence):
    if len(sequence) == M:
        print(*map(int, sequence))
        return

    for i in range(N):
        # 백 트래킹을 위한 조건
        if sequence[-1] <= numbers[i]:
            sequence.append(numbers[i])
            dfs(sequence)
            sequence.pop()

for i in range(N):
    dfs([numbers[i]])