# 마인크래프트

[BOJ 18111](https://www.acmicpc.net/problem/18111)

> 풀이

### 첫 번째 풀이
이진탐색으로 풀이했습니다.

```python
import sys

N,M,B = map(int, sys.stdin.readline().rstrip().split())

lands = []
for _ in range(N):
    lands += list(map(int, sys.stdin.readline().rstrip().split()))

start = 0
end = max(lands)
time = 0
result = [-1, 0]
while start <= end: # start,end,mid 는 땅의 높이
    mid = (start + end) // 2
    bag = B
    time = 0 # 걸린 시간
    for land in lands:
        if land < mid:
            bag -= mid - land
            time += mid - land
        elif land > mid:
            bag += land - mid
            time += 2 * (land - mid)
    if bag >= 0:
        if result[0] == -1:
            result = [time, mid]
        else:
            if result[0] < time:
                pass
            elif result[0] == time and result[1] >= mid:
                pass
            else:
                result = [time, mid]
        start = mid + 1
    else:
        end = mid - 1
print(result[0], result[1])
```

시간 초과

```python
import sys

N,M,B = map(int, sys.stdin.readline().rstrip().split())

lands = []
for _ in range(N):
    lands += list(map(int, sys.stdin.readline().rstrip().split()))

start = 0
end = max(lands)
time = 0
result = [-1, 0]

for h in range(1, 257): # 256
    bag = B
    time = 0
    for land in lands: # 25000
        if land < h:
            bag -= h - land
            time += h - land
        elif land > h:
            bag += land - h
            time += 2 * (land - h)
    if bag >= 0:
        if result[0] == -1:
            result = [time, h]
        else:
            if result[0] < time:
                continue
            elif result[0] == time and result[1] >= h:
                continue
            else:
                result = [time, h]

print(result[0], result[1])
```