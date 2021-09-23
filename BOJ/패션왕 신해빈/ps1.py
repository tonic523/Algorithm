import sys
from itertools import combinations

input = sys.stdin.readline

for _ in range(int(input())):
    N = int(input())
    clothes = {}
    result = N
    for _ in range(N):
        _, b = input().rstrip().split()
        if clothes.get(b):
            clothes[b] += 1
        else:
            clothes[b] = 1
    i = 2
    while i < N:
        temp = list(combinations(clothes, i))
        for t in temp:
            temp2 = 1
            for t2 in t:
                temp2 *= clothes[t2]
            result += temp2
        i += 1
    print(result)