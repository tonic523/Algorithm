import sys
import heapq

input = sys.stdin.readline

def dijkstra(start, graph):
    distance = [1e9] * len(graph)
    queue = [(0, start)]
    distance[start] = 0

    while queue:
        c, now = heapq.heappop(queue)
        for v, cost in graph[now]:
            cost += c
            if distance[v] >= 0 and cost < distance[v]:
                distance[v] = cost
                heapq.heappush(queue, (cost, v))
    return distance


for _ in range(int(input())):
    N, M, W = map(int, input().rstrip().split())
    graph = [[] for _ in range(N+1)]
    r_graph = [[] for _ in range(N+1)]
    answer = "NO"
    for _ in range(M):
        a, b, c = map(int, input().rstrip().split())
        graph[a].append((b, c))
        graph[b].append((a, c))

    for _ in range(W):
        a, b, c = map(int, input().rstrip().split())
        graph[a].append((b, -c))
        r_graph[b].append((a, c))
    for start in range(1, N+1): # O(N)
        b = True
        from_start_d = dijkstra(start, graph) # O(NlogN)
        to_start_d = dijkstra(start, r_graph) # O(NlogN)
        for i in range(1, N+1):
            if from_start_d[i] + to_start_d[i] < 0:
                answer = "YES"
                b = False
                break
        if not b:
            break
    print(answer)