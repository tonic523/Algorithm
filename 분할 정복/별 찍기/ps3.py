import sys

input = sys.stdin.readline

N = int(input())
answer = [[" "] * (N*2) for _ in range(N)]

def print_star(point, n_size):
    global answer
    r, c = point
    if n_size == 3:
        answer[r][c] = "*"
        answer[r+1][c-1] = "*"
        answer[r+1][c+1] = "*"
        for i in range(3):
            answer[r+2][c+i] = "*"
            answer[r+2][c-i] = "*"
    else:
        n_size //= 2
        print_star((r, c), n_size)
        print_star((r+n_size, c-n_size), n_size)
        print_star((r+n_size, c+n_size), n_size)

print_star((0, N-1), N)

for row in answer:
    print("".join(row))