import sys
import heapq

input = sys.stdin.readline
heap = []
answer = []
for _ in range(int(input())):
    c = int(input().rstrip())
    if c:
        if c > 0:
            heapq.heappush(heap, (c, c))
        else:
            heapq.heappush(heap, (-(c+0.5), c))
    else:
        if heap:
            answer.append(heapq.heappop(heap)[1])
        else:
            answer.append(0)
print("\n".join(list(map(str, answer))))