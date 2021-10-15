# [최소비용 구하기](https://www.acmicpc.net/problem/1916)

## 풀이1
- 성공

> 그냥 다익스트라로 풀면 안되나?

다익스트라로 풀었지만 시간초과가 나왔다..\
이 문제의 시간 제한은 0.5초로 매우 짧았다.\
따라서 다익스트라로 풀이하되 더 효율적인 방안을 찾아야 한다.

> 도착지는 한 곳!

다익스트라를 그냥 풀이하면 출발 지점에서 모든 지점에 대한 최단경로를 구하게 된다.\
하지만 이 문제에서는 한 곳만 값을 얻으면 되기 때문에 해단 최단경로를 구하면 바로 값을 반환하는 로직을 구현하면 된다.
```python
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
```

위에서 보듯이 우선순위 큐에서 최소값을 꺼내왔을 때 도착지점이라면 그 비용을 반환하면 조금 더 효율적인 알고리즘을 구현할 수 있다.