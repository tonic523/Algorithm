import sys
import heapq

input = sys.stdin.readline

N, E = map(int, input().strip().split())
graph = [[] for _ in range(N+1)]
for _ in range(E):
    a, b, c = map(int, input().strip().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, input().strip().split())

def dijkstra(start, end):
    queue = [(0,start)]
    distance = [1e9] * (N+1)
    distance[start] = 0
    while queue:
        now_c, now = heapq.heappop(queue)
        for v, cost in graph[now]:
            cost += now_c
            if cost < distance[v]:
                distance[v] = cost
                heapq.heappush(queue, (cost, v))
    return distance[end]

v1_to_v2 = dijkstra(v1, v2)
start_v1_v2_N = dijkstra(1, v1) + v1_to_v2 + dijkstra(v2, N)
start_v2_v1_N = dijkstra(1, v2) + v1_to_v2 + dijkstra(v1, N)
answer = start_v1_v2_N if start_v1_v2_N < start_v2_v1_N else start_v2_v1_N
print(answer if answer < 1e9 else -1)