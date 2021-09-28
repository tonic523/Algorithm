import math
import sys

input = sys.stdin.readline

N = int(input())
answer = 4

sqrt = int(math.sqrt(N))
for i in range(sqrt, 0, -1):
    N -= i ** 2
    if N == 0:
        answer = min(1, answer)
    sqrt2 = int(math.sqrt(N))
    for j in range(sqrt2, 0, -1):
        N -= j ** 2
        if N == 0:
            answer = min(2, answer)
        sqrt3 = int(math.sqrt(N))
        for k in range(sqrt3, 0, -1):
            N -= k ** 2
            if N == 0:
                answer = min(3, answer)
            elif N == 1:
                answer = min(4, answer)
            N += k ** 2
        N += j ** 2
    N += i ** 2
print(answer)