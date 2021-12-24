import sys

input = sys.stdin.readline

# 테스트 케이스
for t in range(int(input())):
    k = int(input())
    n = int(input())
    floor_list = [i for i in range(1, n+1)]
    for i in range(k):
        for j in range(1, n):
            floor_list[j] += floor_list[j-1]
    print(floor_list.pop())