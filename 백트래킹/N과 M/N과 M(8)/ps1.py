import sys

input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

numbers = sorted(list(map(int, input().rstrip().split())))

def solve(n, sequence):
    if len(sequence) == M:
        print(*sequence)
        return

    for i in range(n, N):
        temp = list(sequence)
        temp.append(numbers[i])
        solve(i, temp)

solve(0, list())