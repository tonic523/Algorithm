import sys
import heapq

input = sys.stdin.readline

N, M, X = map(int, input().rstrip().split())
graph = [[] for _ in range(N+1)]
reverse_graph = [[] for _ in range(N+1)]
for _ in range(M):
    start, end, time = map(int, input().rstrip().split())
    graph[start].append((end, time))
    reverse_graph[end].append((start, time))

def dijkstra(v, graph):
    visited = [False] * (N + 1)
    distance = [1e9] * (N + 1)
    distance[v] = 0
    queue = [(0, v)]
    while queue:
        d, now = heapq.heappop(queue)
        visited[now] = True
        for m_v, m_d in graph[now]:
            if not visited[m_v]:
                short_d = distance[m_v] if distance[m_v] < d + m_d else d + m_d
                distance[m_v] = short_d
                heapq.heappush(queue, (short_d, m_v))
    return distance

distance_from_X = dijkstra(X, graph)
distance_to_X = dijkstra(X, reverse_graph)
answer = 0

for i in range(1, N+1):
    total_distance = distance_to_X[i] + distance_from_X[i]
    answer = answer if answer > total_distance else total_distance

print(answer)