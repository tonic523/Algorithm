import sys
import math

input = sys.stdin.readline

for _ in range(int(input())):
    M, N, x, y = map(int, input().rstrip().split())
    i = 0
    lcd = M * N // math.gcd(M,N)
    count = x
    while count <= lcd:
        temp = count % N
        temp = temp if temp != 0 else N
        if y == temp:
            break
        i += 1
        count = x + (M * i)

    if count > lcd:
        print(-1)
    else:
        print(count)