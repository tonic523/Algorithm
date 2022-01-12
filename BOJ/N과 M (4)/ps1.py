import sys

input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

def solve(n, sequence):
    if len(sequence) == M:
        print(*sequence)
        return

    for i in range(n, N+1):
        temp = list(sequence)
        temp.append(i)
        solve(i, temp)

solve(1, list())