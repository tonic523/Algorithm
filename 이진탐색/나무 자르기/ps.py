import sys
from collections import Counter

N, M = map(int, sys.stdin.readline().rstrip().split())
trees = Counter(map(int, sys.stdin.readline().rstrip().split()))

start = 0
end = max(trees)

while start <= end: # 최대 약 20번 정도?
    mid = (start + end) // 2
    sum_len = 0
    for tree, num in trees.items(): # 최대 1000000
        len = tree-mid
        if len > 0:
            sum_len += len * num
    if sum_len < M:
        end = mid - 1
    elif sum_len >= M:
        start = mid + 1
print(end)