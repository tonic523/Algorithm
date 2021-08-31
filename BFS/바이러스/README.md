# 바이러스

[BOJ 2606](https://www.acmicpc.net/problem/2606)

> 풀이1

DFS 알고리즘으로 풀었습니다.\
우선 컴퓨터들이 서로 연결된 자료구조를 리스트안에 리스트로 구현했습니다.\
```python
computers = [[0] for _ in range(101)]
// [[0],[0],[0]]
```
1 3 이라는 값이 들어오면 리스트에서 1 인덱스 3을 추가하고 3 인덱스에 1을 추가합니다.\
```python
def virus(key):
    result = 0
    v_computers = computers[key]
    for idx, v_computer in enumerate(v_computers):
        if idx == 0:
            if v_computer == 1:
                return -1
            else:
                computers[key][0] = 1
        else:
            result += virus(v_computer) + 1
    return result
```
인덱스 1부터 위의 함수를 실행합니다.
- 처음 방문이라면 1 인덱스의 첫번째 원소값인 0을 1로 바꿔줍니다.
- 그 후 값이 있다면 차례로 위 함수를 실행하면서 카운트를 더해줍니다.
- 최종적으로 1 과 연결된 카운트 수를 리턴합니다.

> 풀이2

BFS 알고리즘으로 풀었습니다.\
컴퓨터들의 연결된 자료구조는 딕셔너리를 사용했고 방문한 컴퓨터를 구분하기 위해 리스트를 따로 구현했습니다.\
```python
computers = { k : [] for k in range(1, N+1)}
visited = [0] * (N+1)
```
bfs 함수에서는 큐 자료구조를 활용해 1에서 연결된 컴퓨터를 스택처럼 쌓고 연결된 컴퓨터를 모두 방문하면 방문했던 수를\
카운트 한 값을 리턴하게 했습니다.
```python
def bfs():
    q = deque([1])
    result = -1
    while q:
        v_com = q.popleft()
        if visited[v_com]:
            continue
        else:
            visited[v_com] = 1
            v_coms = computers[v_com]
            q.extend(v_coms)
            result += 1
    return result
```