import sys
import heapq

input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(int(input())):
    a, b, c = map(int, input().rstrip().split())
    graph[a].append((b, c))

def dijkstra(start, end):
    distance = [1e9] * (N+1)
    queue = [(0, start)]
    distance[start] = 0

    while queue:
        cost, v = heapq.heappop(queue)
        # 제한시간이 0.5초밖에 안되기 때문에 좀 더 효율적인 방법 추가
        if v == end:
            return cost
        for m_v, m_c in graph[v]:
            m_c += cost
            if m_c < distance[m_v]:
                distance[m_v] = m_c
                heapq.heappush(queue, (m_c, m_v))

    return distance[end]

start, end = map(int, input().rstrip().split())
print(dijkstra(start, end))