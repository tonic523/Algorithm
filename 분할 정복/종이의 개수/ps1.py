import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
result = [0,0,0]
graph = []
for _ in range(N):
    temp = list(map(int, input().rstrip().split()))
    graph.append(temp)

def isEqual(r_s, c_s, length):
    for r in range(length):
        for c in range(length):
            if graph[r_s + r][c_s + c] != graph[r_s][c_s]:
                return False
    return True

queue = deque()
queue.append((0,0,N))

while queue:
    r_s, c_s, length = queue.popleft()
    if not isEqual(r_s, c_s, length):
        new_length = length // 3
        for i in range(3):
            for j in range(3):
                if new_length == 1:
                    result[graph[r_s + new_length * i][c_s + new_length * j] + 1] += 1
                else:
                    queue.append((r_s + new_length * i, c_s + new_length * j, new_length))
    else:
        result[graph[r_s][c_s] + 1] += 1
print("\n".join(map(str, result)))
