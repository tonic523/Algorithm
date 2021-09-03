import sys
from collections import deque

paper = []
N = int(input())
for _ in range(N):
    paper.append(list(map(int, sys.stdin.readline().rstrip().split())))

q = deque([(0,0,N)])
result = [0, 0]
while q:
    r_f, c_f, size = q.popleft()
    white = 0
    blue = 0
    if size > 1:
        for r in range(r_f, r_f + size):
            for c in range(c_f, c_f + size):
                if paper[r][c] == 1:
                    blue += 1
                else:
                    white += 1
    else:
        if paper[r_f][c_f] == 1:
            blue += 1
        else:
            white += 1

    if white == 0:
        result[1] += 1
    elif blue == 0:
        result[0] += 1
    else:
        size //= 2;
        q.append((r_f, c_f, size))
        q.append((r_f, c_f + size, size))
        q.append((r_f + size, c_f, size))
        q.append((r_f + size, c_f + size, size))
for i in result:
    print(i)