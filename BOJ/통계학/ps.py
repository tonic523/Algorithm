import sys
from collections import Counter

N = int(input())
arr = []
for _ in range(N):
    arr.append(int(sys.stdin.readline().rstrip()))
arr.sort()

counter = dict(Counter(arr))
counter = sorted(counter.items(), key = lambda item: item[1], reverse=True)
most = counter[0]
if len(counter) > 1 and most[1] == counter[1][1]:
    most = counter[1]

mid = 0 if N == 1 else N//2

print(round(sum(arr)/N))
print(arr[mid])
print(most[0])
print(arr[-1]-arr[0])