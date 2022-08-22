import sys

input = sys.stdin.readline

N, people_c = map(int, input().rstrip().split())

capacitys = [int(input()) for _ in range(N)]

right = sum(capacitys) // people_c
left = 0

def cal_bottle_c(mid):
    bottle_c = 0
    for c in capacitys:
        bottle_c += c // mid
    return bottle_c

while left <= right:
    mid = (right + left) // 2
    if mid == 0:
        mid += 1
    bottle_c = cal_bottle_c(mid)
    if people_c <= bottle_c:
        left = mid + 1
    else:
        right = mid - 1


print(right)