import sys

input = sys.stdin.readline
INF = int(1e9) # 무한 상수

# 노드의 갯수, 간선의 갯수, 시작 노드 입력
N, M, C = map(int, input().split())
# 최단 거리 테이블 무한으로 초기화
distance = [INF] * (N+1)
# 각 노드의 연결된 노드와 간선의 값을 저장하는 그래프 초기화
graph = [[] for _ in range(N+1)]
# 방문테이블 초기화
visited = [False] * (N+1)
# 연결된 노드, 간선 입력
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))

# 방문하지 않았고 거리 테이블에서 가장 작은 값인 노드 반환
def get_smallest_node():
    index = 0
    min_value = INF
    for node, dist in enumerate(distance):
        if min_value > dist and not visited[node]:
            min_value = dist
            index = node
    return index

# 다익스트라 알고리즘
def dijkstra(start):
    visited[start] = True
    distance[start] = 0
    # 시작 노드와 연결된 노드의 거리 테이블 초기화
    for n, d in graph[start]:
        distance[n] = d
    # 시작 노드를 제외한 모든 노드를 순회하면서 거리테이블 초기화
    for i in range(N - 1):
        now = get_smallest_node()
        # 방문 유무 체크
        if visited[now]:
            continue
        else:
            visited[now] = True
        # 노드와 연결된 노드들의 거리테이블 초기화
        for l_node, cost in graph[now]:
            if distance[l_node] > distance[now] + cost:
                distance[l_node] = distance[now] + cost

dijkstra(C)
count = 0
time = 0
for d in distance:
    if d != 0 and d != INF:
        count += 1
        time = d if time < d else time
print(count, time)