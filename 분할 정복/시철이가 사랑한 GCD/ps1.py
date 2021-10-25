import sys
from math import gcd
from collections import deque

input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().rstrip().split()))
queue = deque([(0, N-1, 0)]) # 위치, 크기, 최대공약수 합
answer = 0
while queue:
    start, end, value = queue.popleft()
    size = end-start+1
    if size == 1:
        answer = max(answer, numbers[start]+value)
    else:
        mid_s = size // 2
        l_gcd = gcd(*numbers[start:start+mid_s])
        r_gcd = gcd(*numbers[start+mid_s:end+1])
        queue.append((start+mid_s, end, value+l_gcd))
        queue.append((start, end-mid_s, value+r_gcd))

print(answer)