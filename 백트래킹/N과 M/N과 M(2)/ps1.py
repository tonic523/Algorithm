import sys
from itertools import combinations

input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

li = [i for i in range(1, N+1)]

for i in list(combinations(li, M)):
    print(*i)