import sys
import math

input = sys.stdin.readline

N, K = map(int, input().rstrip().split())

for _ in range(K-1):
    math_pow = math.pow(2, int(math.log2(N)))
    if N < math_pow:
        break
    elif N == math_pow:
        N = 0
        break
    N -= math_pow

x = 0
t = 1
while True:
    t = math.pow(2, x)
    if N == 0 or N == t:
        print(0)
        break
    elif N < t:
        print(int(t - N))
        break
    x += 1
