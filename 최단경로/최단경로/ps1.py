import sys
import heapq

input = sys.stdin.readline

V, E = map(int, input().rstrip().split())
start = int(input())
graph = [[] for _ in range(V+1)]
distance = []
for _ in range(E):
    a, b, c = map(int, input().rstrip().split())
    graph[a].append((b, c))

def dijkstra(start):
    queue = [(0, start)]
    distance = [1e9] * (V+1)
    distance[start] = 0
    while queue:
        d, now = heapq.heappop(queue)
        for v, cost in graph[now]:
            cost += d
            if cost < distance[v]:
                distance[v] = cost
                heapq.heappush(queue, (cost, v))
    return distance

distance = dijkstra(start)
for i in range(1, len(distance)):
    if distance[i] == 1e9:
        print("INF")
    else:
        print(distance[i])