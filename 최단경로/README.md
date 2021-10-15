# ⭐️ 최단 경로

> **목차**
- 📌 최단 경로란?
- 📌 다익스트라 최단 경로 알고리즘
- 📌 개선된 다익스트라 알고리즘
- 📌 플로이드 워셜 알고리즘
- 📌 벨만 포드 알고리즘

## 📌 최단 경로란?


- 가장 짧은 경로를 찾는 알고리즘
- 보통 '길 찾기' 문제라고도 불린다.

> 문제 예시
1. 한 지점에서 다른 특정 지점까지의 최단 경로
2. 한 지점에서 다른 모든 지점까지의 최단 경로
3. 모든 지점에서 다른 모든 지점까지의 최단 경로

최단 경로 문제는 보통 **그래프**를 활용해 **각 지점을 그래프의 노드**로 하고 **지점간 연결된 도로는 그래프에서 간선**으로 표현됩니다.
![](https://images.velog.io/images/tonic523/post/a11d74f5-8ee8-42ec-8e0d-a797b60789ee/image.png)

## 📌 다익스트라 최단 경로 알고리즘
다익스트라 최단 경로 알고리즘은 그리디 알고리즘 유형으로 볼 수 있습니다.
> **동작 과정**
1. 출발 노드(지점)을 설정한다.
2. 출발 노드로 부터 다른 노드들까지의 최단 거리 테이블을 초기화한다.
3. 출발 노드에 간선으로 연결된 노드들의 거리를 최단 거리 테이블에 초기화한다.
4. 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드를 선택한다.(그리디)
5. 해당 노드를 거쳐 다른 노드로 가는 비용을 계산하여 최단 거리 테이블을 갱신한다.
6. 3번, 4번, 5번을 반복한다.(출발 노드와 연결된 모든 노드에 방문하면 탈출)

![](https://images.velog.io/images/tonic523/post/11b47364-b867-420a-b94f-e947b45ed650/image.png)
1번 노드를 출발 노드로 지정
1번 노드부터 출발하기 때문에 거리 테이블에서 1번 노드는 0 입니다.
다른 노드들은 아직 거리가 어느정도인지, 연결이 되있는지 모르는 상태이기 때문에 무한으로 지정합니다.
![](https://images.velog.io/images/tonic523/post/a02d0684-346e-4069-bbc2-9b6095c9a79a/image.png)
방문하지 않은 노드 중 가장 짧은 거리 0 인 노드 1번을 방문처리합니다.
**노드 1번과 연결된 노드까지 가는 거리를 1번 노드의 거리와 합한 값 = A
원래 해당 노드의 거리테이블 값 = B**
위 A와 B를 비교해서 더 작은 값을 거리테이블에 초기화합니다.
예를 들어 1번에서 2번으로 갈 때
A = 0(1번 노드의 거리테이블 값) + 2(1번에서 2번 노드로 가는 비용)
B = 무한(초기화 전인 값)
A 가 B보다 작으므로 A로 2번 노드의 거리테이블 값을 초기화합니다.

위 과정을 1번과 연결된 모든 노드에 실행하여 거리테이블을 갱신합니다.

![](https://images.velog.io/images/tonic523/post/f10598a8-b7b3-4fca-bb42-ee22342c8316/image.png)
마찬가지로 방문하지 않은 노드 중 거리테이블에서 가장 작은 값인 4번 노드를 방문 처리합니다.
4번 노드와 연결된 3번과 5번노드 까지의 거리를 아까 A,B 비교한 것처럼 비교하여 거리테이블을 초기화합니다.

이 과정이 끝나면 다시 방문하지 않은 노드 중 가장 짧은 거리인 노드를 찾고 반복합니다.

![](https://images.velog.io/images/tonic523/post/05a20a8a-7e70-4bf4-b084-d92f33b48919/image.png)
모든 노드를 방문하고 마지막 노드인 6번을 갔을 때는 더이상 위 과정을 반복하지 않아도 됩니다.
위 그래프는 6번 노드에서 더이상 갈 수 있는 노드가 없기 때문에 아무것도 실행하지 않은 것을 알 수 있습니다.


> **구현하기 위해 필요한 로직들**
1. 거리테이블 중에서 가장 적은 값(최단 거리)을 가지는 노드의 값을 구해야 한다.
2. 최단 거리를 가지는 노드를 방문 처리한다.
3. 해당 노드에 연결된 노드들의 거리테이블을 갱신하는 로직을 구현한다.
	- 연결된 노드의 원래 거리테이블 값
    - 해당 노드의 거리테이블 값 + 연결된 간선의 비용
    - 위 두개의 값을 비교하여 작은 값으로 거리테이블 초기화

> 구현

```python
import sys
input = sys.stdin.readline
INF = int(1e9) # 10억
N, M = map(int, input().split()) # N=노드의 수, M은 간선의 수
start = int(input()) # 시작 노드
graph = [[] for _ in range(N+1)] # 그래프 초기화
distance = [INF] * (N+1) # 거리 테이블 무한으로 초기화
visited = [False] * (N+1) # 노드에 방문 유무 테이블

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c)) # a는 노드, b는 인접 노드, c는 간선 비용

def get_smallest_node():
    min_value = INF # 최소값을 무한으로 초기화
    index = 0 # 최소값인 노드의 값을 0으로 초기화
    for j in range(1, N+1): # 모든 노드 순회
        if distance[j] < min_value and not visited[j]: # 최소값보다 거리테이블 값이 작고 방문하지 않았을 때
            min_value = distance[j] # 최소값을 해당 노드의 값으로 갱신
            index = j # 해당 노드의 값으로 갱신
    return index

def dijkstra(start):
    visited[start] = True # 시작 노드 방문 처리
    distance[start] = 0 # 시작 노드의 거리 0으로 초기화
    for node, cost in graph[start]: # 시작 노드에 연결된 노드들의 거리는 간선 비용을 초기화
        distance[node] = cost
    for i in range(N-1): # 시작 노드를 제외한 N-1개의 노드에 대해 반복
        now = get_smallest_node() # 가장 짧은 노드의 값 초기화
        visited[now] = True # 해당 노드 방문 처리
        for node, cost in graph[now]: # 해당 노드와 연결된 노드들의 최단 거리 갱신
            total_cost = distance[now] + cost
            if distance[node] > total_cost:
                distance[node] = total_cost

dijkstra(start)
print(distance) # 0 노드는 없으니 무한대 값으로 반한됩니다.
```
다익스트라의 간단한 구현 방법입니다.
> **간단한 구현 방법의 성능**
- 총 O(V)번에 걸쳐서 최단 거리가 가장 짧은 노드를 매번 선형 탐색합니다.
- 따라서 전체 시간 복잡도는 O(V^2)입니다.
- 코딩테스트에서 전체 노드의 개수가 5000개 이하라면 이 코드로 문제를 해결할 수 있습니다.
- 단, 노드의 개수가 10000개를 넘어가는 문제는 해결하지 못합니다.

🧐 **노드의 개수가 많을 때는 어떡해해야 하나요??**
- 간단한 다익스트라 알고리즘에서 최단 거리가 가장 짧은 노드를 찾기 위해서 매번 거리 테이블을 선형적으로 탐색했습니다.
- 이 과정을 선형적으로 찾는 것이 아닌 더욱 빠른 방법이 있다면 알고리즘의 시간 복잡도를 개선할 수 있습니다.
- 이를 개선한 방법을 **개선된 다익스트라 알고리즘**이라고 합니다.

## 📌 개선된 다익스트라 알고리즘
개선된 다익스트라 알고리즘에서는 힙 자료구조를 사용합니다.
힙 자료구조는 우선순위 큐를 구현하기 위하여 사용하는 자료구조 중 하나입니다.
[힙이란?](https://velog.io/@tonic523/DataStructureheap)

> **힙을 사용하는 이유?**
간단한 다익스트라 알고리즘에서는 **_최단 거리가 가장 짧은 노드를 선택하는 과정_** 에서 O(N) 즉 선형적으로 탐색했습니다.
가장 짧은 값을 구하는 것이기 때문에 **최소 힙**을 사용하면 O(logN)으로 시간을 절약할 수 있습니다.

> **동작 과정**
1. 출발 노드(지점)을 설정한다.
2. 출발 노드로 부터 다른 노드들까지의 최단 거리 테이블을 초기화한다.
3. 우선순위 큐를 선언한다.
4. (0(거리), 출발 노드)를 우선순위 큐에 삽입한다.
5. 우선순위 큐에서 가장 작은 값을 가진 튜플을 호출한다.(O(logN))
6. 방문하지 않은 노드인지 확인(방문했다면 5번 실행)
7. 해당 노드를 거쳐 연결된 노드로 가는 비용을 계산하여 최단 거리 테이블을 갱신하고, 갱신됬다면 우선순위 큐에 (거리, 연결된 노드)를 추가한다.
8. 5번~7번을 반복하고 우선순위 큐가 비어있다면 실행 종료

> **구현**

```python
import sys
import heapq
input = sys.stdin.readline
INF = int(1e9) # 10억
N, M = map(int, input().split()) # N=노드의 수, M은 간선의 수
start = int(input()) # 시작 노드
graph = [[] for _ in range(N+1)] # 그래프 초기화
distance = [INF] * (N+1) # 거리 테이블 무한으로 초기화
visited = [False] * (N+1) # 노드에 방문 유무 테이블

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c)) # a는 노드, b는 인접 노드, c는 간선 비용

def dijkstra(start):
    queue = []
    distance[start] = 0 # 시작 노드의 거리 0으로 초기화
    heapq.heappush(queue, (0, start)) # 시작 노드 우선순위 큐에 추가
    while queue:
        dist, now = heapq.heappop(queue) # 최단 경로 중 가장 짧은 노드를 호출
        if visited[now]: # 방문했다면 continue
            continue
        visited[now] = True # 방문하지 않았다면 방문 처리
        for l_node, cost in graph[now]: # 연결된 노드들 순회
            total_cost = distance[now] + cost
            if distance[l_node] > total_cost: # 현재 노드에서 거리와 최단 거리 비교 후 할당
                distance[l_node] = total_cost
                heapq.heappush(queue, (distance[l_node], l_node)) # 최단 거리로 갱신되면 우선순위 큐에 추가


dijkstra(start)
print(distance) # 0 노드는 없으니 무한대 값으로 반한됩니다.
```

## 📌 플로이드 워셜 알고리즘
플로이드 워셜 알고리즘은 다이나믹 프로그래밍 알고리즘 유형으로 볼 수 있습니다.

> **목적**
모든 경로에서 부터 다른 모든 경로의 최단 거리를 알고 싶을 때 사용합니다.

> **특징**
- 시간 복잡도: O(N^3) - N = 노드의 갯수
- 구현은 다익스트라 알고리즘에 비교하면 쉬운 편
- 시간 복잡도가 크기 때문에 모든 최단 거리를 필요로 하지 않는다면 쓰지 않는 것이 좋을 것 같다.

> **동작 과정**
![](https://images.velog.io/images/tonic523/post/2a1b136d-f4e3-4399-b2fe-f1b48a35473e/image.png)
1. 2차원 그래프를 준비하고 노드마다 걸리는 간선 비용으로 초기화합니다.
![](https://images.velog.io/images/tonic523/post/d452b5fc-27e1-400b-9130-15e24dc1069e/image.png)
2. 1번 노드를 거쳐가는 모든 경우를 고려해서 위 점화식을 실행시켜 테이블을 갱신합니다.
3. 1번 -> 2번 -> ... N번까지 모든 노드를 2번의 과정을 진행합니다.

> 구현

```python
import sys
input = sys.stdin.readline
INF = int(1e9) # 무한 상수
N, M = map(int, input().split()) # 노드 갯수, 간선 갯수
distance = []
for n in range(N+1): # 2차원 거리테이블 초기화
    distance.append([INF] * (N+1))
    distance[n][n] = 0
for _ in range(M): # 거리테이블 간선입력
    a, b, c = map(int, input().split())
    distance[a][b] = c

for k in range(1, N+1): # k번 노드를 거치는 모든 경우를 고려하여 테이블 갱신
    for a in range(1, N+1):
        for b in range(1, N+1):
            distance[a][b] = min(distance[a][b], distance[a][k] + distance[k][b])

for d in distance:
    print(d)

```

## 📌 벨만 포드 알고리즘

- 음수 간선이 포함된 상황에서의 최단거리 문제

> 만약 간선 중에 음수 간선이 있다면?
> 

이 때 A 지점에서 B 지점으로 갈 때 최단거리를 구한다고 가정해봅시다.

음수 간선이 없을 때는 다익스트라로 풀이하면 값이 나오지만 음수 간선이 있다면

음수 사이클이 발생할 수 있습니다.

- 1 → 2 로 갈때 (비용 1)
- 2 → 3 로 갈때 (비용 1)
- 3 → 1 로 갈때 (비용 -3)

이렇게 되면 1 → 3으로 갈 때 -1의 비용이 듭니다.

다익스트라는 이 상황에서 모든 경로의 최소값을 계속 구해야 하기 때문에 -무한대로 가게 될 것입니다.

이렇게 음수 사이클이 발생할 때는 벨만 포드 알고리즘을 사용하면 효과적입니다.

> 특징
> 
- 음의 간선이 포함된 상황에서도 사용 가능
- 음수 간선의 순환을 감지할 수 있다.
- 시간 복잡도 - O(VE) (정점 * 간선) <다익스트라에 비해 느림>

> 구현 과정
> 
- 최단 거리 테이블 초기화
- 출발 노드 설정(출발 노드는 0으로 저장)
- 다음의 과정을 N-1번 반복
    - 전체 간선의 개수 E 를 하나 씩 확인
    - 각 간선을 거쳐 다른 노드로 가는 비용을 계산 후 최단거리 테이블 갱신
    - **만약 N번째 반복을 할 때도 최단거리 테이블 갱신을 하게 되면 음수 사이클이 있는 것이다!!**

```python
import sys

input = sys.stdin.readline

# 거리 테이블에 음수 사이클이 있는지 없는지 확인하는 알고리즘
def bf(start):
    distance = [1e9] * len(graph)
    distance[start] = 0
    for i in range(1, N+1):
        for s in range(1, N+1):
            for end, cost in graph[s]:
                cost += distance[s]
                if cost < distance[end]:
                    distance[end] = cost
                    if i == N:
                        return True
    return False
```

- 음수 사이클의 유무 뿐만아니라 최단거리 테이블도 반환할 수 있다.








