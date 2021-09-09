import sys
import heapq

input = sys.stdin.readline
INF = int(1e9) # 무한 상수
# 노드 개수, 간선 개수, 시작 노드
N, M, C = map(int, input().split())
distance = [INF] * (N+1)
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

def dijkstra(start):
    # 시작 노드 최단 거리 0 으로 초기화
    distance[start] = 0
    # 시작 노드 큐에 삽입
    queue = [(0, start)]
    # 큐가 없을 때까지
    while queue:
        # 우선순위 큐에서 가장 작은 값 꺼내기
        min_value, now = heapq.heappop(queue)
        # 큐 삽입하고 나중에 거리가 갱신됬다면 continue
        if min_value > distance[now]:
            continue
        # 해당 노드와 연결된 노드들의 거리 갱신, 갱신 됬다면 우선순위 큐에 삽입
        for n, cost in graph[now]:
            if distance[n] > distance[now] + cost:
                distance[n] = distance[now] + cost
                heapq.heappush(queue, (distance[n], n))

dijkstra(C)
# 메시지를 받은 도시의 개수, 도시들이 모두 메시지를 받는데 걸린 시간 출력
count = 0
max_value = 0
for d in distance:
    if d != INF:
        count += 1
        max_value = max(max_value, d)
print(count-1, max_value)