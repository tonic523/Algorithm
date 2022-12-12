import sys

input = sys.stdin.readline

def solve(n, l):
    if l > 100:
        return [-1]

    a, r = divmod(2*n - l*(l-1), 2*l)
    if r == 0:
        if a < r:
            return [-1]
        sequence = []
        for i in range(l):
            sequence.append(a+i)
        return sequence

    return solve(n, l+1)


N, L = map(int, input().rstrip().split())
print(*solve(N, L))
