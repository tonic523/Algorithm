import sys

input = sys.stdin.readline

for _ in range(int(input())):
    N = int(input())
    clothes = {}
    result = 1
    for _ in range(N):
        _, b = input().rstrip().split()
        if clothes.get(b):
            clothes[b] += 1
        else:
            clothes[b] = 1
    for v in clothes.values():
        result *= v + 1

    print(result - 1)